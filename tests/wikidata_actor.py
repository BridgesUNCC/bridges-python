from bridges.bridges import *
from bridges.bfs_benchmark import *
import time


def get_bacon_number(gr, src_actor, mark, dist, parent):
    lq = queue.Queue()

    lq.put(src_actor)

    mark[src_actor] = "visited"
    dist[src_actor] = 0
    parent[src_actor] = "none"

    while not lq.empty():
        vertex = lq.get()

        if not vertex:
            continue

        for e in gr.out_going_edge_set_of(vertex):
            w = e.tov

            if mark[w] == "unvisited":
                mark[w] = "visited"
                lq.put(w)

                dist[w] = dist[vertex] + 1
                parent[w] = vertex

    return -1


def my_bfs(gr, src_actor, dist, parent):
    mark = {}

    for v in gr.vertices:
        mark[v] = "unvisited"
        parent[v] = "none"
        dist[v] = 0

    get_bacon_number(gr, src_actor, mark, dist, parent)


def main():
    bridges = Bridges(28, "test", "211416381091")
    bridges.connector.set_server_url("local")

    for year in [1980, 1979]:
        data_begin = time.time()

        v = get_wiki_data_actor_movie(year, 1981)

        data_elapsed_seconds = time.time() - data_begin

        print(data_elapsed_seconds)

        count = {}

        for ma in v:
            if ma.movie_uri in count.keys():
                count[ma.movie_uri] += 1
            else:
                count[ma.movie_uri] = 1

            if ma.actor_uri in count.keys():
                count[ma.actor_uri] += 1
            else:
                count[ma.actor_uri] = 1

        movie_graph = GraphAdjList()

        edge_count = 0

        for ma in v:
            if count[ma.movie_uri] < 2 or count[ma.actor_uri] < 2:
                continue

            movie_vertex = movie_graph.get_vertex(ma.movie_uri)
            if movie_vertex == None:
                movie_graph.add_vertex(ma.movie_uri, ma.movie_name)
                movie_vertex = movie_graph.get_vertex(ma.movie_uri)
                movie_vertex.label = ma.movie_name

            actor_vertex = movie_graph.get_vertex(ma.actor_uri)
            if actor_vertex == None:
                movie_graph.add_vertex(ma.actor_uri, ma.actor_name)
                actor_vertex = movie_graph.get_vertex(ma.actor_uri)
                actor_vertex.label = ma.actor_name

            movie_graph.add_edge(ma.movie_uri, ma.actor_uri)
            movie_graph.add_edge(ma.actor_uri, ma.movie_uri)
            edge_count += 1

        print("year: %s vertices: %d edge: %d" % (year, len(movie_graph.vertices), edge_count))

        bridges.set_data_structure(movie_graph)
        bridges.visualize()

        kevinuri = ""
        for ma in v:
            if ma.actor_name == "Kevin Bacon":
                kevinuri = ma.actor_uri
                print("Kevin Bacon is %s" % kevinuri)
                break

        start = time.time()

        mark = {}
        parent = {}
        dist = {}

        for v in movie_graph.vertices:
            mark[v] = "unvisited"
            parent[v] = "none"
            dist[v] = 0

        d = get_bacon_number(movie_graph, kevinuri, mark, dist, parent)

        print("bfs in ", time.time() - start)

        plot = LineChart()
        bfsb = BFSBenchamrk(plot)
        bfsb.time_cap = 0.8
        bfsb.run("mybfs", my_bfs)
        bridges.set_data_structure(plot)
        bridges.visualize()


if __name__ == '__main__':
    main()