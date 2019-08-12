from bridges.graph_adj_list import *
from bridges.data_src_dependent.data_source import *
import sys

class GraphBenchmark:

    def __init__(self):
        self._time_cap = sys.float_info.max

    def _genertate_wiki_data_movie_actor(self, year_min, year_max, movie_graph):
        v = get_wiki_data_actor_movie(year_min, year_max)
        edge_count = 0
        vertex_count = 0

        for ma in v:
            movie_vertex = movie_graph.get_vertex(ma.movie_name)
            if movie_vertex is None:
                movie_graph.add_vertex(ma.movie_uri, ma.movie_name)
                movie_vertex = movie_graph.get_vertex(ma.movie_uri)
                vertex_count += 1

            actor_vertex = movie_graph.get_vertex(ma.actor_uri)
            if actor_vertex is None:
                movie_graph.add_vertex(ma.actor_uri, ma.actor_name)
                actor_vertex = movie_graph.get_vertex(ma.actor_uri)
                vertex_count += 1

            movie_graph.add_edge(ma.movie_uri, ma.actor_uri)
            movie_graph.add_edge(ma.actor_uri, ma.movie_uri)
            edge_count += 2

        return vertex_count, edge_count

    def _highest_degree_vertex(self, gr):
        max_degree = -1
        ret = ""

        for k in gr.key_set():
            degree = 0
            for e in gr.out_going_edge_set_of(k):
                degree += 1
            if degree > max_degree:
                max_degree = degree
                ret = k

        return ret

    def _count_vertices(self, gr):
        return len(gr.vertices)

    def _count_edges(self, gr):
        edges = 0
        for k in gr.key_set():
            for e in gr.out_going_edge_set_of(k):
                edges+=1
        return edges

    @property
    def time_cap(self):
        return self._time_cap

    @time_cap.setter
    def time_cap(self, cap_in_s):
        self._time_cap = cap_in_s






