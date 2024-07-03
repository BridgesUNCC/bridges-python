from bridges.bridges import *
from bridges.graph_adj_list import *
from bridges.element import *
from bridges.link_visualizer import *
from bridges.edge import *
import math


def main():
    # Initialize BRIDGES with your credentials
    bridges = Bridges(4, "test", "988181220044")
    bridges.set_title("MST on US Cities Dataset")
    bridges.set_server_url("local")
    bridges.set_coord_system_type("equirectangular")
    bridges.map = ["world", "china"]
    bridges.set_map_overlay(True)

    graph = GraphAdjList()
    # build graph using a set of cities in North Carolina
    build_nc_graph(graph, "nc_cities.txt")

    bridges.set_data_structure(graph)
    bridges.visualize()

    cost = 0
    # run Prim's MST algorithm
    cost = build_mst(graph, "Asheville", cost)
    print("MST Min. Cost: " + str(cost))
    bridges.visualize()

    cost = 0
    # alternate implementation, using only fringe vertices to make decision
    build_mst_prim_fringe(graph, cost)
    bridges.visualize()


def build_nc_graph(graph, file):
    with open(file, 'r') as f:
        cities = {}
        lat = []
        lon = []

        # read the data and put it into cities array
        # add the vertices to the graph
        for x in range(0, len(open("nc_cities.txt").readlines())):
            line = f.readline().strip()  # eliminates \n
            tab = line.split(" ")
            graph.add_vertex(tab[0])
            cities[tab[0]] = x
            lat.append(float(tab[2]))
            lon.append(float(tab[3]))
            i = lat.index(float(tab[2]))
            graph.get_visualizer(tab[0]).set_location(lon[i], lat[i])

        # compute distances between all pairs of cities
        for city1 in graph.vertices.keys():
            for city2 in graph.vertices.keys():
                if city1 != city2:
                    distance = get_dist(lat[int(cities.get(city1))], lon[int(cities.get(city1))],
                                        lat[int(cities.get(city2))], lon[int(cities.get(city2))])
                    graph.add_edge(city1, city2, label=str(distance / 1000), data=distance / 1000)
                    graph.add_edge(city2, city1, label=str(distance / 1000), data=distance / 1000)

                    graph.get_link_visualizer(city1, city2).opacity = 0.10
                    graph.get_link_visualizer(city2, city1).opacity = 0.10
        f.close()


def get_dist(lat1, long1, lat2, long2):
    # haversine formula
    # in meters
    R = 6371000
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    del_phi = math.radians(lat2 - lat1)
    del_lambda = math.radians(long2 - long1)

    a = math.sin(del_phi / 2) * math.sin(del_phi / 2) + math.cos(phi1) * math.cos(phi2) * math.sin(
        del_lambda / 2) * math.sin(del_lambda / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    # in meters
    return R * c


def get_min_vertex(graph, min_dist, mark):
    # initialize to an unvisited vertex, this is not an efficient algo, should use priority queue!
    vertex = ""
    # set vertex to first unvisited node
    for i in graph.vertices.keys():
        if not mark[i]:
            vertex = i

    # find another vertex that has the shortest edge, which will be a tree vertex
    for i in graph.vertices.keys():
        if (not mark[i]) and min_dist[i] < min_dist[vertex]:
            vertex = i

    return vertex


def build_mst(graph, start, cost):
    cost = 0
    # initialize mark array and graph vertices
    min_dist = {}
    mark = {}
    tree_verts = {}

    for node in graph.vertices.keys():
        min_dist[node] = float('inf')
        mark[node] = False

    min_dist[start] = 0.0

    for i in graph.vertices.keys():
        # local decision to add the edge with the shortest distance
        vertex = get_min_vertex(graph, min_dist, mark)
        mark[vertex] = True

        if vertex != start:
            # styling edge
            graph.get_link_visualizer(tree_verts[vertex], vertex).color = 'red'
            cost += graph.get_edge(tree_verts[vertex], vertex).edge_data

        # update the distances, given we have now added a tree vertex
        for edge in graph.out_going_edge_set_of(vertex):
            edge_to = edge.tov
            edge_from = edge.fromv
            edge_wt = graph.get_edge(edge_to, edge_from).edge_data

            if min_dist[edge_to] > edge_wt:
                min_dist[edge_to] = edge_wt
                # keep track of parent
                tree_verts[edge_to] = edge_from
                # highlight the tree vertex
                graph.get_visualizer(vertex).color = "red"
                graph.get_visualizer(vertex).size = 3.0
                graph.get_visualizer(vertex).label = vertex
    return cost


# this version only considers the fringe vertices of the current set of tree vertices
# more efficient as the edge to be added to the MST will always be a fringe vertices
def build_mst_prim_fringe(graph, cost):
    cost = 0
    # Initialize mark array and graph vertices
    mark = {}
    min_dist = {}
    min_dist_verts = {}

    for v in graph.vertices.keys():
        mark[v] = False
        min_dist[v] = float('inf')

    start_vertex = "Asheville"
    min_dist[start_vertex] = 0.0

    min_vert = start_vertex
    for x in range(0, len(graph.vertices.keys())):
        # find the min edge vertex among the fringe verts of v
        mark[min_vert] = True
        graph.get_visualizer(min_vert).color = "green"
        graph.get_visualizer(min_vert).size = 5.0

        if x > 0:
            src = min_dist_verts[min_vert]
            dest = min_vert
            graph.get_link_visualizer(src, dest).color = 'red'
            graph.get_link_visualizer(dest, src).color = 'red'
            graph.get_link_visualizer(src, dest).thickness = 2.0
            graph.get_link_visualizer(dest, src).thickness = 2.0
            cost += min_dist[min_vert]

        v = min_vert
        min_edge_wt = float('inf')
        for edge in graph.out_going_edge_set_of(v):
            edge_to = edge.tov
            edge_from = edge.fromv
            edge_wt = graph.get_edge(edge_to, edge_from).edge_data
            if (edge_wt < min_edge_wt) and not mark[edge_to]:
                min_edge_wt = edge_wt
                min_vert = edge_to

        # update distances
        for edge in graph.out_going_edge_set_of(v):
            edge_to = edge.tov
            edge_from = edge.fromv
            edge_wt = graph.get_edge(edge_to, edge_from).edge_data
            if min_dist[edge_to] > edge_wt:
                min_dist[edge_to] = edge_wt
                min_dist_verts[edge_to] = edge_from


if __name__ == "__main__":
    main()