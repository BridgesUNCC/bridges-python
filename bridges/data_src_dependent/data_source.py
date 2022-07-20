import json
import requests
import pickle
import urllib.parse

from bridges.data_src_dependent.earthquake_usgs import *
from bridges.data_src_dependent import actor_movie_imdb
from bridges.data_src_dependent.game import *
from bridges.data_src_dependent.shakespeare import *
from bridges.data_src_dependent.gutenberg_book import *
from bridges.data_src_dependent.gutenberg_meta import *
from bridges.data_src_dependent.reddit import *
from bridges.data_src_dependent.cancer_incidence import *
from bridges.data_src_dependent.song import *
from bridges.data_src_dependent import lru_cache
from bridges.data_src_dependent.movie_actor_wiki_data import *
from bridges.data_src_dependent.city import *
from bridges.data_src_dependent.osm import *
from bridges.data_src_dependent.elevation import *
from bridges.data_src_dependent.amenity import *
from bridges.data_src_dependent.actor_movie_imdb import *
from bridges.color_grid import ColorGrid
from bridges.color import Color
from SPARQLWrapper import SPARQLWrapper, JSON


source_type = "live"

def set_source_type(t) -> None:
    global source_type
    if (t == "testing"):
        source_type = "testing"
    if (t == "local"):
        source_type = "local"
    if (t == "live"):
        source_type = "live"
    return

def _get_reddit_url():
    if source_type == "testing":
        return "http://bridges-data-server-reddit-t.bridgesuncc.org"
    elif source_type == "local":
        return "http://localhost:9999"
    else:
        return "http://bridges-data-server-reddit.bridgesuncc.org"

def _get_gutenberg_url():
    if source_type == "testing":
        return "http://bridges-data-server-gutenberg-t.bridgesuncc.org"
    elif source_type == "local":
        return "http://localhost:3000"
    return "http://bridges-data-server-gutenberg.bridgesuncc.org"

def _get_osm_baseurl():
    if source_type == "local":
        return "http://localhost:3000"
    return "http://bridges-data-server-osm.bridgesuncc.org"

def _get_elevation_url():
    if source_type == "local":
        return "http://localhost:3000"
    return "http://bridges-data-server-elevation.bridgesuncc.org"

def _get_amenity_url():
    if source_type == "local":
        return "http://localhost:3000"
    return "http://bridges-data-server-osm.bridgesuncc.org"

def get_game_data():
    """
    @brief Get meta data of the IGN games collection.

    This function retrieves  and formats the data into a list of
    Game objects

    @throws Exception if the request fails
    
    @return a list of Game objects,
    """

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


def get_us_cities_data(**kwargs) -> List[City]:
    """
    @brief retrieves a set of cities filtered by provided arguments
    Args:
        kwargs: can be one or more of the following:
        'city': city name
        'state': US state
        'timezone': cities within this timezone
        'min_pop': include cities larger than this number
        'max_pop': include cities smaller than this number
        'min_elev':  include cities larger than this  elevation 
        'max_elev': include cities smaller than this  elevation 
        'min_lat':  min latitude
        'min_long':  min longitude
        'max_lat':  max latitude
        'max_long': max longtude
        'limit':  number of cities to be included
    """

    wrapper = []

    url = "http://bridgesdata.herokuapp.com/api/us_cities"
    if len(kwargs) > 0:
        url = url + '?'
        if kwargs.get('state'):
            url = url + 'state=' + kwargs['state'] + '&'
        if kwargs.get('min_pop'):
            url = url + 'minPopulation=' + str(kwargs['min_pop']) + '&'
        if kwargs.get('max_pop'):
            url = url + 'maxPopulation=' + str(kwargs['max_pop']) + '&'
        if kwargs.get('min_lat'):
            url = url + 'minLat=' + str(kwargs['min_lat']) + '&'
            print('url(partial): ' + url)
        if kwargs.get('min_long'):
            url = url + 'minLong=' + str(kwargs['min_long']) + '&'
        if kwargs.get('max_lat'):
            url = url + 'maxLat=' + str(kwargs['max_lat']) + '&'
        if kwargs.get('max_long'):
            url = url + 'maxLong=' + str(kwargs['max_long']) + '&'
        if kwargs.get('min_elev'):
            url = url + 'minElevation=' + str(kwargs['min_elev']) + '&'
        if kwargs.get('max_elev'):
            url = url + 'maxElevation=' + str(kwargs['max_elev']) + '&'
        if kwargs.get('limit'):
            url = url + 'limit=' + str(kwargs['limit']) + '&'
        url = url[:-1]  # remove last &

    print(url)
    PARAMS = {"Accept: application/json"}

    r = requests.get(url=url, params=str(PARAMS))

    r = r.json()

    D = r["data"]

    for i in range(len(D)):
        V = D[i]
        wrapper.append(City(city = V['city'], state=V['state'], country = V['country'], lat = V['lat'], lon=V['lon'], elevation=V['elevation'],
                                          population = V['population'], timezone=V['timezone']))
    return wrapper

