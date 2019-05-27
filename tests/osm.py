from bridges.data_src_dependent import data_source
from bridges.bridges import Bridges
import os
import queue as Q
    
#return the vertex the closest to some lat/lon coordinate
def getClosest(gr, lat, lon):
    closest = -1
    dist = float('inf')

    for k in gr.vertices:
        theosmvertex = gr.get_vertex(k).get_value()
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
    elvis.set_color(1,0,0)

#shortest path function
def dijkstra (gr, root) :
    distance = {}
    parent = {}
    
    for v in gr.vertices:
        distance[v] = float('inf')

    distance[root] = 0

    qu = Q.PriorityQueue()
    qu.put((distance[root], root))
    
    while not qu.empty():
        (d,v) = qu.get()
        if d > distance[v]: #because we use a heap and not a fibonacci heap, the same vertex could show up multiple times.
            continue

        for nei in gr.out_going_edge_set_of(v):
            to = nei.tov()
            edge_length=nei.get_edge_data()
            #Relax the edge

            if distance[v]+edge_length < distance[to]:
                #new SP found
                distance[to] = distance[v]+edge_length
                qu.put((distance[nei], nei))
                parent[to] = v
            
    return (distance, parent)
    
#style the graph based on distance
def style_distance(gr, distance):
    #find the maximum distance which is not infinity
    maxd = 0
    for v in gr.vertices:
        if distance[v] != float('inf') and distance[v] > maxd:
            maxd = distance[v]

    #style the color of vertices with a linear scale
    for v in gr.vertices:
        if distance[v] != float('inf'):
            grays = (maxd-distance[v])/255
            gr.get_vertex(v).set_color("red")

#style the path between the root and the destination (root is not given because all parent path goes to root)
def style_parent(gr, parent, dest):
    # style all vertices to almost invisible
    for v in gr.vertices:
        gr.get_visualizer(v).set_color(0, 0, 0, 0.2)

    # style all edges to almost invisible
    for v in gr.vertices:
        nei_link = gr.get_adjacency_list(v)

        #CHANGE AFTER EXPOSING LINK/ELEMENT VIS TO ELEMENT CLASS
        while (nei_link != None):
            nei=nei_link.get_value().tov()
            gr.get_link_visualizer(v, nei).set_color(0, 0, 0, 0.2)

            nei_link=nei_link.get_next()

    # Style the path between parent and dest in black
    prev = dest
    cur = dest
    while cur != None:
        #style node
        gr.get_visualizer(cur).set_color(0, 0, 0, 1)

        #style edge along the path
        if prev != cur:
            gr.get_link_visualizer(cur, prev).set_color(0, 0, 0, 1) 
            gr.get_link_visualizer(prev, cur).set_color(0, 0, 0, 1) #some of these back edges don't exist but bridges ignore them
        
        prev = cur
        cur = parent.get(cur)
    
    return

def main():

    #get data
    bridges = Bridges(100, "test", "137842425086")
    bridges.connector.set_server("clone")
    
    osm_data = data_source.get_osm_data("uncc_campus")
    
    print(osm_data.longitude_range)
    print(osm_data.latitude_range)
    
    gr = osm_data.get_graph()

    #find and style de root of the Shortest Path
    
    root = getClosest(gr,
                         (osm_data.latitude_range[0]+osm_data.latitude_range[1])/2,
                         (osm_data.longitude_range[0]+osm_data.longitude_range[1])/2)

    print (root)

    style_root(gr, root)

    #run Shortest Path
    (distance,parent) = dijkstra(gr,root)

    #style vertices based on distances
    style_distance(gr, distance)
    
    bridges.set_data_structure(gr)
    bridges.visualize()

    #find a destination
    dest = getClosest(gr,
                      (osm_data.latitude_range[0]+(osm_data.latitude_range[1]-osm_data.latitude_range[0])/4),
                      (osm_data.longitude_range[0]+(osm_data.longitude_range[1]-osm_data.longitude_range[0])/4))

    #style the path from root to destination
    style_parent(gr,parent, dest)

    bridges.set_data_structure(gr)
    bridges.visualize()


if __name__ == "__main__":
    main()
