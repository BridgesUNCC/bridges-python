from bridges.bridges import *
from bridges.data_src_dependent.data_source import *
from bridges.graph_adj_list import *
import math

def calc_distance(la1, lo1, la2, lo2):
    radius = 6371

    la_distance = math.radians(la2 - la1)
    lo_distance = math.radians(lo2 - lo1)
    a = math.sin(la_distance / 2) * math.sin(la_distance / 2) + math.cos(math.radians(la1)) * math.cos(math.radians(la2)) * math.sin(lo_distance / 2) * math.sin(lo_distance / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance = radius * c
    return distance

def sorting(e):
    return e.magnitude

def main():
    # create the Bridges object, set credentials
    bridges = Bridges(0, "test", "988181220044")
    bridges.set_visualize_JSON(True)
    bridges.connector.set_server("local")
    bridges.set_title("Bacon Number: IMDB Actor-Movie Data")

    bridges.connector.set_server("local")

    graph = GraphAdjList()

    eqlist = get_earthquake_usgs_data(5000)

    eqlist.sort(key=sorting, reverse=True)

    for eq in eqlist:
        if len(graph.get_adjacency_list()) > 99:
            break
        graph.add_vertex(eq.title, eq.title)
        vis = graph.get_visualizer(eq.title)
        vis.set_location(eq.longit, eq.latit)
        vis.size = eq.magnitude

        red = ((eq.longit/180.0)*255)
        if red > 0:
            red = red
        else: red = 0

        blue = ((eq.longit / 180.0) * 255)
        if blue < 0:
            blue = blue * -1
        else: blue = 0

        green = ((eq.latit / 90.0) * 255)
        if green < 0:
            green = green * -1
        else: green = green
        vis.color = [int(red),int(green),int(blue),1.0]

    bridges.set_coord_system_type("equirectangular")
    bridges.set_data_structure(graph)
    bridges.set_map_overlay(True)
    bridges.set_title("Earthquake Map")
    bridges.visualize()

    for i in range(99):
        eq = eqlist[i]

        for j in range(99):
            if i == j:
                continue

            ua = eqlist[j]
            distance = calc_distance(eq.latit, eq.longit, ua.latit, ua.longit)

            if distance < 500:
                graph.add_edge(eq.title, ua.title)
                graph.get_link_visualizer(eq.title, ua.title).label = "%s.2f KM" % distance

    bridges.set_data_structure(graph)
    bridges.visualize()

    for i in range(99):
        eq = eqlist[i]
        vis = graph.get_visualizer(eq.title)

        vis.set_location(float('inf'), float('inf'))
        vis.size = eq.magnitude * 5

    bridges.set_data_structure(graph)
    bridges.set_map_overlay(False)
    bridges.visualize()

if __name__ == '__main__':
    main()
