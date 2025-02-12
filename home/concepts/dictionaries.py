movie_names =   ["Morbious", "Dune", "Batman"]
movie_ratings = [    9,         2,       4   ]
#instead of the above representation

movie_A ={
    "name":"Morbious",
    "rating": 9
}

movie_B = {
    "name": "Dune",
    "rating": 2
}

movie_C= {
    "name": "Batman",
    "rating": 4
}

movies = [movie_A, movie_B, movie_C]

print(movies)
for movie in movies:
    print(movie)

print("\naccessing value")
print(movie_C["name"])


print("\nchanging value")
print(movie_C)
movie_C["rating"]=10
print(movie_C)

print("\nadding key/value")
movie_C["length"]="2 hours"
print(movie_C)