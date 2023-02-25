import sqlite3


class Seat:
    database = "cinema.db"

    def __init__(self, seat_id):
        self.seat_id = seat_id

    def get_price(self):
        """Get the price for a certain seat"""
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        cursor.execute("""
        SELECT "price" FROM "Seat" WHERE "seat_id" = ?
        """, [self.seat_id])
        price = cursor.fetchall()[0][0]
        return price

    def is_free(self):
        """Check in database if the seat taken or not"""
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        cursor.execute("""
        SELECT "taken" FROM "Seat" WHERE "seat_id" = ?
        """, [self.seat_id])
        result = cursor.fetchall()[0][0]
        # 0: indicate the seat is not taken so it is free
        if result == 0:
            return True
        else:
            return False

    def occupy(self):
        connection = sqlite3.connect(self.database)
        connection.execute("""
        UPDATE "Seat" SET "taken" = ? WHERE "seat_id" = ?
        """, [1, self.seat_id])
        connection.commit()
        connection.close()
