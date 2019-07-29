from bridges.data_src_dependent import *
from bridges.graph_adj_list import *
from bridges.bridges import *


def main():
    # Init a Bridges connection with your credentials
    bridges = Bridges(0, "test", "988181220044")
    bridges.set_visualize_JSON(True)
    bridges.connector.set_server("local")

    #Title and Description
    bridges.set_title("A Simple Graph (Adjacency List) Example using IMDB Actor/Movie Data")
    bridges.set_description("Two lists each having an actor as the root node with 15 movies they played in as leaf nodes. "
            +	"Root nodes are both red, Kevin Bacon's leaf nodes are green and Denzel Washington's leaf nodes are neutral.")

    actor_movie_data = get_actor_movie_imdb_data(1813)

    # create an adjacency list based graph
    g = GraphAdjList()

    # first create vertices for two actors and add the to the graph
    a1 = "Kevin_Bacon_(I)"
    a2 = "Denzel_Washington"

    g.add_vertex(a1, "")
    g.add_vertex(a2, "")

    g.get_vertex(a1).color = "red"
    g.get_vertex(a1).size = 30
    g.get_vertex(a2).color = "red"
    g.get_vertex(a2).size = 30

    # add and edge between the two actors
    g.add_edge(a1, a2)
    g.get_link_visualizer(a1, a2).color = "magenta"
    g.get_link_visualizer(a1, a2).thickness = 4.0

    # get their nodes
    v1 = g.get_vertex(a1)
    v2 = g.get_vertex(a2)

    cnt1 = 0
    cnt2 = 0

    # we will find the first 15 immediate neighbors of the two actors
    # and color those links and nodes by following their adjacency lists
    for k in range(len(actor_movie_data)):
        # from the actor movie data, get and actor-movie pair
        a = actor_movie_data[k].actor
        m = actor_movie_data[k].movie

        if (a == "Kevin_Bacon_(I)" and cnt1 < 15):
            # add vertices for this movie and an edge for the link
            g.add_vertex(m, "")
            g.add_edge(a1, m)
            g.add_edge(m, a1)
            # make the movie node a bit transparent
            g.get_vertex(m).opacity = 0.5
            cnt1 += 1

        elif (a == "Denzel_Washington" and cnt2 < 15):
            # add vertices for this movie and an edge for the link
            g.add_vertex(m, "")
            g.add_edge(a2, m)
            g.add_edge(m, a2)
            # make the movie node a bit transparent
            g.get_vertex(m).opacity = 0.5
            cnt2 += 1

    # Next, we illustrate traversing the adjacency list and color the movie
    # nodes adjacent to the Kevin Bacon node

    # first get the adjacency list for Kevin Bacon
    for edge in g.out_going_edge_set_of(a1):
        f = edge.fromv
        to = edge.tov
        if to != a2:
            g.get_visualizer(to).color = "turquoise"

    for edge in g.out_going_edge_set_of(a2):
        f = edge.fromv
        to = edge.tov
        if to != a1:
            g.get_visualizer(to).color = "orange"

    # Pass the graph object to BRIDGES
    bridges.set_data_structure(g)
    # visualize the graph
    bridges.visualize()


if __name__ == "__main__":
    main()