from bridges.color import *
from bridges.data_src_dependent import data_source
from bridges.bridges import Bridges

#return the vertex the closest to some lat/lon coordinate
def getClosest(gr, lat, lon):
    closest = -1
    dist = float('inf')

    for k in gr.vertices:
        theosmvertex = gr.get_vertex(k).value
        vlat = theosmvertex.latitude
        vlon = theosmvertex.longitude
        vdist = (vlat-lat)*(vlat-lat)+(vlon-lon)*(vlon-lon)
        if (vdist < dist):
            dist = vdist
            closest = k

    return closest

#styling the source vertex
def style_root(gr, root) :
    elvis = gr.get_visualizer(root)
    elvis.color = Color(0,0,0)

def main():
    # Set bridges credentials
    bridges = Bridges(209, "test", "988181220044")

    # bridges.connector.set_server("local")

    bridges.set_title("Graph : OpenStreet Map Example")
    bridges.set_description("OpenStreet Map data of Charlotte downtown area, with colors based on distance from the center of downtown")
    bridges.set_server_url("local")
    bridges.set_coord_system_type('albersusa')
    bridges.set_map_overlay(True)
    # osm_data = data_source.get_osm_data("Charlotte, North Carolina", "default")
    osm_data = data_source.get_osm_data(35.28, -80.75, 35.32, -80.71, "default")

    print(osm_data.longitude_range)
    print(osm_data.latitude_range)

    gr = osm_data.get_graph()

    print (str(gr.vertices[0].get_locationX()) + " " + str(gr.vertices[0].get_locationY()))

    gr.force_large_visualization(True)


    #find and style de root of the Shortest Path

    # root = getClosest(gr,
    #                      (osm_data.latitude_range[0]+osm_data.latitude_range[1])/2,
    #                      (osm_data.longitude_range[0]+osm_data.longitude_range[1])/2)
    #
    # print ("root is "+str(root))
    #
    # style_root(gr, root)

    bridges.set_data_structure(gr)
    bridges.visualize()


if __name__ == '__main__':
    main()