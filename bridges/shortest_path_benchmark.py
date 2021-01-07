from bridges.line_chart import *
from bridges.graph_benchmark import *
from bridges.data_src_dependent.data_source import *
from datetime import datetime
import time as time_

class ShortestPathBenchmark(GraphBenchmark):

    def __init__(self, p):
        super(ShortestPathBenchmark,self).__init__()
        self.__plot = p
        self.__plot.x_label = "Number of Edges"
        self.__plot.y_label = "Runtime (in s)"

    def __get_center(self, osm_data, graph, latc, lonc):
        def dist_function(v):
            return (v.latitude - latc) * (v.latitude - latc) + (v.logitude - lonc) * \
            (v.logitude - lonc)

        minindex = 0
        dist = dist_function(graph.get_vertex(minindex).value)

        for i in range(1, len(graph.vertices)):
            locdist = dist_function(graph.get_vertex(i).value)
            if locdist < dist:
                minindex = i
                dist = locdist

        return minindex

    def run(self, algoname, spalgo):
        time = []
        vtx_count = []
        edge_count = []

        reflat = 40.74
        reflong = -73.98

        radius = 0.2
        while radius < 0.15:
            osm_data = get_osm_data(reflat - radius, reflong - radius, reflat+radius, reflong+radius)
            graph = osm_data.get_graph()
            vtx_count = self._count_vertices(graph)
            edge_count = self._count_edges(graph)
            root = self.__get_center(osm_data, graph, reflat, reflong)

            level = dict()
            parent = dict()

            start = int(round(time_.time() * 1000))
            spalgo(graph, root, level, parent)
            end = int(round(time_.time() * 1000))

            elapsed_seconds = end - start
            time.append(elapsed_seconds)
            vtx_count.append(vtx_count)
            edge_count.append(edge_count)

            if elapsed_seconds > self.time_cap:
                break
        self.__plot.set_x_data(algoname, edge_count)
        self.__plot.set_y_data(algoname, time)
