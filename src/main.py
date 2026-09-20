from src.booking import book_tickets, show_bookings, cancel_booking, bookings
from src.movies import show_movies, add_movie, show_movie_info, show_favorites, add_to_favorites, movies


def show_menu() -> None:
    print("\n=== Cinema Booking ===")
    print("1. View movies")
    print("2. Add movie")
    print("3. Movie information")
    print("4. Book tickets")
    print("5. Add movie to favorites")
    print("6. View favorites")
    print("7. View bookings")
    print("8. Cancel booking")
    print("9. Statistics")
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


def add_movie_to_favorites() -> None:
    print("\n=== Add to Favorites ===")
    show_movies()
    try:
        movie_number = int(input("Enter movie number: "))
    except ValueError:
        print("Please enter a number.")
        return
    from movies import movies
    if movie_number < 1 or movie_number > len(movies):
        print("Movie not found.")
        return
    add_to_favorites(movies[movie_number - 1]["title"])
    print("Movie added to favorites.")


def view_favorites() -> None:
    print("\n=== Favorite Movies ===")
    show_favorites()


def view_movie_info() -> None:
    print("\n=== Movie Information ===")
    show_movies()

    try:
        movie_number = int(input("Enter movie number: "))
    except ValueError:
        print("Please enter a number.")
        return

    show_movie_info(movie_number)


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


def show_statistics() -> None:
    print("\n=== Statistics ===")
    available_movies = len(movies)
    booked_tickets = sum(booking["quantity"] for booking in bookings)
    print(f"Available movies: {available_movies}")
    print(f"Booked tickets: {booked_tickets}")


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
            create_booking()

        elif choice == "5":
            add_movie_to_favorites()

        elif choice == "6":
            view_favorites()

        elif choice == "7":
            view_bookings()

        elif choice == "8":
            cancel_ticket_booking()
        elif choice == "9":
            show_statistics()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
