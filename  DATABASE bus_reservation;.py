CREATE DATABASE bus_reservation;


------------------------

CREATE TABLE bus_seats (
    seat_number SERIAL PRIMARY KEY,
    bus_number VARCHAR(10),
    passenger_name VARCHAR(50),
    booking_status BOOLEAN DEFAULT false
);


import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="bus_reservation",
    user="postgres",
    password="yourpassword"
)



def display_seats(bus_number):
    cur = conn.cursor()
    cur.execute("SELECT seat_number FROM bus_seats WHERE bus_number=%s AND booking_status=false", (bus_number,))
    rows = cur.fetchall()
    seats = [row[0] for row in rows]
    print("Available seats:", seats)

def book_seat(bus_number, seat_number, passenger_name):
    cur = conn.cursor()
    cur.execute("UPDATE bus_seats SET booking_status=true, passenger_name=%s WHERE bus_number=%s AND seat_number=%s", (passenger_name, bus_number, seat_number))
    conn.commit()
    print("Seat booked successfully!")


def cancel_booking(bus_number, seat_number):
    cur = conn.cursor()
    cur.execute("UPDATE bus_seats SET booking_status=false, passenger_name=NULL WHERE bus_number=%s AND seat_number=%s", (bus_number, seat_number))
    conn.commit()
    print("Booking cancelled successfully!")


display_seats("XYZ123")
book_seat("XYZ123", 1, "John Doe")
cancel_booking("XYZ123", 1)

