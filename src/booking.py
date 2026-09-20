bookings = []


def book_tickets(movie_title: str, quantity: int) -> None:
    bookings.append(
        {
            "movie": movie_title,
            "quantity": quantity,
        }
    )

    print("Tickets booked successfully.")


def show_bookings() -> None:
    if not bookings:
        print("No bookings.")

        return

    for index, booking in enumerate(bookings, start=1):
        print(
            f"{index}. {booking['movie']} - "
            f"{booking['quantity']} ticket(s)"
        )


def cancel_booking(index: int) -> None:
    if index < 1 or index > len(bookings):
        print("Booking not found.")
        return

    bookings.pop(index - 1)

    print("Booking cancelled.")