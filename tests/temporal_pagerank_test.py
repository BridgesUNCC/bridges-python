from bridges.bridges import *
from bridges.page_rank_benchmark import *
from bridges.data_src_dependent.data_source import *
import time as time_


def page_rank(graph, in_val, out):
    nvtx = graph.vertices.size
    degree = dict()
    for vert in graph.key_set():
        deg = 0
        for e in graph.out_going_edge_set_of(vert):
            deg+=1
        degree[vert] = deg

    for vert in graph.key_set():
        out[vert] = 1./nvtx

    lam = .8

    for i in range(0, 15):
        in_val,out = out,in_val

        for vert in graph.key_set():
            outv = (1.-lam)/nvtx

            for e in graph.out_going_edge_set_of(vert):
                fromv = e.to()
                outv += lam*(in_val[fromv]/degree[fromv])
            out[vert] = outv

def my_pr(gr, out):
    in_val = dict()
    page_rank(gr, in_val, out)


def main():
    bridges = Bridges(0, "test", "988181220044")
    bridges.set_visualize_JSON(True)
    bridges.connector.set_server("local")

    for i in range(1970, 1969):
        data_begin = int(round(time_.time() * 1000))
        v = get_wiki_data_actor_movie(i, 1975)
        data_end = int(round(time_.time() * 1000))
        data_elapsed_time = data_end-data_begin

        count = dict()
        for ma in v:
            count[ma.movie_uri] +=1
            count[ma.actor_uri] +=1

        movie_graph = GraphAdjList()
        edge_count = 0
        for ma in v:
            if count[ma.movie_uri] < 2 or count[ma.actor_uri] < 2:
                continue

            movie_vertex = movie_graph.get_vertex(ma.movie_uri)
            if movie_vertex is None:
                movie_graph.add_vertex(ma.movie_uri ,ma.movie_uri)
                movie_vertex = movie_graph.get_vertex(ma.movie_uri)
                movie_vertex.label = ma.movie_name

            actor_vertex = movie_graph.get_vertex(ma.actor_uri)
            if actor_vertex is None:
                movie_graph.add_vertex(ma.actor_uri, ma.actor_uri)
                actor_vertex = movie_graph.get_vertex(ma.actor_uri)
                actor_vertex.label = ma.actor_name

            movie_graph.add_edge(ma.movie_uri, ma.actor_uri)
            movie_graph.add_edge(ma.actor_uri, ma.movie_uri)
            edge_count+=1

        in_v = dict()
        out = dict()

        page_rank(movie_graph, in_v, out)



