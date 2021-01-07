#!/usr/bin/env python
import base64
import wave
import json
import array
import math
from bridges.audio_channel import AudioChannel

class AudioClip(object):
    """
    @brief This class provides support for reading, modifying, and playing, audio waveform.
    
    This class provides a way to represent an AudioClip (think of a
    WAV file) in Bridges as waveforms.
    
    An AudioClip can be composed of multiple channels: a stereo sound
    would be composed of 2 channels (Left and Right), a mono sound
    would be composed of a single channel. A 5.1 sound would be
    composed of 6 channels. When building an AudioClip from a file, the
    number of channels is taken from the file; some constructors have a
    num_channels parameter that enables to pass the number of channels
    explicitly. If unsure, one can know how many channels are in an
    audio clip using get_num_channels().
    
    Each channel is essentially a 1D signal. That is to say, it is an
    array of values that represent how far the membrane of a speaker
    should be from its resting position. The quality of the sound is
    controlled by two parameters: sampling rate and sampling depth.
    
    Sampling rate tells how many positions per second are encoded by
    the AudioClip. It is expressed in Hertz. CD quality is 44100Hz;
    while walkie-talkies use 8000Hz. It is set automatically if read
    from a file; or it can be passed as the sampleRate parameter to
    some of the constructors. The sampling rate can be obtained from an
    AudioClip using get_sample_rate().
     
    The length of an AudioClip is expressed in number of samples. So if
    an AudioClip is composed of 16,000 samples with a sampling rate of
    8000Hz, the clip would be 2 seconds long. The number of samples
    can obtained with get_sample_count(); it is set from a file or can be
    passed as the sampleCount parameter of some of the constructor.
    
    The sampling depth indicates how many different positions the
    membrane can take. It is typically expressed in bits with supported
    values being 8-bit, 16-bit, 24-bit, and 32-bit. If a clip is
    encoded with a depth of 8 bits, the membrane can take 2^8 different
    position ranging from -128 to +127, with 0 being the resting
    position. The sampling depth is read from files or passed as the
    sampleBits parameter of the constructor. The sampling depth of an
    existing clip can be obtained with get_sample_bits().
    
    The individual samples are accessed with the get_sample() and
    set_sample() functions. The samples are integer values in the
    2^(get_sample_bits()-1) ; 2^(get_sample_bits()-1)[ range. The
    functions allow to specify for channel and sample index.
    
    @author Luke Sloop, Erik Saule
    
    @date 2020, 1/31/2020, 2021
    """
    def __init__(self, filepath: str="", sample_count: int=0, num_channels: int=1, sample_bits: int=32, sample_rate: int=44100) -> None:
        """
        AudioBase constructor.
        specify either a filepath or all the other parameters.
        Args:
            (str) filepath: name of the wav file to creat a clip of. If this parameter is used, all the other ones are ignored.
            (int) sample_count: The total number of samples in this audio object
            (int) num_channels: number of channels (stereo would be 2)
            (int) sample_rate: The number of samples in 1 second of audio (default to cd quality: 44100)
            (int) sample_bits: Bit depth, that is to say, each sample will be in the [-2^(get_sample_bits()-1) ; 2^(get_sample_bits()-1)[ range
        Returns:
            None
        """
        if filepath != "":
            self._from_filepath(filepath)
            return

        if sample_count > 1000000000:
            raise ValueError("Maximum frames exceeded with value %d" % self.get_sample_count())

        if sample_bits != 8 and sample_bits != 16 and sample_bits != 24 and sample_bits != 32:
            raise ValueError("sample_bits should be 8, 16, 24, or 32")

        if num_channels <= 0:
            raise ValueError("num_channels should be positive")

        if sample_rate <= 0:
            raise ValueError("sample_rate should be positive")
        
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
                if self.get_sample_bytes() == 1:
                    val = int.from_bytes(framebytes[i:i+self.get_sample_bytes()], byteorder='little', signed=False)
                    val = val - 128
                    self.set_sample(channel, count, val)
                else:
                    val = int.from_bytes(framebytes[i:i+self.get_sample_bytes()], byteorder='little', signed=True)
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
            int: The sample in the [-2^(get_sample_bits()-1) ;  2^(get_sample_bits()-1)) range
        """
        value = self.get_channel(channel).get_sample(index)

        return int(value)

    def set_sample(self, channel: int, index: int, value: int) -> None:
        """
        Set the sample at the index of the sample data to value
        Args:
            (int) channel: The index of the channel to get. 0 for front-left, 1 for front-right, etc.
            (int) index: The index of sampledata to set which must be less than get_sample_count()
            (int) value: The value to set the sample to which must be a valid signed integer with bit length get_sample_bits(). That is to say in the [-2^(get_sample_bits()-1) ;  2^(get_sample_bits()-1)) range).
        Returns:
            None
        """

        if (value < -2**(self.get_sample_bits()-1)) or (value >= 2**(self.get_sample_bits()-1)):
            raise ValueError("Audio value Out of Bound. Should be in [-2^(get_sample_bits()-1) ;  2^(get_sample_bits()-1)) range")
        
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
            shiftedbytes = bytearray()
            for sample in framedata:
                shiftedbytes += int.to_bytes(sample, length=3, byteorder='little', signed=True)

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