def get_world_cities_data(**kwargs) -> List[City]:
    wrapper = []

    url = "http://localhost:3001/api/world_cities"
    # url = "http://bridgesdata.herokuapp.com/api/world_cities"
    if len(kwargs) > 0:
        url = url + '?'
        if kwargs.get('state'):
            url = url + 'state=' + kwargs['state'] + '&'
        if kwargs.get('min_pop'):
            url = url + 'minPopulation=' + str(kwargs['min_pop']) + '&'
        if kwargs.get('maxpop'):
            url = url + 'maxPopulation=' + str(kwargs['max_pop']) + '&'
        if kwargs.get('min_lat_long'):
            url = url + 'minLatLong=' + str(kwargs['minll'][0]) + ',' + str(kwargs['minll'][1]) + '&'
        if kwargs.get('max_lat_long'):
            url = url + 'maxLatLong=' + str(kwargs['maxll'][0]) + ',' + str(kwargs['maxll'][1]) + '&'
        if kwargs.get('min_elev'):
            url = url + 'minElevation=' + str(kwargs['min_elev']) + '&'
        if kwargs.get('max_elev'):
            url = url + 'maxElevation=' + str(kwargs['max_elev']) + '&'
        if kwargs.get('limit'):
            url = url + 'limit=' + str(kwargs['limit']) + '&'
        url = url[:-1]  # remove last &

    print(url)
    PARAMS = {"Accept: application/json"}

    r = requests.get(url=url, params=str(PARAMS))

    r = r.json()

    D = r["data"]

    for i in range(len(D)):
        V = D[i]
        wrapper.append(USCities(city = V['city'], state=V['state'], country = V['country'], lat = V['lat'], lon=V['lon'], elevation=V['elevation'],
                                          population = V['population'], timezone=V['timezone']))
    return wrapper




def _parse_actor_movie_imdb(item) -> ActorMovieIMDB:
    """
    @brief Parses an actor movie pair

    Args:
        item: input actor-movie pair
    """
    am_pair = ActorMovieIMDB()
    am_pair.actor = item["actor"]
    am_pair.movie = item["movie"]
    return am_pair


def get_actor_movie_imdb_data(count = 0) -> ActorMovieIMDB:
    """
    @brief Get ActorMovie IMDB Data. 

    Data is retrieved, formatted into a list of ActorMovieIMDB objects

    Args:
        count: count of the number of actor/movie pairs, but currently unused,
        returns all records.

    Returns:
        a list of ActorMovieIMDB objects, but only actor and movie fields in this version
    @throws Exception if the request fails
    """

    wrapper = []

    url = "http://bridgesdata.herokuapp.com/api/imdb?limit=" + str(count)
    PARAMS = {"Accept: application/json"}

    r = requests.get(url=url, params=str(PARAMS))
    # print(r.status_code, r.reason)

    data = r.json()

    D = data["data"]

    for i in range(len(D)):
        V = D[i]
        wrapper.append(ActorMovieIMDB(V["actor"], V["movie"]))

    return wrapper

