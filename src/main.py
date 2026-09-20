from src.booking import book_tickets, show_bookings, cancel_booking
from src.movies import show_movies, add_movie, show_movie_info, search_movies


def show_menu() -> None:
    print("\n=== Cinema Booking ===")
    print("1. View movies")
    print("2. Add movie")
    print("3. Movie information")
    print("4. Search movies")
    print("5. Book tickets")
    print("6. View bookings")
    print("7. Cancel booking")
    print("0. Exit")


def view_movies() -> None:
    print("\n=== Movies ===")
    show_movies()


def create_movie() -> None:
    print("\n=== Add Movie ===")

    title = input("Enter movie title: ").strip()
    genre = input("Enter genre: ").strip()

    try:
        duration = int(input("Enter duration in minutes: "))
    except ValueError:
        print("Duration must be a number.")
        return

    if not title or not genre:
        print("Title and genre cannot be empty.")
        return

    add_movie(title, genre, duration)
    print("Movie added successfully.")


def view_movie_info() -> None:
    print("\n=== Movie Information ===")
    show_movies()

    try:
        movie_number = int(input("Enter movie number: "))
    except ValueError:
        print("Please enter a number.")
        return

    show_movie_info(movie_number)


def search_movie() -> None:
    print("\n=== Search Movies ===")
    query = input("Enter movie title: ").strip()
    if not query:
        print("Search query cannot be empty.")
        return
    results = search_movies(query)
    if not results:
        print("No movies found.")
        return
    print("\nSearch results:")
    for index, movie in enumerate(results, start=1):
        print(f"{index}. {movie['title']} | " f"{movie['genre']} | " f"{movie['duration']} min")


def create_booking() -> None:
    print("\n=== Book Tickets ===")
    show_movies()

    from movies import movies

    try:
        movie_number = int(input("Enter movie number: "))
    except ValueError:
        print("Please enter a number.")
        return

    if movie_number < 1 or movie_number > len(movies):
        print("Movie not found.")
        return

    try:
        quantity = int(input("Enter number of tickets: "))
    except ValueError:
        print("Number of tickets must be a number.")
        return

    if quantity <= 0:
        print("Number of tickets must be greater than zero.")
        return

    movie_title = movies[movie_number - 1]["title"]

    book_tickets(movie_title, quantity)


def view_bookings() -> None:
    print("\n=== Bookings ===")
    show_bookings()


def cancel_ticket_booking() -> None:
    print("\n=== Cancel Booking ===")
    show_bookings()

    from booking import bookings

    if not bookings:
        return

    try:
        booking_number = int(input("Enter booking number: "))
    except ValueError:
        print("Please enter a number.")
        return

    cancel_booking(booking_number)


def main() -> None:
    while True:
        show_menu()

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            view_movies()

        elif choice == "2":
            create_movie()

        elif choice == "3":
            view_movie_info()

        elif choice == "4":
            search_movie()

        elif choice == "5":
            create_booking()

        elif choice == "6":
            view_bookings()

        elif choice == "7":
            cancel_ticket_booking()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
