import json
import requests
from Bridges.data_src_dependent import EarthquakeUSGS
from Bridges.data_src_dependent import ActorMovieIMDB
from Bridges.data_src_dependent import Game
from Bridges.data_src_dependent import Shakespeare
from Bridges.data_src_dependent import GutenbergBook
from Bridges.data_src_dependent import CancerIncidence
from Bridges.data_src_dependent import Song


def getGameData():

    wrapper = []

    url = "http://bridgesdata.herokuapp.com/api/games"
    PARAMS = {"Accept: application/json"}

    r = requests.get(url=url, params=str(PARAMS))

    r = r.json()

    D = r["data"]
    # print(D)

    for i in range(len(D)):
        V = D[i]
        G = V["genre"]
        genre = []
        for j in range(len(G)):
            genre.append(str(G[j]))
        wrapper.append(Game.Game(V["game"], V["platform"], V["rating"], genre))
    return wrapper


def getActorMovieIMDBData(number = 0):

    wrapper = []

    url = "http://bridgesdata.herokuapp.com/api/imdb?limit=" + str(number)
    PARAMS = {"Accept: application/json"}

    r = requests.get(url=url, params=str(PARAMS))
    # print(r.status_code, r.reason)

    data = r.json()

    D = data["data"]

    for i in range(len(D)):
        V = D[i]
        wrapper.append(ActorMovieIMDB.ActorMovieIMDB(V["actor"], V["movie"]))

    return wrapper

def getEarthquakeUSGSData(number = 0):

    wrapper = []
    url = "http://earthquakes-uncc.herokuapp.com/eq"
    latest_url = "http://earthquakes-uncc.herokuapp.com/eq/latest/" + str(number)
    PARAMS = {"Accept: application/json"}

    if number <= 0:
        r = requests.get(url=url, params=str(PARAMS))
        r = r.json()
        for i in range(len(r)):
            V = r[i]["properties"]
            G = r[i]["geometry"]["coordinates"]
            wrapper.append(EarthquakeUSGS.EarthquakeUSGS(V["mag"], G[0], G[1], V["place"], V["title"], V["url"], V["time"]))
    else:
        r = requests.get(url=latest_url, params=str(PARAMS))
        data = r.json()
        D = data["Earthquakes"]
        for i in range(len(D)):
            V = D[i]["properties"]
            G = D[i]["geometry"]["coordinates"]
            wrapper.append(EarthquakeUSGS.EarthquakeUSGS(V["mag"], G[0], G[1], V["place"], V["title"], V["url"], V["time"]))
    return wrapper


def getShakespeareData(endpoint = "", textonly = False):
    wrapper = []
    url = "http://bridgesdata.herokuapp.com/api/shakespeare/"
    PARAMS = {"Accept: application/json"}

    if endpoint == "plays" or endpoint == "poems":
        url += "/" + endpoint
    if textonly:
        url += "?format=simple"

    r = requests.get(url = url, params = str(PARAMS))
    r = r.json()

    D = r["data"]
    for i in range(len(D)):
        V = D[i]
        wrapper.append(Shakespeare.Shakespeare(V["title"], V["type"], V["text"]))
    return wrapper

def getGutenBergBookData(num = 0):
    wrapper = []
    url = "http://bridgesdata.herokuapp.com/api/books"
    PARAMS = {"Accept: application/json"}

    if num > 0:
        url += "?limit=" + str(num)

    r = requests.get(url=url, params = str(PARAMS))
    r = r.json()

    D = r["data"]
    for i in range(len(D)):
        V = D[i]

        A = V["author"]
        L = V["languages"]

        lang = []

        for j in range(len(L)):
            lang.append(str(L[j]))

        G = V["genres"]
        genre = []

        for j in range(len(G)):
            genre.append(str(G[j]))

        S = V["subjects"]
        subject = []
        for j in range(len(S)):
            subject.append(str(S[j]))

        M = V["metrics"]
        wrapper.append(GutenbergBook.GutenbergBook(A["name"], A["birth"], A["death"], V["title"],
                                                   lang, genre, subject, M["characters"], M["words"],
                                                   M["sentences"], M["difficultWords"], V["url"], V["downloads"]))

    return wrapper


def getCancerIncidentData(num = 0):

    wrapper = []
    url = "https://bridgesdata.herokuapp.com/api/cancer/withlocations"
    PARAMS = {"Accept: application/json"}

    if num > 0:
        url += "?limit="+str(num)

    r = requests.get(url=url, params=str(PARAMS))
    r = r.json()

    D = r["data"]

    # c = CancerIncidence.CancerIncidence()
    for i in range(len(D)):
        c = CancerIncidence.CancerIncidence()
        v = D[i]
        age = v["Age"]
        c.setAgeAdjustedRate(age["Age Adjusted Rate"])
        c.setAgeAdjustedCI_Lower(age["Age Adjusted CI Lower"])
        c.setAgeAdjustedCI_Upper(age["Age Adjusted CI Upper"])
        c.setYear(v["Year"])

        data = v["Data"]

        c.setCrudeRate(data["Crude Rate"])
        c.setCrudeRate_CI_lower(data["Crude CI Lower"])
        c.setCrudeRate_CI_Upper(data["Crude CI Upper"])
        c.setRace(data["Race"])
        c.setPopulation(data["Population"])
        c.setEventType(data["Event Type"])
        c.setAffectedArea(v["Area"])

        loc = v["loc"]

        c.setLocationX(loc[0])
        c.setLocationY(loc[1])

        wrapper.append(c)
    return wrapper


def getSong(songTitle, artistName = None):
    wrapper = []
    url = "http://bridgesdata.herokuapp.com/api/songs/find/"
    PARAMS = {"Accept: application/json"}

    if len(songTitle):
        url += songTitle

    if artistName is not None:
        if len(artistName):
            url += "?artistName=" + artistName

    url.replace(" ", "%20")

    r = requests.get(url = url, params = str(PARAMS))
    r = r.json()
    if "artist" in r:
        artist = r["artist"]
    else:
        artist = ""
    if "song" in r:
        song = r["song"]
    else:
        song = ""
    if "album" in r:
        album = r["album"]
    else:
        album = ""
    if "lyrics" in r:
        lyrics = r["lyrics"]
    else:
        lyrics = ""
    if "release_date" in r:
        release_date = r["release_date"]
    else:
        release_date = ""

    return Song.Song(artist, song, album, lyrics, release_date)


def getSongData():
    all_songs = []
    url = "http://bridgesdata.herokuapp.com/api/songs/"
    PARAMS = {"Accept: application/json"}

    r = requests.get(url = url, params = str(PARAMS))
    r = r.json()

    D = r["data"]

    for i in range(len(D)):
        v = D[i]

        if "artist" in v:
            artist = v["artist"]
        else:
            artist = ""

        if "song" in v:
            song = v["song"]
        else:
            song = ""

        if "album" in v:
            album = v["album"]
        else:
            album = ""

        if "lyrics" in v:
            lyrics = v["lyrics"]
        else:
            lyrics = ""

        if "release_date" in v:
            release_date = v["release_date"]
        else:
            release_date = ""

        all_songs.append(Song.Song(artist, song, album, lyrics, release_date))
    return all_songs

class DataSource:
    pass






