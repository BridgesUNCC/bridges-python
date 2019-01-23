from bridges.bridges import *
from bridges.color import *
from bridges.color_grid import *
from bridges.data_src_dependent.data_source import *
import math
import re

def split_lyrics(lyrics):
    lyrics = re.sub('[\(\[].*?[\)\]]', '', lyrics)
    lyrics = lyrics.strip()
    lyrics_split = lyrics.split()
    print(lyrics_split)


    for i in range(len(lyrics_split)):
        lyrics_split[i] = lyrics_split[i].replace("\\W+$", "")
        lyrics_split[i] = lyrics_split[i].replace("^\\W+", "")
        lyrics_split[i] = lyrics_split[i].strip()

    return lyrics_split

def split_lines(lyrics):
    lyrics = lyrics.replace("\\[.+\\]", "")
    lyrics = lyrics.strip()
    lyrics_split = lyrics.split("\\n+")
    corpus = [len(lyrics_split)]

    for i in range(len(corpus)):
        corpus[i] = split_lyrics(lyrics_split[i])

    return corpus

def term_frequency(term, document):
    tf =0
    for word in document:
        if term.lower() == word.lower():
            tf = tf + 1
        else:
            tf = tf + 0

    return tf

def has_term(term, document):
    for word in document:
        if term.lower() == word.lower():
            return True
    return False

def documents_containing_term(term, corpus):
    n = 0

    for document in corpus:
        if has_term(term, document):
            n = n + 1
        else:
            n = n +0
    return n

def inverse_document_frequency(term, corpus):
    return math.log(len(corpus) / (1 + documents_containing_term(term, corpus)))

def term_frequency_inverse_document_frequency(term, document, corpus):
    return term_frequency(term, document) * inverse_document_frequency(term, corpus)

def get_unique_terms(corpus):
    unique_terms = []

    for document in corpus:
        for term in document:
            if term not in unique_terms:
                unique_terms.append(term)

    return unique_terms

def vectorize(document, corpus, unique_terms):
    vector = dict()

    for term in unique_terms:
        vector[term] = term_frequency_inverse_document_frequency(term, document, corpus)

def cosine(v1, v2):
    return float(dot_product(v1,v2)/ (norm(v1)*norm(v2)))

def dot_product(v1, v2):
    sum = 0

    for key in v1.keys():
        sum = sum + v1[key] * v2[key]

    return sum

def norm(vector):
    return math.sqrt(dot_product(vector, vector))


def main():
    # Init a Bridges Connection with your credentials
    bridges = Bridges(36, "test", "211416381091")

    # Set assignment title
    bridges.set_title("ListEQ Example")

    bridges.connector.set_server("local")

    song = get_song("Delicate").get_lyrics()
    lyrics = split_lyrics(song)

    if len(lyrics) > 480:
        word_count = 480
    else:
        word_count = len(lyrics)

    grid = ColorGrid(word_count, word_count)

    match_color = Color(0,0,0,1)
    default_color = Color(255,255,255,1)

    for i in range(word_count):
        for j in range(word_count):
            if lyrics[i].lower() != lyrics[j].lower():
                grid.set(i,j,match_color)
            else:
                grid.set(i,j,default_color)

    bridges.set_title("Song Grid")
    bridges.set_data_structure(grid)
    bridges.visualize()

if __name__ == '__main__':
    main()

