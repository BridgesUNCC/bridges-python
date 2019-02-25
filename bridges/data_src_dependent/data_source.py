import json
import requests
from bridges.data_src_dependent import earthquake_usgs
from bridges.data_src_dependent import actor_movie_imdb
from bridges.data_src_dependent import game
from bridges.data_src_dependent import shakespeare
from bridges.data_src_dependent import gutenberg_book
from bridges.data_src_dependent import cancer_incidence
from bridges.data_src_dependent import song
from bridges.data_src_dependent.osm import *
from bridges.data_src_dependent.actor_movie_imdb import *
from bridges.color_grid import ColorGrid
from bridges.color import Color


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
def get_game_data():

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
        wrapper.append(game.Game(V["game"], V["platform"], V["rating"], str(genre)))
    return wrapper


def parse_actor_movie_imdb(item):
    am_pair = ActorMovieIMDB()
    am_pair.set_actor(item["actor"])
    am_pair.set_movie(item["movie"])
    return am_pair


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
def get_actor_movie_imdb_data(number = 0):

    wrapper = []

    url = "http://bridgesdata.herokuapp.com/api/imdb?limit=" + str(number)
    PARAMS = {"Accept: application/json"}

    r = requests.get(url=url, params=str(PARAMS))
    # print(r.status_code, r.reason)

    data = r.json()

    D = data["data"]

    for i in range(len(D)):
        V = D[i]
        wrapper.append(actor_movie_imdb.ActorMovieIMDB(V["actor"], V["movie"]))

    return wrapper

def get_actor_movie_imdb_data2():

    url = "https://bridgesdata.herokuapp.com/api/imdb2"

    r = requests.get(url = url)
    status = r.status_code

    data = r.json()
    D = data["data"]
    am_list = []

    if status == 200:
        for i in range(len(D)):
            V = D[i]
            am_pair = parse_actor_movie_imdb(V)
            am_pair.set_rating(int(V['rating']))

            genre = V['genres']
            v = []
            for k in range(len(genre)):
                v.append(genre[k])
            am_pair.set_genres(v)
            am_list.append(am_pair)
        return am_list
    else:
        r.raise_for_status()





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
def get_earthquake_usgs_data(number = 0):

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
            wrapper.append(earthquake_usgs.EarthquakeUSGS(V["mag"], G[0], G[1], V["place"], V["title"], V["url"], V["time"]))
    else:
        r = requests.get(url=latest_url, params=str(PARAMS))
        data = r.json()
        D = data["Earthquakes"]
        for i in range(len(D)):
            V = D[i]["properties"]
            G = D[i]["geometry"]["coordinates"]
            wrapper.append(earthquake_usgs.EarthquakeUSGS(V["mag"], G[0], G[1], V["place"], V["title"], V["url"], V["time"]))
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
def get_shakespeare_data(endpoint = "", textonly = False):
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
        wrapper.append(shakespeare.Shakespeare(V["title"], V["type"], V["text"]))
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
def get_gutenberg_book_data(num = 0):
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
        wrapper.append(gutenberg_book.GutenbergBook(A["name"], A["birth"], A["death"], V["title"],
                                                    str(lang), str(genre), str(subject), M["characters"], M["words"],
                                                    M["sentences"], M["difficultWords"], V["url"], V["downloads"]))

    return wrapper


