movies = [
    {
        "title": "Interstellar",
        "genre": "Sci-Fi",
        "duration": 169,
    },
    {
        "title": "Inception",
        "genre": "Sci-Fi",
        "duration": 148,
    },
]

favorites = []


def add_movie(title: str, genre: str, duration: int) -> None:
    movies.append(
        {
            "title": title,
            "genre": genre,
            "duration": duration,
        }
    )


def show_movies() -> None:
    if not movies:
        print("No movies available.")
        return

    for index, movie in enumerate(movies, start=1):
        print(
            f"{index}. {movie['title']} | "
            f"{movie['genre']} | "
            f"{movie['duration']} min"
        )


def show_movie_info(index: int) -> None:
    if index < 1 or index > len(movies):
        print("Movie not found.")
        return

    movie = movies[index - 1]

    print(f"Title: {movie['title']}")
    print(f"Genre: {movie['genre']}")
    print(f"Duration: {movie['duration']} min")


def add_to_favorites(movie_title: str) -> None:
    if movie_title not in favorites:
        favorites.append(movie_title)


def show_favorites() -> None:
    if not favorites:
        print("No favorite movies.")
        return

    for movie in favorites:
        print(movie)