def get_actor_movie_imdb_data2() -> ActorMovieIMDB:
    """
    Get ActorMovie IMDB Data. Data is retrieved, formatted into a list of ActorMovieIMDB objects

    Args:
        count: the number of actor/movie pairs, but currently unused,

    Returns:
        All records.

    Throws: 
        Exception if the request fails
    """
    url = "https://bridgesdata.herokuapp.com/api/imdb2"

    r = requests.get(url = url)
    status = r.status_code

    data = r.json()
    D = data["data"]
    am_list = []

    if status == 200:
        for i in range(len(D)):
            V = D[i]
            am_pair = _parse_actor_movie_imdb(V)
            am_pair.rating = int(V['rating'])

            genre = V['genres']
            v = []
            for k in range(len(genre)):
                v.append(genre[k])
            am_pair._genres = v
            am_list.append(am_pair)
        return am_list
    else:
        r.raise_for_status()


def get_earthquake_usgs_data(count = 0) -> EarthquakeUSGS:
    """
    @brief Get USGS earthquake data

    USGS Tweet data (https://earthquake.usgs.gov/earthquakes/map/). Data
    retrieved, formatted into a list of EarthquakeUSGS objects

    Args:
        count: the number of earthquake records retrieved

    @throws Exception if the request fails

    Returns:
        a list of earthquake records
    """
    wrapper = []
    url = "http://earthquakes-uncc.herokuapp.com/eq"
    latest_url = "http://earthquakes-uncc.herokuapp.com/eq/latest/" + str(count)
    PARAMS = {"Accept: application/json"}

    if count <= 0:
        r = requests.get(url=url, params=str(PARAMS))
        r = r.json()
        for i in range(len(r)):
            V = r[i]["properties"]
            G = r[i]["geometry"]["coordinates"]
            wrapper.append(EarthquakeUSGS(V["mag"], G[0], G[1], V["place"], V["title"], V["url"], V["time"]))
    else:
        r = requests.get(url=latest_url, params=str(PARAMS))
        data = r.json()
        D = data["Earthquakes"]
        for i in range(len(D)):
            V = D[i]["properties"]
            G = D[i]["geometry"]["coordinates"]
            wrapper.append(EarthquakeUSGS(V["mag"], G[0], G[1], V["place"], V["title"], V["url"], V["time"]))
    return wrapper


def get_shakespeare_data(endpoint = "", textonly = False) -> Shakespeare:
    """
    @brief Get data of Shakespeare works (plays, poems)

    This function retrieves  and formats the data into a
    a list of Shakespeare objects.

    Valid endpoints: 'poems','plays'
    Valid queryParams: format{simple}

    @throws Exception if the request fails

    Args: 
        endpoint:  can be either "plays" or "poems". If this is
            specified, then only these types of works are retrieved.
        textonly:  if this is set, then only the text is retrieved.

    Returns:
        An array of Shakespeare objects
    """

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
        wrapper.append(Shakespeare(V["title"], V["type"], V["text"]))
    return wrapper


def get_gutenberg_book_data(num = 0) -> GutenbergBook:

    """
    @brief Get meta data of the Gutenberg book collection (1000 books)

    This function retrieves,  and formats the data into a list of
    GutenbergBook objects

    (deprecated you may want to use get_gutenberg_book_metadata() instead. )

    @throws Exception if the request fails

    Returns:
        A list of GutenbergBook objects,
    """
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