##
# Retrieves the CDC dataset into a vector of records
# See CancerIncidence class for more information
#
#
def get_cancer_incident_data(num = 0):

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
        c = cancer_incidence.CancerIncidence()
        v = D[i]
        age = v["Age"]
        c.set_age_adjusted_rate(age["Age Adjusted Rate"])
        c.set_age_adjusted_ci_lower(age["Age Adjusted CI Lower"])
        c.set_age_adjusted_ci_upper(age["Age Adjusted CI Upper"])
        c.set_year(v["Year"])

        data = v["Data"]

        c.set_crude_rate(data["Crude Rate"])
        c.set_crude_rate_ci_lower(data["Crude CI Lower"])
        c.set_crude_rate_ci_upper(data["Crude CI Upper"])
        c.set_race(data["Race"])
        c.set_population(data["Population"])
        c.set_event_type(data["Event Type"])
        c.set_affected_area(v["Area"])

        loc = v["loc"]

        c.set_location_x(loc[0])
        c.set_location_y(loc[1])

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
def get_song(songTitle, artistName = None):
    wrapper = []
    url = "http://bridgesdata.herokuapp.com/api/songs/find/"
    PARAMS = {"Accept: application/json"}

    if len(songTitle):
        url = url + songTitle

    if artistName is not None:
        if len(artistName):
            url += "?artistName=" + artistName

    url.replace(" ", "%20")

    r = requests.get(url = url, params = str(PARAMS))
    if r.status_code is not 200:
        raise ConnectionError("HTTP Request Failed. Error Code: " + r.status_code)
    r = r.json()
    if "artist" in r:
        artist = r["artist"]
    else:
        artist = ""
    if "song" in r:
        songs = r["song"]
    else:
        songs = ""
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

    return song.Song(artist, songs, album, lyrics, release_date)


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
def get_song_data():
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

        all_songs.append(song.Song(artist, song, album, lyrics, release_date))
    return all_songs


def get_color_grid_from_assignment(server: str, user: str, assignment: int, subassignment: int = 0) -> ColorGrid:
    """
    Reconstruct a ColorGrid from an existing ColorGrid on the bridges server

    :param str server: internal server url of bridges object
    :param str user: the name of the user who uploaded the assignment
    :param int assignment: the ID of the assignment to get
    :param int subassignment: the ID of the subassignment to get (default 0)
    :return: ColorGrid: the ColorGrid stored in the bridges server
    """
    response = get_assignment(server, user, assignment, subassignment)

    try:
        from types import SimpleNamespace as Namespace
    except ImportError:
        # Python 2.x fallback
        from argparse import Namespace

    assignment_object = json.loads(response, object_hook=lambda d: Namespace(**d))
    try:
        if assignment_object.assignment_type != "ColorGrid":
            raise RuntimeError("Malformed ColorGrid JSON: not a ColorGrid")

        data_list = assignment_object.data
        if len(data_list) is not 1:
            raise RuntimeError("Malformed JSON: data is malformed")
        data = data_list[0]
        try:
            encoding = data.encoding
        except AttributeError:
            # Handle case for ColorGrid generated before encoding field was added
            encoding = "RAW"

        if encoding != "RLE" and encoding != "RAW":
            raise RuntimeError("Malformed ColorGrid JSON: encoding not supported: " + encoding)

        if len(data.dimensions) != 2:
            raise RuntimeError("Malformed ColorGrid JSON: dimensions are malformed")
        dim_x = data.dimensions[0]
        dim_y = data.dimensions[1]

        if len(data.nodes) != 1:
            raise RuntimeError("Malformed ColorGrid JSON: nodes are malformed")

        try:
            node_string = str(data.nodes[0])
        except (TypeError, ValueError):
            raise RuntimeError("Malformed ColorGrid JSON: node is not a String")

        import base64
        decoded_bytes = bytearray(base64.b64decode(node_string))
        decoded = [int(x) for x in decoded_bytes]
    except AttributeError:
        raise RuntimeError("Malformed JSON: Unable to Parse. Does this assignment exist?")

    color_grid = ColorGrid(dim_x, dim_y)

    if encoding == "RAW":
        if len(decoded) != dim_x * dim_y * 4:
            raise RuntimeError("Malformed ColorGrid JSON: nodes is not the size we expect for RAW encoding")

        base = 0
        for x in range(0, dim_x):
            for y in range(0, dim_y):
                color = Color(decoded[base],
                              decoded[base + 1],
                              decoded[base + 2],
                              (decoded[base + 3]/255.0)
                              )
                color_grid.set(x, y, color)
                base = base + 4

    elif encoding == "RLE":
        if len(decoded) % 5:
            raise RuntimeError("Malformed ColorGrid JSON: RLE nodes are not a multiple of 5")
        current_in_decoded = 0
        current_in_cg = 0
        while current_in_decoded != len(decoded):
            repeat = decoded[current_in_decoded]

            color = Color(decoded[current_in_decoded + 1],
                          decoded[current_in_decoded + 2],
                          decoded[current_in_decoded + 3],
                          (decoded[current_in_decoded + 4] / 255.0)
                          )
            current_in_decoded = current_in_decoded + 5

            while repeat >= 0:
                pos_x = int(current_in_cg / dim_y)
                pos_y = int(current_in_cg % dim_y)
                if pos_x >= dim_x or pos_y >= dim_y:
                    raise RuntimeError("Malformed ColorGrid JSON: Too much data in nodes")

                color_grid.set(pos_x, pos_y, color)
                current_in_cg = current_in_cg + 1
                repeat = repeat - 1

    return color_grid


