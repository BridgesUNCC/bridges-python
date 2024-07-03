from bridges.bridges import *
from bridges.graph_adj_list import *
from bridges.element import *
from bridges.link_visualizer import *
from bridges.edge import *
from bridges.symbol_collection import *
from bridges.circle import *
from bridges.polyline import *
import math


def main():
    bridges = Bridges(10, "test", "988181220044")
    bridges.set_title("Convex Hull on USA dataset")
    bridges.set_server_url("local")
    bridges.set_map_overlay(True)
    bridges.set_coord_system_type("albersusa")


    sc = construct_graph(False, "./us_cities.txt")
    # NON-CONTINENTAL VIEWPORT
    sc.setviewport(-6280, -3000, 1000, 1800)
    bridges.map = ["us", "all"]
    bridges.set_data_structure(sc)
    bridges.visualize()

    sc = construct_graph(True, "./us_cities.txt")
    # CONTINENTAL VIEWPORT
    sc.setviewport(-5000, -3000, 1000, 2000)
    bridges.map = ["us", "all"]
    bridges.set_description("Not including Alaska and Hawaii")
    bridges.set_data_structure(sc)
    bridges.visualize()

    sc = construct_graph(True, "./us_cities.txt", "North_Carolina")
    # CONTINENTAL VIEWPORT
    sc.setviewport(-5000, -3000, 1000, 2000)
    bridges.map = ["us", "North Carolina"]
    bridges.set_description("Not including Alaska and Hawaii")
    bridges.set_data_structure(sc)
    bridges.visualize()


def construct_graph(continental, file, state_filter=None):
    # Constructs graph using Circles as points
    sc = SymbolCollection()
    city_coords = {}
    lat = {}
    lon = {}

    with open(file, 'r') as f:
        for x in range(0, 1000):
            line = f.readline().strip()
            line_arr = line.split(" ")
            if state_filter is not None:
                if line_arr[1] == state_filter:
                    city = line_arr[0]
                    print(city)
                    latitude = line_arr[2]
                    longitude = line_arr[3]
                    lat[x - 1] = float(latitude)
                    lon[x - 1] = float(longitude)

                    # if city is honolulu or anchorage AND continental is True, remove from dict
                    if non_continental(city) and continental:
                        continue

                    # creating the point
                    city_state_pt = Circle(locx=lon[x - 1], locy=lat[x - 1], r=5.0)
                    city_state_pt.fill_color = "blue"

                    # make charlotte unique
                    if city == "Charlotte":
                        city_state_pt.fill_color = "red"
                        city_state_pt.radius = 10.0

                    city_coords[city] = str(lon[x - 1]) + " " + str(lat[x - 1])
                    sc.add_symbol(city_state_pt)
                else:
                    continue
            else:
                city = line_arr[0]
                print(city)
                latitude = line_arr[2]
                longitude = line_arr[3]
                lat[x - 1] = float(latitude)
                lon[x - 1] = float(longitude)

                # if city is honolulu or anchorage AND continental is True, remove from dict
                if non_continental(city) and continental:
                    continue

                # creating the point
                city_state_pt = Circle(locx=lon[x - 1], locy=lat[x - 1], r=5.0)
                city_state_pt.fill_color = "blue"

                # make charlotte unique
                if city == "Charlotte":
                    city_state_pt.fill_color = "red"
                    city_state_pt.radius = 10.0

                city_coords[city] = str(lon[x - 1]) + " " + str(lat[x - 1])
                sc.add_symbol(city_state_pt)

    brute_force(sc, city_coords)
    return sc


def brute_force(sc, city_coords):
    # Check if all points are to the 'left' of city1,city2 edge
    # if true, draw hull line
    for city1 in city_coords.keys():
        for city2 in city_coords.keys():
            city1_coords = city_coords.get(city1).split(" ")
            city2_coords = city_coords.get(city2).split(" ")
            x1 = float(city1_coords[0])
            y1 = float(city1_coords[1])
            x2 = float(city2_coords[0])
            y2 = float(city2_coords[1])
            positive_counter = 0
            negative_counter = 0
            for city3 in city_coords.keys():
                # ensures all 3 cities are unique
                if city1 != city3 and city1 != city2 and city2 != city3:
                    city3_coords = city_coords.get(city3).split(" ")
                    x3 = float(city3_coords[0])
                    y3 = float(city3_coords[1])
                    # calculating Ax + By + C, only care about the sign (+,-) of result
                    result = ((y2 - y1) * x3 + (x1 - x2) * y3 + (x2 * y1 - x1 * y2))

                    if result > 0:
                        positive_counter = positive_counter + 1
                    elif result < 0:
                        negative_counter = negative_counter + 1

                    # if true, edge is not on the hull, repeat with new cities
                    if positive_counter > 0 and negative_counter > 0:
                        break

            # ensures line is on hull before drawing
            if positive_counter > 0 and negative_counter == 0 or positive_counter == 0 and negative_counter > 0:
                if city1 != city2:
                    line = Polyline()
                    line.add_point(x1, y1)
                    line.add_point(x2, y2)
                    line.stroke_color = "purple"
                    sc.add_symbol(line)


def non_continental(city):
    # returns True if city == Honolulu or Anchorage
    return city == "Honolulu" or city == "Anchorage"


if __name__ == "__main__":
    main()