def get_cancer_incident_data(num = 0) -> CancerIncidence:
    """
    @brief Retrieves the CDC cancer incidence dataset.

    Returns a list of records.  See CancerIncidence class for more information

    Args:
        num:  count of records to be retrieved
    Returns:
         cancer incidence data records in a list
    """
    wrapper = []
    url = "https://bridgesdata.herokuapp.com/api/cancer/withlocations"
    PARAMS = {"Accept: application/json"}

    if num > 0:
        url += "?limit="+str(num)

    r = requests.get(url=url, params=str(PARAMS))
    r = r.json()

    D = r["data"]

    for i in range(len(D)):
        c = CancerIncidence()
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


def get_song(songTitle, artistName = None) -> Song:
    """
    @brief Get data of a particular song (including lyrics) using the Genius API.

    Data from Genius API(https://docs.genius.com/), given the song title and artist name.
    Valid endpoints:  http://bridgesdata.herokuapp.com/api/songs/find/
    Valid queryParams: song title, artist name

    This function retrieves  and formats the data into a
    Song object. The song if not cached in the local DB is queried
    and added to the DB

    Args:
        songTitle: title of song
        artistName: name of artist

    @throws Exception if the request fails

    Returns:
         a Song object,
    """
    wrapper = []
    url = "http://bridgesdata.herokuapp.com/api/songs/find/"
    PARAMS = {"Accept: application/json"}

    if len(songTitle):
        url = url + urllib.parse.quote(songTitle)

    if artistName is not None:
        if len(artistName):
            url += "?artistName=" + urllib.parse.quote(artistName)

    r = requests.get(url = url, params = str(PARAMS))
    if r.status_code != 200:
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

    return Song(artist, songs, album, lyrics, release_date)


def get_song_data() -> List[Song]:
    """

    Get data of the songs (including lyrics) using the Genius API.

    Song data from https://docs.genius.com/.
    Valid endpoints:  https://bridgesdata.herokuapp.com/api/songs/

    This function retrieves  and formats the data into a list of
    Song objects. This version of the API retrieves all the cached
    songs in the local DB.

    @throws Exception if the request fails

    Returns:
         A list of Song objects,
    """
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

        all_songs.append(Song(artist, song, album, lyrics, release_date))
    return all_songs


def get_color_grid_from_assignment(server: str, user: str, assignment: int, subassignment: int = 0) -> ColorGrid:
    """
    @brief Reconstruct a ColorGrid from an existing ColorGrid on the bridges server

    This method can be useful in early CS courses like CS1 or CS2  to 
    work with an existing data structure holding a dataset, like an image.

    Args:
        server:  server holding the assignment
        user:  user name
        assignment:  assignment number
        subassignment:  sub-assignment number

    Returns:
        ColorGrid structure
    """

    response = _get_assignment(server, user, assignment, subassignment)

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
        if len(data_list) != 1:
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
        dim_x = int(data.dimensions[0])
        dim_y = int(data.dimensions[1])

        try:
            node_string = str(data.nodes)
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


def _get_assignment(server: str, user: str, assignment: int, subassignment: int = 0) -> str:
    """
    @brief This method retrieves a stored assignment from the server.

    It is unlikely a student would eve want to use this directly

    Args:
        server:  server holding the assignment
        user: the name of the user who uploaded the assignment
        assignment:  assignment number
        subassignment:  sub-assignment number

    Returns:
        data structure representation of the assignment as a JSON string
    """
    subassignment_fixed = "0{}".format(subassignment) if subassignment < 10 else subassignment
    url = "{}/assignmentJSON/{}.{}/{}".format(server, assignment, subassignment_fixed, user)
    params = "Accept: application/json"

    request = requests.get(url, params)
    if request.ok:
        return request.content
    else:
        raise request.raise_for_status()


def _osm_server_request(url):
    """
    @brief Fulfills a server request for OpenStreetMap

    For internal use only

    Args:
        url: url for server to process

    """
    request = requests.get(url)
    if not request.ok:
        if request.status_code == 404:
            request = requests.get(url)
            if not request.ok:
                raise request.raise_for_status()
            raise RuntimeError("Location: {} is not supported,\n valid names: {}".format(location, valid_names))
        raise request.raise_for_status()

    server_data = request.content

    return server_data