def get_assignment(server: str, user: str, assignment: int, subassignment: int = 0) -> str:
    """
    This function obtains the JSON representation of a particular assignment as a string

    :param str server: internal server url of bridges object
    :param str user: the name of the user who uploaded the assignment
    :param int assignment: the ID of the assignment to get
    :param int subassignment: the ID of the subassignment to get (default 0)
    :return str that is the JSON representation of the subassignment as stored by the bridges server
    """
    subassignment_fixed = "0{}".format(subassignment) if subassignment < 10 else subassignment
    url = "{}/assignmentJSON/{}.{}/{}".format(server, assignment, subassignment_fixed, user)
    params = "Accept: application/json"

    request = requests.get(url, params)
    if request.ok:
        return request.content
    else:
        raise request.raise_for_status()


def get_osm_data(location: str) -> OsmData:
    """Takes a location name as a string and returns an OsmData object
    :param location: str, name of location
    :return: OsmData:
    """
    import os
    try:
        from types import SimpleNamespace as Namespace
    except ImportError:
        from argparse import Namespace

    if not os.path.isdir("./bridges_data_cache"):
        os.mkdir("./bridges_data_cache")

    data = None
    for f in os.listdir("./bridges_data_cache"):
        if f == location.lower() + ".json":
            with open("./bridges_data_cache/" + f, "r") as j:
                data = json.load(j, object_hook=lambda d: Namespace(**d))

    if data is None:
        url = "https://osm-api.herokuapp.com/name/" + location
        params = "Accept: application/json"

        request = requests.get(url, params)
        if not request.ok:
            if request.status_code == 404:
                url = "https://osm-api.herokuapp.com/name_list"
                params = "Accept: application/json"
                request = requests.get(url, params)
                if not request.ok:
                    raise request.raise_for_status()
                data = json.loads(request.content)
                valid_names = data['names']
                raise RuntimeError("Location: {} is not supported,\n valid names: {}".format(location, valid_names))
            raise request.raise_for_status()

        content = request.content
        data = json.loads(content.decode('utf-8'), object_hook=lambda d: Namespace(**d))
        with open("./bridges_data_cache/{}.json".format(location.lower()), "w") as f:
            # write to file in cache
            json.dump(json.loads(content.decode('utf-8')), f)

    try:
        if data.nodes is None or data.edges is None or data.meta is None:
            raise RuntimeError("Malformed OSM JSON")

        vertex_map = {}
        vertices = []
        for i, node in enumerate(data.nodes):
            vertex_map[node[0]] = i
            vertices.append(OsmVertex(node[1], node[2]))

        edges = []
        for edge in data.edges:
            id_from = edge[0]
            id_to = edge[1]
            dist = edge[2]
            edges.append(OsmEdge(vertex_map[id_from], vertex_map[id_to], dist))

        ret_osm = OsmData()
        ret_osm.edges = edges
        ret_osm.vertices = vertices
        ret_osm.name = data.meta.name
        return ret_osm

    except AttributeError:
        raise RuntimeError("Malformed JSON: Unable to parse")


class DataSource:
    pass
