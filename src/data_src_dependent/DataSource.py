import json
import requests
from data_src_dependent import ActorMovieIMDB


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


class DataSource:
    pass






