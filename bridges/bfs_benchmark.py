from bridges.graph_benchmark import *
from bridges.line_chart import *
from datetime import datetime
import time as time_


class BFSBenchamrk(GraphBenchmark):

    def __init__(self, p):
        super(BFSBenchamrk, self).__init__()
        self.__plot = p
        self.__plot.x_label = "Number of Edges"
        self.__plot.y_label = "Runtime (in s)"

    def run(self, algo_name, bfsalgo):
        time = []
        vtx_count = []
        edge_count = []

        years = 0
        while years < 120:
            year = 2019 - years
            graph = GraphAdjList()
            vertex_count, edge_count = self._genertate_wiki_data_movie_actor(year, 2019, graph)
            root = self._highest_degree_vertex(graph)
            level = dict()
            parent = dict()
            start = int(round(time_.time() * 1000))
            bfsalgo(graph, root, level, parent)
            end = int(round(time_.time() * 1000))
            elapsed_time = end - start

            time.append(elapsed_time)
            vtx_count.append(vertex_count)
            edge_count.append(edge_count)

            if elapsed_time > self.time_cap:
                break
            years = 1.2 * years + 1

        self.__plot.set_x_data(algo_name, edge_count)
        self.__plot.set_y_data(algo_name, time)



