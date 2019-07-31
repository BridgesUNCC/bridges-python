from bridges.bridges import *
from bridges.data_src_dependent.data_source import *
from bridges.data_src_dependent.actor_movie_imdb import *
from bridges.graph_adj_list import *

def create_genre_vertices(g, genres):
    for k in range(len(genres)):
        g.add_vertex(genres[k], ActorMovieIMDB())
        g.get_vertex(genres[k]).color = "red"
        g.get_vertex(genres[k]).opacity = 0.5
        g.get_vertex(genres[k]).size = 50

def group_movies_by_actors(g, actor_movie_data):
    verts = g.vertices
    for k in range(len(actor_movie_data)):
        actor = actor_movie_data[k].actor
        movie = actor_movie_data[k].movie
        m_genre = actor_movie_data[k].generes
        rating = actor_movie_data[k].rating

        if(actor not in g.vertices):
            g.add_vertex(actor, actor_movie_data[k])
            verts[actor].color = "green"
            verts[actor].label = actor

        if (movie not in g.vertices):
            g.add_vertex(movie, actor_movie_data[k])
            verts[movie].color = "yellow"
            verts[movie].label = movie

        g.add_edge(actor,movie,1)
        g.add_edge(movie,actor,1)

        for l in range(len(m_genre)):
            genre = m_genre[l]
            g.add_edge(movie, genre, 1)
            label = g.get_vertex(movie).label + "(" + str(rating) + ")"
            g.get_vertex(movie).label = label
            if rating < 5.0:
                g.get_vertex(movie).color = "blue"
            elif rating < 6.0:
                g.get_vertex(movie).color = "green"
            elif rating < 7.0:
                g.get_vertex(movie).color ="yellow"
            elif rating < 8.0:
                g.get_vertex(movie).color = "tan"
            else:
                g.get_vertex(movie).color = "gold"

def main():
    bridges = Bridges(0, "test", "988181220044")
    bridges.set_visualize_JSON(True)
    bridges.connector.set_server("local")

    g = GraphAdjList()

    actor_movie_data = get_actor_movie_imdb_data2()

    genres = ["Mystery", "Comedy","Documentary", "Drama", "Romance", "Crime", "Thriller","Biography", "Horror","News", "Action","Adventure", "Animation","Family", "Sci-Fi","Music", "Sport","Short", "Musical","History", "Talk-Show", "Reality-TV", "Game-Show", "Fantasy","War"]

    create_genre_vertices(g, genres)
    group_movies_by_actors(g, actor_movie_data)
    bridges.set_data_structure(g)
    bridges.visualize()

if __name__ == '__main__':
    main()




