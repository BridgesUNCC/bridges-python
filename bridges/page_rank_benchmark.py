from bridges.graph_benchmark import *
from bridges.line_chart import *
from datetime import datetime

class PageRankBenchmark(GraphBenchmark):
    def __init__(self, p):
        super(PageRankBenchmark, self).__init__()
        self.__plot = p
        p.x_label = "Number of Edges"
        p.y_label = "Runtime (in s)"

    def run(self, algoname, paralgo):
        time = []
        vtx_count = []
        edge_count = []

        years = 0
        while years < 120:
            year = 2019 - years
            graph = GraphAdjList()
            vertex_count, edge_count = self._genertate_wiki_data_movie_actor(year, 2019, graph)
            pr = dict()
            start = datetime.now()
            paralgo(graph, pr)
            end = datetime.now()
            elapsed_time = end - start

            time.append(elapsed_time)
            vtx_count.append(vertex_count)
            edge_count.append(edge_count)

            if elapsed_time > self.time_cap:
                break
            years = 1.2 * years + 1

        self.__plot.set_x_data(algoname, edge_count)
        self.__plot.set_y_data(algoname, time)