def get_osm_data(*args) -> OsmData:
    """
    @brief This method retrieves an OpenStreet Map dataset given a location.
    
    The function can either take a city name or a bounding box in lat/long. The city name can be taken from the list at http://bridges-data-server-osm.bridgesuncc.org/cities

    The function also take a level of detail which can be anything in ["motorway", "trunk", "primary", "secondary", "tertiary, "unclassified", "residential", "living_street", "service", "trails", "walking", "bicycle" ]


    Args:
        locname: name of a city (str)
        level:  level of detail (str)

    Args alternatively:
         minLat: minimum latitude of the bounding box (float)
         minLon: minimum longitude of the bounding box (float)
         maxLat: maximum latitude of the bounding box (float)
         maxLon: maximum longitude of the bounding box (float)
         level: level of detail (str)

    Returns:
        OsmData
    """
    import os

    debug = True

    if (len(args) == 2):
        location = args[0]
        level = args[1]
        url = _get_osm_baseurl()+"/loc?location=" + urllib.parse.quote(location) + "&level=" + urllib.parse.quote(level)
        hash_url = _get_osm_baseurl()+"/hash?location=" + urllib.parse.quote(location) + "&level=" + urllib.parse.quote(level)
    elif (len(args) == 5):
        minLat = str(args[0])
        minLon = str(args[1])
        maxLat = str(args[2])
        maxLon = str(args[3])
        level = args[4]
        url = _get_osm_baseurl()+"/coords?minLon=" + minLon + "&minLat=" + minLat + "&maxLon=" + maxLon + "&maxLat=" + maxLat + "&level=" + level
        hash_url = _get_osm_baseurl()+"/hash?minLon=" + minLon + "&minLat=" + minLat + "&maxLon=" + maxLon + "&maxLat=" + maxLat + "&level=" + level
    else:
        raise RuntimeError("Invalid Map Request Inputs")

    lru = lru_cache.lru_cache(30)

    if debug:
        print ("url: "+url)
        print ("hash_url: "+hash_url)

    try:
        from types import SimpleNamespace as Namespace
    except ImportError:
        from argparse import Namespace


    data = None
    not_skip = True
    hash = _osm_server_request(hash_url).decode('utf-8')
    if (hash != "false" and lru.inCache(hash)):
        not_skip = False
        data = lru.get(hash)

    if not_skip:
        content = _osm_server_request(url)
        try:
            data = json.loads(content.decode('utf-8'), object_hook=lambda d: Namespace(**d))
        except:
            print("Error: Corrupted JSON download...\nAttempting redownload...")
            content = _osm_server_request(url)
            try:
                data = json.loads(content.decode('utf-8'), object_hook=lambda d: Namespace(**d))
            except Exception as e:
                print(f"Error: Redownload attempt failed\n{e}")
                sys.exit(0)

        hash = _osm_server_request(hash_url).decode('utf-8')
        lru.put(hash, data)


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

def _server_request(url):
    """
    @brief Fulfills a server request
    
    For internal use only
    """
    request = requests.get(url)
    if not request.ok:
        if request.status_code == 404:
            request = requests.get(url)
            if not request.ok:
                raise request.raise_for_status()
            raise RuntimeError("404 issue with server request")
        elif request.status_code == 504:
            request = requests.get(url)
            if not request.ok:
                raise request.raise_for_status()
            raise RuntimeError(f"504 issue with server request: {request.raise_for_status}")
        raise request.raise_for_status()

    server_data = request.content

    return server_data

