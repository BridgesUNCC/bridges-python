#!/usr/bin/env python
import base64
import wave
import json
import array
import math
from bridges.audio_channel import AudioChannel

##
#  @brief This is a class in BRIDGES for multi-channel audio data
#
#  This class contains a list of channels that contain sample data. The samples audio are 
#  encoded in 8, 16, 24, or 32 bit integers. All methods use 32 bits when taking and returning samples.
#
#  @author Luke Sloop
#
#  @date 2020, 1/31/2020
#
class AudioClip(object):
    def __init__(self, filepath: str="", sample_count: int=0, sample_rate: int=44100, num_channels: int=1, sample_bits: int=32) -> None:
        """
        AudioBase constructor
        Args:
            (int) sample_count: The total number of samples in this audio object
            (int) sample_rate: The number of samples in 1 second of audio default cd quality (44100)
        Returns:
            None
        """
        if filepath != "":
            self._from_filepath(filepath)
            return

        if sample_count > 1000000000:
            raise ValueError("Maximum frames exceeded with value %d" % self.get_sample_count())
        
        self.sample_count = sample_count
        self.sample_rate = sample_rate
        self.sample_bits = sample_bits

        self.num_channels = num_channels
        # Initialize the channels
        self._channels = []
        for i in range(self.num_channels):
            self._channels.append(AudioChannel(sample_count=self.sample_count, sample_bits=self.sample_bits)) 

    def _from_filepath(self, filepath: str):
        with wave.open(filepath, "r") as f:
            self.__init__(sample_count=f.getnframes(), sample_rate=f.getframerate(), num_channels=f.getnchannels(), sample_bits=f.getsampwidth()*8)

            self.framebytes = f.readframes(f.getnframes())
            framebytes = self.framebytes

            channel = 0
            count = 0
            for i in range(0, len(framebytes), self.get_sample_bytes()):
                if self.get_sample_bytes() != 3:
                    val = int.from_bytes(framebytes[i:i+self.get_sample_bytes()], byteorder='little', signed=True)
                    scaled = (val / ((2 ** self.get_sample_bits() / 2) - 1)) * ((2 ** 32 / 2) - 1)
                    self.set_sample(channel, count, val)
                else:
                    # Pad an empty byte to the start of 24 bit waves
                    val = int.from_bytes(b'\x00' + framebytes[i:i+self.get_sample_bytes()], byteorder='little', signed=True)
                    scaled = (val / ((2 ** self.get_sample_bits() / 2) - 1)) * ((2 ** 32 / 2) - 1)
                    self.set_sample(channel, count, val)
                
                channel += 1

                if channel >= f.getnchannels():
                    count += 1
                    channel = 0

    def get_num_channels(self) -> int:
        """
        Return the number of channels in this AudioClip. 1 for mono, 2 for stereo, etc.
        Returns:
            int: The number of channels of audio samples this object holds.
        """
        return self.num_channels

    def get_channel(self, index: int) -> AudioChannel:
        """
        Get the audio channel at index. The index should be less than get_num_channels().
        Args:
            (int) index: The index of the channel to get. 0 for front-left, 1 for front-right, etc.
        Returns:
            AudioChannel: The audio channel at index
        """
        return self._channels[index]

    def get_sample_rate(self) -> int:
        """
        Get the sample rate of this audio clip. This is the number of samples that are taken in one second.
        The default is CD Quality (44100).
        Returns:
            int: The sample rate or number of samples in 1 second of audio
        """
        return self.sample_rate

    def get_sample_count(self) -> int:
        """
        Get the number of samples in each channel of this audio object. 
        Each channel will contain this number of samples.
        Returns:
            int: The total number of samples in this audio object
        """
        return self.sample_count

    def get_sample(self, channel: int, index: int) -> int:
        """
        Get the sample at the index of the sample data from a specific channel.
        Args:
            (int) channel: The index of the channel to get. 0 for front-left, 1 for front-right, etc.
            (int) index: The index of the sample to get. From 0 - get_sample_count()
        Returns:
            int: The 32 bit sample
        """
        value = self.get_channel(channel).get_sample(index)

        minmax32 = (2 ** 32 // 2) - 1
        minmaxbit = (2 ** self.get_sample_bits() // 2) - 1

        scaled_sample = (value / minmaxbit) * minmax32
        return int(scaled_sample)

    def set_sample(self, channel: int, index: int, value: int) -> None:
        """
        Set the sample at the index of the sample data to value
        Args:
            (int) channel: The index of the channel to get. 0 for front-left, 1 for front-right, etc.
            (int) index: The index of sampledata to set which must be less than get_sample_count()
            (int) value: The value to set the sample to which must be a valid signed integer with bit length get_sample_bits()
        Returns:
            None
        """
        minmax32 = (2 ** 32 // 2) - 1
        if value < -minmax32 - 1:
            raise ValueError("Sample value out of minimum for signed 32 bit integer with value %d" % (value))
        if value > minmax32:
            raise ValueError("Sample value out of maxmium for signed 32 bit integer with value %d" % (value))
        
        minmaxbit = (2 ** self.get_sample_bits() // 2) - 1
        scaled_sample = (value / minmax32) * minmaxbit

        self.get_channel(channel).set_sample(index, int(value))

    def get_sample_bits(self) -> int:
        """
        Get the number of bits for the samples in this audio clip.  Will be 8, 16, 24, or 32 bits.
        Returns:
            int: The number of bits for each sample 
        """
        return self.sample_bits

    def get_sample_bytes(self) -> int:
        """
        Get the number of bytes for the samples in this audio clip.  Will be 1, 2, 3, or 4 bits.
        Returns:
            int: The number of bytes for each sample 
        """
        return self.sample_bits // 8

    def _get_type_code(self) -> str:
        if self.get_sample_bytes() == 1:
            return "b"
        elif self.get_sample_bytes() == 2:
            return "h"
        elif self.get_sample_bytes() == 3:
            return "f"
        elif self.get_sample_bytes() == 4:
            return "l"
        else:
            raise ValueError("Wave file sample bytes of unsupported length %d, supported lengths are 8, 16, 24, and 32 bit" % (self.get_sample_bytes() * 8))

    def get_data_structure_type(self) -> str:
        """
        Get the data structure type
        Returns:
            str : data structure type
        """
        return "Audio"

    def get_data_structure_representation(self) -> dict:
        """ Return a dictionary of the data in this audio file
        Returns:
            dict: The data of this audio file
        """
        json_dict = {}

        json_dict["encoding"] = "RAW"
        json_dict["numChannels"] = self.num_channels
        json_dict["sampleRate"] = self.get_sample_rate()
        json_dict["bitsPerSample"] = self.get_sample_bits()
        json_dict["numSamples"] = self.get_sample_count()

        # Combine all channel data
        framedata = []
        for i in range(self.sample_count):
            for c in range(self.num_channels):
                # Go straight to channel sample for correct bit data
                framedata.append(self._channels[c].get_sample(i))

        if self.get_sample_bytes() == 4:
            newarr = []
            for val in framedata:
                minmax32 = (2 ** 32 / 2.0) - 1
                minmax16 = (2 ** 16 / 2.0) - 1

                newval = (val / minmax32) * minmax16

                newarr.append(int(newval))

            json_dict["bitsPerSample"] = 16
            json_dict["samples"] = base64.b64encode(array.array("h", newarr).tobytes()).decode("utf-8")
        elif self.get_sample_bytes() != 3:
            json_dict["samples"] = base64.b64encode(array.array(self._get_type_code(), framedata).tobytes()).decode("utf-8")
        else:
            # 24 Bit samples have a pad that must be removed first
            shiftedbytes = bytearray()
            for sample in framedata:
                shiftedbytes += int.to_bytes(sample >> 8, length=3, byteorder='little', signed=True)

            json_dict["samples"] = base64.b64encode(shiftedbytes).decode("utf-8")

        return json_dict

    def display(self) -> None:
        """ Print information about this audio file to the console
        """
        print("Num Channels: %d, Sample Rate: %d, Sample Bits: %d, Num Samples: %d" % (self.num_channels, self.sample_rate, self.get_sample_bits(), self.get_sample_count()))

    def audio_from_json(json_dict: dict) -> 'AudioClip':
        """ Create an AudioClip from a json dictionary created by another AudioClip object
        Args:
            (dict) json_dict: The json dictionary created by another AudioClip object
        """
        audio = AudioClip(sample_count=json_dict["numSamples"], num_channels=json_dict["numChannels"], sample_rate=json_dict["sampleRate"], sample_bits=json_dict["bitsPerSample"])
        
        data = []
        if audio.get_sample_bytes() != 3:
            data = array.array(audio._get_type_code(), base64.b64decode(json_dict["samples"]))
        else:
            # No simple type to convert 24 bit base64 string to integer array
            chunk = base64.b64decode(json_dict["samples"])

            for i in range(0, len(chunk), audio.get_sample_bytes()):
                data.append(int.from_bytes(chunk[i:i+audio.get_sample_bytes()], byteorder='little', signed=True))

        for i in range(audio.get_sample_count() * audio.get_num_channels()):
            audio.set_sample(i % audio.get_num_channels(), int(i / audio.get_num_channels()), (data[i] / ((2 ** audio.get_sample_bits() / 2) - 1) * ((2 ** 32 / 2) - 1)))

        return audio