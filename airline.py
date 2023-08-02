from typing import Optional
import psycopg2 as pg
import datetime


class Airline:

    def __init__(self) -> None:
        """Initialize this class, with no database connection yet.
        """
        self.db_conn = None

    
    def connect_db(self, host: str, db_name: str, username: str, pword: str) -> bool:
        """Connect to the database at url and for username, and set the
        search_path to "air_travel". Return True iff the connection was made
        successfully.
        """
        try:
            self.db_conn = pg.connect(host=host, dbname=db_name, user=username, password=pword,
                                      options="-c search_path=air_travel")
        except pg.Error:
            return False

        return True

    def disconnect_db(self) -> bool:
        """Return True iff the connection to the database was closed
        successfully.
        """
        try:
            self.db_conn.close()
        except pg.Error:
            return False

        return True

    # ----------------------- Airline-related methods ------------------------- */

    def book_seat(self, pass_id: int, flight_id: int, seat_class: str) -> Optional[bool]:
        """Attempts to book a flight for a passenger in a particular seat class. 
        Does so by inserting a row into the Booking table.

        Parameters:
        * pass_id - id of the passenger
        * flight_id - id of the flight
        * seat_class - the class of the seat

        Precondition:
        * seat_class is one of "economy", "business", or "first".
        
        Return: 
        * True iff the booking was successful.
        * False iff the seat can't be booked, or if the passenger or flight cannot be found.
        """
        try:
            # TODO: Complete this method.
            pass
        except pg.Error:
            return None


    def upgrade(self, flight_id: int) -> Optional[int]:
        """Attempts to upgrade overbooked economy passengers to business class
        or first class (in that order until each seat class is filled).
        Does so by altering the database records for the bookings such that the
        seat and seat_class are updated if an upgrade can be processed.
        
        Upgrades should happen in order of earliest booking timestamp first.
        If economy passengers are left over without a seat (i.e. not enough higher class seats), 
        remove their bookings from the database.
        
        Parameters:
        * flight_id - the flight to upgrade passengers in
        
        Precondition: 
        * flight_id exists in the database (a valid flight id).
        
        Return: 
        * The number of passengers upgraded.
        """
        try:
            # TODO: Complete this method.
            pass
        except pg.Error:
            return None


# ----------------------- Helper methods below  ------------------------- */
    

    # A helpful method for adding a timestamp to new bookings.
    def _get_current_timestamp(self):
        """Return a datetime object of the current time, formatted as required
        in our database.
        """
        return datetime.datetime.now().replace(microsecond=0)

# ----------------------- Testing code below  ------------------------- */

def output(self):
        """Print each tuple in the list (query)
        
        Keyword arguments:
        argument -- description
        Return: return_description
        """
        for item in self:
            print(item)

def sample_testing_function() -> None:
    f1 = Airline()
    # TODO: Change this to connect to your own database:
    print(f1.connect_db("localhost", "airline", "fionyvan", ""))
    # TODO: Test one or more methods here.
    cur=f1.db_conn.cursor()
    cur.execute("""SELECT * FROM airline;""")
    query = cur.fetchall()
    output(query)
    print(f1.disconnect_db())

def test_booking():
    pass


if __name__ == '__main__':
    # Put your testing code here
    sample_testing_function()