def get_elevation_data(*args) -> ElevationData:
    """
    @brief This method retrieves an Elevation  Map dataset, given a location by name (string).

    Args:
        args(0): a bounding box, aka an array [minLat, minLon, maxLat, maxLon]
        args(1): spatial resolution, aka the distance between two samples (in degrees)

    Returns:
        Elevation data for the bounding box and resolution requested  (approximately) [type: ElevationData]
    """
    base_url = _get_elevation_url() + "/elevation"
    hash_url = _get_elevation_url() + "/hash"

    coords = args[0]
    minLat = str(coords[0])
    minLon = str(coords[1])
    maxLat = str(coords[2])
    maxLon = str(coords[3])

    res = .0166
        
    if len(args) == 2:
        res = args[1]
        
    url = base_url + f"?minLat={minLat}&minLon={minLon}&maxLat={maxLat}&maxLon={maxLon}&resX={res}&resY={res}"
    hash_url = hash_url + f"?minLat={minLat}&minLon={minLon}&maxLat={maxLat}&maxLon={maxLon}&resX={res}&resY={res}"
    #loads cache
    lru = lru_cache.lru_cache(30)

    data = None
    not_skip = True
    hash = False
    hash = _server_request(hash_url).decode('utf-8')
    if (hash != "false" and lru.inCache(hash)):
        not_skip = False
        data = lru.get(hash)

    if not_skip:
        data = _server_request(url).decode("utf-8")

    hash = _server_request(hash_url).decode('utf-8')
    lru.put(hash, data)

    
    #parse and build object
    ret_ele = ElevationData()
    
    file_array = data.splitlines()
    ret_ele.cols = int(file_array[0].split(" ")[-1])
    ret_ele.rows = int(file_array[1].split(" ")[-1])
    ret_ele._xll = float(file_array[2].split(" ")[-1])
    ret_ele._yll = float(file_array[3].split(" ")[-1])
    ret_ele.cellsize = float(file_array[4].split(" ")[-1])

    maxVal = float('-inf')
    minVal = float('inf')
    x = 5
    while (x < len(file_array)):
        arr = file_array[x].replace("\n", "").split(" ")
        arr.pop(0)
        parsedline = []
        for y in arr:
            parsedline.append(int(y))
            if(int(y) > maxVal):
                maxVal = int(y)
            if(int(y) < minVal):
                minVal = int(y)
        ret_ele.data.append(parsedline)
        x += 1
    ret_ele.maxVal = maxVal
    ret_ele.minVal = minVal    

    return ret_ele

def _get_wiki_actor_movie_direct(year_begin, year_end, array_out):
    """
    @brief get actor movie data from wiki data
    Args:
        year_begin: beginning year of data
        year_end: ending year of data.
        array_out: returned data in an array
    """
    # allocate cache - this makes no sense
    lru = lru_cache.lru_cache(30)

    # check cache code name and check cache
    code_name = "wikidata-actormovie-" + str(year_begin) + "-" + str(year_end)
    print(code_name)
    from_cache = False
    if lru.inCache(code_name):  
        results = lru.get(code_name)
        from_cache = True
    else:
        sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
        sparql.setQuery("""
            SELECT ?movie ?movieLabel ?actor ?actorLabel WHERE \
            {\
                ?movie wdt:P31 wd:Q11424.\
                ?movie wdt:P161 ?actor.\
                ?movie wdt:P364 wd:Q1860.\
                ?movie wdt:P577 ?date.\
                FILTER(YEAR(?date) >= """ + str(year_begin) + """ && YEAR(?date) <= """ + str(year_end) + """).\
                SERVICE wikibase:label { bd:serviceParam wikibase:language \"en\". } \
            }
        """)
        sparql.addCustomHttpHeader("User-Agent", 'bridges-python')
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()
        lru.put(code_name, results)

    for result in results["results"]["bindings"]:
        mak = MovieActorWikiData()
        actor_uri = str(result['actor']['value'])
        movie_uri = str(result['movie']['value'])
        actor_uri = actor_uri.replace("http://www.wikidata.org/entity/","",1)
        movie_uri = movie_uri.replace("http://www.wikidata.org/entity/","",1)
        mak.actor_uri = actor_uri
        mak.movie_uri = movie_uri
        mak.movie_name = str(result['movieLabel']['value'])
        mak.actor_name = str(result['actorLabel']['value'])
        array_out.append(mak)
        # print(result['movie']['value'])

