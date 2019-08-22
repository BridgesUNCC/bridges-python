from bridges.graph_benchmark import *
from bridges.line_chart import *
from datetime import datetime
import time as time_


class BFSBenchamrk(GraphBenchmark):
    """
    @brief Benchmarks Breadth First Search algorithms.

	Benchmarks BFS algorithms and add time series to a LineChart.

	One can also set a maximum time spent on a particular run
	using setTimeCap().

	The BFS algorithms must have for prototype:

	and can be passed to the run function for being
	benchmarked. A typical use would look something like

	code
	lc LineChart();
	sb BFSBenchmark(lc);
	sb.run("mybfsalgorithm", bfsalgo);
	endcode

	@author Erik Saule
	@date 07212019
    """
    def __init__(self, p):
        super(BFSBenchamrk, self).__init__()
        self.__plot = p
        self.__plot.x_label = "Number of Edges"
        self.__plot.y_label = "Runtime (in s)"

    def run(self, algo_name, bfsalgo):
        """
        benchmark one implementation
        Args:
            algo_name: screen name of the algorithm to be used in the visualization
            bfsalgo: pointer to the sorting function to benchmark
        """
        time = []
        vtx_count = []
        edge_cnt = []

        years = 0
        while years < 120:
            year = 2019 - years
            graph = GraphAdjList()
            vertex_count, edge_count = self._genertate_wiki_data_movie_actor(int(year), 2019, graph)
            root = self._highest_degree_vertex(graph)
            level = dict()
            parent = dict()
            start = float((time_.time() * 1000))
            bfsalgo(graph, root, level, parent)
            end = float((time_.time() * 1000))
            elapsed_time = end - start
            time.append(elapsed_time)
            vtx_count.append(vertex_count)
            edge_cnt.append(edge_count)

            if elapsed_time > self.time_cap:
                break
            years = 1.2 * years + 1

        self.__plot.set_x_data(algo_name, edge_cnt)
        self.__plot.set_y_data(algo_name, time)



