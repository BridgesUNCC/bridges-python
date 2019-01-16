from bridges.bridges import *
from bridges.data_src_dependent.data_source import *
from bridges.data_src_dependent.actor_movie_imdb import *
from bridges.graph_adj_list import *

def create_genre_vertices(g, genres):
    for k in range(len(genres)):
        g.add_vertex(genres[k], ActorMovieIMDB())
        g.get_vertex(genres[k]).get_visualizer().set_color("red")
        g.get_vertex(genres[k]).get_visualizer().set_opacity(0.5)
        g.get_vertex(genres[k]).get_visualizer().set_size(50)

def group_movies_by_actors(g, actor_movie_data):
    verts = g.get_vertices()
    for k in range(len(actor_movie_data)):
        actor = actor_movie_data[k].get_actor()
        movie = actor_movie_data[k].get_movie()
        m_genre = actor_movie_data[k].get_genres()
        rating = actor_movie_data[k].get_movie_rating()

        if(actor not in g.get_vertices()):
            g.add_vertex(actor, actor_movie_data[k])
            verts[actor].get_visualizer().set_color("green")
            verts[actor].set_label(actor)

        if (movie not in g.get_vertices()):
            g.add_vertex(movie, actor_movie_data[k])
            verts[movie].get_visualizer().set_color("yellow")
            verts[movie].set_label(movie)

        g.add_edge(actor,movie,1)
        g.add_edge(movie,actor,1)

        for l in range(len(m_genre)):
            genre = m_genre[l]
            g.add_edge(movie, genre, 1)

            rating = g.get_vertex(movie).get_value().get_movie_rating()
            label = g.get_vertex(movie).get_label() + "(" + str(rating) + ")"
            g.get_vertex(movie).set_labe(label)

            if rating < 5.0:
                g.get_vertex(movie).get_visualizer().set_color("blue")
            elif rating < 6.0:
                g.get_vertex(movie).get_visualizer().set_color("green")
            elif rating < 7.0:
                g.get_vertex(movie).get_visualizer().set_color("yellow")
            elif rating < 8.0:
                g.get_vertex(movie).get_visualizer().set_color("tan")
            else:
                g.get_vertex(movie).get_visualizer().set_color("gold")

def main():
    # Initialize BRIDGES with your credentials
    bridges = Bridges(0, "test", "211416381091")

    # set title for visualization
    bridges.set_title("Graph Example(IMDB Data): Movies Grouped by Genre")

    bridges.connector.set_server("local")

    g = GraphAdjList()

    actor_movie_data = get_actor_movie_imdb_data()

    genres = ["Mystery", "Comedy",
				"Documentary", "Drama", "Romance", "Crime", "Thriller",
				"Biography", "Horror",
				"News", "Action",
				"Adventure", "Animation",
				"Family", "Sci-Fi",
				"Music", "Sport",
				"Short", "Musical",
				"History", "Talk-Show", "Reality-TV", "Game-Show", "Fantasy",
				"War"]

    create_genre_vertices(g, genres)
    group_movies_by_actors(g, actor_movie_data)
    bridges.set_data_structure(g)
    bridges.visualize()

if __name__ == '__main__':
    main()