def get_wiki_data_actor_movie(year_begin, year_end) -> List[MovieActorWikiData]:
    """
    @brief This method retrieves an actor-movie data from Wikidata

    Uses a sparql query

    Args:
        year_begin:  beginning year of data request
        year_end:    ending year of data request

    Returns:
        A list of the actor-movie data of type MovieActorWikiData
    """
    ret = []
    for y in range(year_begin, year_end+1):
        _get_wiki_actor_movie_direct(y, y, ret)
    return ret

def get_amenity_data(*args) -> List[Amenity] :
    """
    @brief This method retrieves amenity data from Open Street Map datasets.
    
    Valid types are "food", "school", "firestation", "airport", "heli"

    Args:
         minLat: minimum latitude of the bounding box (float)
         minLon: minimum longitude of the bounding box (float)
         maxLat: maximum latitude of the bounding box (float)
         maxLon: maximum longitude of the bounding box (float)
         type: amenity type (str)

    Args alternatively:
        locname: name of a city (str)
        type:  amenity type (str)


    Returns:
        A list of amenities
    """
    if(len(args)) == 5:
        url = f"{_get_amenity_url()}/amenity?minLat={args[0]}&minLon={args[1]}&maxLat={args[2]}&maxLon={args[3]}&amenity={args[4]}"
        hash_url = f"{_get_amenity_url()}/hash?minLat={args[0]}&minLon={args[1]}&maxLat={args[2]}&maxLon={args[3]}&amenity={urllib.parse.quote(args[4])}"
    elif(len(args) == 2):
        url = f"{_get_amenity_url()}/amenity?location={urllib.parse.quote(args[0])}&amenity={urllib.parse.quote(args[1])}"
        hash_url = f"{_get_amenity_url()}/hash?location={args[0]}&amenity={args[1]}"
    else:
        raise RuntimeError("Invalid Number of Map Request Inputs")

    lru = lru_cache.lru_cache(30)
    data = None
    not_skip = True

    hash = _osm_server_request(hash_url).decode('utf-8')
    if (hash != "false" and lru.inCache(hash)):
        not_skip = False
        data = lru.get(hash)
    
    if (not_skip):
        content =  _osm_server_request(url)
        try:
            data = json.loads(content.decode('utf-8'))
        except:
            print("Error: Corrupted JSON download...\nAttempting redownload...")
            content = _osm_server_request(url)
            try:
                data = json.loads(content.decode('utf-8'))
            except Exception as e:
                print(f"Error: Redownload attempt failed\n{e}")
                raise RuntimeError(e)
                sys.exit(0)

        hash = _osm_server_request(hash_url).decode('utf-8')
        lru.put(hash, data)


    ret_data = []

    for i, node in enumerate(data['nodes']):
        amen = Amenity()
        for x, vals in enumerate(node):
            if (x == 0):
                amen.id = vals
            elif (x == 1):
                amen.lat = vals
            elif (x == 2):
                amen.lon = vals
            elif (x == 3):
                amen.name = vals
            else:
                amen.addOther = vals
        ret_data.append(amen)
    

    return ret_data

