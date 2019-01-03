import json
import requests
from Bridges.data_src_dependent import EarthquakeUSGS
from Bridges.data_src_dependent import ActorMovieIMDB
from Bridges.data_src_dependent import Game
from Bridges.data_src_dependent import Shakespeare
from Bridges.data_src_dependent import GutenbergBook
from Bridges.data_src_dependent import CancerIncidence
from Bridges.data_src_dependent import Song
from Bridges import ColorGrid


##
#
# Get meta data of the IGN games collection.
#
# This function retrieves  and formats the data into a list of
# Game objects
#
# @throws Exception if the request fails
#
# @return a list of Game objects,
#
#
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


##
# Get ActorMovie IMDB Data
# retrieved, formatted into a list of ActorMovieIMDB objects
#
# @param number the number of actor/movie pairs, but currently unused,
# 	returns all records.
# @throws Exception if the request fails
#
# @return a list of ActorMovieIMDB objects, but only actor and
# movie fields in this version
#
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

##
# Get USGS earthquake data
# USGS Tweet data (https://earthquake.usgs.gov/earthquakes/map/)
# retrieved, formatted into a list of EarthquakeUSGS objects
#
# @param number the number of earthquake records retrieved,
# 	limited to 5000
# @throws Exception if the request fails
#
# @return a list of earthquake records
#
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

##
#
# Get data of Shakespeare works (plays, poems)
#
# This function retrieves  and formats the data into a
#   a list of Shakespeare objects.
#
# Valid endpoints: 'poems','plays', <title>
# Valid queryParams: format{simple}
#
# @throws Exception if the request fails
#
# @param endpoint  can be either "plays" or "poems". If this is
# 		 		specified, then only these types of works are retrieved.
# @param textOnly  if this is set, then only the text is retrieved.
#
# @return an array of Shakespeare objects
#
#
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


##
#
# Get meta data of the Gutenberg book collection (1000 books)
# 		This function retrieves,  and formats the data into a list of
# GutenbergBook objects
#
# @throws Exception if the request fails
#
# @return a list of GutenbergBook objects,
#
#
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


##
# Retrieves the CDC dataset into a vector of records
# See CancerIncidence class for more information
#
#
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


##
#
# Get data of a particular songs (including lyrics) using the Genius API
# (https://docs.genius.com/), given the song title and artist name.
# Valid endpoints:  http://bridgesdata.herokuapp.com/api/songs/find/
# Valid queryParams: song title, artist name
#
# This function retrieves  and formats the data into a
# Song object. The song if not cached in the local DB is queried
# and added to the DB
#
# @throws Exception if the request fails
#
# @return a Song object,
#
#
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


##
#
# Get data of the songs (including lyrics) using the Genius API
# https://docs.genius.com/
# Valid endpoints:  https://bridgesdata.herokuapp.com/api/songs/
#
# This function retrieves  and formats the data into a list of
# Song objects. This version of the API retrieves all the cached
# songs in the local DB.
#
# @throws Exception if the request fails
#
# @return a list of Song objects,
#
# 
def getSongData():
    all_songs = []
    url = "http://bridgesdata.herokuapp.com/api/songs/"
    params = {"Accept: application/json"}

    r = requests.get(url=url, params=str(params))
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


def get_color_grid_from_assignment(server: str, user: str, assignment: int, subassignment: int = 0) -> ColorGrid:
    response = get_assignment(server, user, assignment, subassignment)

    try:
        from types import SimpleNamespace as Namespace
    except ImportError:
        # Python 2.x fallback
        from argparse import Namespace

    assignment_wrapper = json.loads(response, object_hook=lambda d: Namespace(**d))
    try:
        assignment_object = assignment_wrapper.assignmentJSON
    except AttributeError:
        raise RuntimeError("Malformed JSON: Unable to Parse")

    if len(assignment_object.data) is not 1:
        raise RuntimeError("Malformed JSON: data is malformed")

    data = assignment_object.data[0]
    print(data)
    if data.visual is not "ColorGrid":
        raise RuntimeError("Malformed ColorGrid JSON: not a ColorGrid")



def get_assignment(server: str, user: str, assignment: int, subassignment: int = 0) -> str:
    """
    This function obtains the JSON representation of a particular assignment as a string

    @:return str that is the JSON representation of the subassignment as stored by the Bridges server
    @:param str user: the name of the user who uploaded the assignment
    @:param int assignment: the ID of the assignment to get
    @:param int subassignment: the ID of the subassignment to get (default 0)
    """
    subassignment_fixed = f"0{subassignment}" if subassignment < 10 else subassignment
    url = f"{server}/assignmentJSON/{assignment}.{subassignment_fixed}/{user}"
    params = "Accept: application/json"

    request = requests.get(url, params)
    if request.ok:
        return request.content
    else:
        raise request.raise_for_status()


class DataSource:
    pass
