from Bridges import *
from data_src_dependent import DataSource
from GraphAdjMatrix import *

class GraphAdjMatrixtutorial:

    bridges = Bridges(33, "1343747370122", "test")

    actor_movie_data = DataSource.getActorMovieIMDBData(1813)

    g = GraphAdjMatrix()

    a1 = "Kevin_Bacon_(I)"
    a2 = "Denzel_Washington"

    g.add_vertex(a1, "")
    g.add_vertex(a2, "")

    g.add_edge(a1, a2, 1)

    g.get_vertices().get("Kevin_Bacon_(I)").get_visualizer().set_color("red")
    g.get_vertices().get("Denzel_Washington").get_visualizer().set_color("red")

    g.get_vertices().get("Kevin_Bacon_(I)").get_visualizer().set_size(20)
    g.get_vertices().get("Denzel_Washington").get_visualizer().set_size(20)

    cnt1 = 0
    cnt2 = 0

    for k in range(len(actor_movie_data)):
        a = actor_movie_data[k].get_Actor()
        m = actor_movie_data[k].get_Movie()

        if (a == "Kevin_Bacon_(I)" and cnt1 < 15):
            g.add_vertex(m, "")
            g.add_edge(a1, m, 1)
            g.add_edge(m, a1, 1)

            g.get_vertices().get(m).get_visualizer().set_opacity(0.5)
            cnt1 += 1

        elif (a == "Denzel_Washington" and cnt2 < 15):
            g.add_vertex(m, "")
            g.add_edge(a2, m, 1)
            g.add_edge(m, a2, 1)

            g.get_vertices().get(m).get_visualizer().set_opacity(0.5)
            cnt2 += 1

    bacon_row = g.get_adjacency_matrix("Kevin_Bacon_(I)")
    for entry, key in bacon_row.items():
        print(entry)
        if(entry != "Denzel Washington" and key != 0):
            g.get_visualizer(entry).set_color("green")

    bridges.set_data_structure(g)
    bridges.visualize()