#def get_gutenberg_book_metadata(*args) -> list[GutenbergMeta]:
def get_gutenberg_book_metadata(*args) -> GutenbergMeta:
    """
    @brief function to search for a gutenberg book given a search string and type of metadata to search through

    :param args:
        args[0]: search string, i.e home
        args[1]: metadata type, i.e id, title, lang, date_added, authors, genres, loc_class

    :return: a list of books with containing matched strings from the specified metadata type
    """
    url = _get_gutenberg_url() + f"/search?search={args[0]}&type={args[1]}"

    content = _server_request(url)
    data = json.loads(content.decode('utf-8'))

    book_list = []
    for node in data['book_list']:
        meta = GutenbergMeta ()

        meta.id = node["id"]
        meta.title = node['title']
        meta.lang = node["lang"]
        meta.date = node["date_added"]
        meta.authors = node["authors"]
        meta.genres = node["genres"]
        meta.loc = node["loc_class"]

        book_list.append(meta)

    return book_list

def get_a_gutenberg_book_metadata(id) -> GutenbergMeta:
    """
    @brief function to retrieve the metadata of a gutenberg book given its ID
    :param id: ID of the book
    :return: a dictionary containing the metadata of the gutenberg book
    """
    url = _get_gutenberg_url() + "/meta?id=" + str(id)

    content = _server_request(url)
    data = json.loads(content.decode('utf-8'))

    meta = GutenbergMeta()
    for node in data['book_list']:
        
        
        meta.id = node["id"]
        meta.title = node['title']
        meta.lang = node["lang"]
        meta.date = node["date_added"]
        meta.authors = node["authors"]
        meta.genres = node["genres"]
        meta.loc = node["loc_class"]

    return meta

def gutenberg_book_text(id, strip = False):
    """
    @brief function to retrieve the text of a gutenberg book given the ID
    :param id: id of the book
    :param strip: boolean to determine if headers and footers are stripped from the text
    :return: json containing the text of the book
    """
    url = _get_gutenberg_url() + "/book?id=" + str(id)
    
    lru = lru_cache.lru_cache(120)
    try:
        if (lru.inCache("gutenberg" + str(id))):
            if source_type == "local" or source_type == "testing":
                print(f"Using cache to request {id}")
            data = lru.get("gutenberg" + str(id))
        else:
            if source_type == "local" or source_type == "testing":
                print(f"Using {source_type} server to request {id}")
            content = _server_request(url)
            data = content.decode('utf-8')
            lru.put("gutenberg" + str(id), data)
    except Exception as e:
        print(e)
        raise RuntimeError(e)

    book_data = json.loads(data)

    return book_data[str(id)]

def available_subreddits() -> List[str]:
    """
    @brief retrieves the subreddits made available by BRIDGES
    :return: a list of strings which identify subreddits
    """
    base_url = _get_reddit_url()
    url = f"{base_url}/listJSON"
    content = _server_request(url)
    return json.loads(content.decode("utf-8"))

def reddit_data(subreddit, time_request = -9999) -> Reddit:
    """
    @brief  retrieves the reddit post from a subreddit
    :param subreddit: the name of the subreddit ( check list available at http://bridges-data-server-reddit.bridgesuncc.org/list ) 
    :param time_request: unix timestamp of when requested subreddit was generated or less than 0 for now
    :return: a list of reddit objects with the data of the posts
    """
    base_url = _get_reddit_url()
    url = f"{base_url}/cache?subreddit={subreddit}&time_resquest={time_request}"


    content = _server_request(url)
    print ("Object type:" + str(type(content)))
    print("reddit content:" + str(content))
    data = json.loads(content.decode("utf-8"))

    reddit_posts = []

    for n in data:
        post = Reddit()
        post.id = data[n]["id"]
        post.title = data[n]["title"]
        post.author = data[n]["author"]
        post.score = int(data[n]["score"])
        post.vote_ratio = float(data[n]["vote_ratio"])
        post.comment_count = int(data[n]["comment_count"])
        post.subreddit = data[n]["subreddit"]
        post.post_time = int(data[n]["post_time"])
        post.url = data[n]["url"]
        post.text = data[n]["text"]

        reddit_posts.append(post)

    return reddit_posts



class DataSource:
    pass
