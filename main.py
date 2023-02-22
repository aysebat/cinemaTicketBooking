import random
import sqlite3
import string

class User:

    def __init__(self, name):
        self.name = name

    def buy(self, seat, card):
        pass

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
        #0: indicate the seat is not taken so it is free
        if result == 0:
            return True
        else:
            return False

    def occupt(self):
        pass

class Card:

    database = "banking.db"

    def __init__(self, type, number, csv, holder):
        self.type = type
        self.number = number
        self.csv = csv
        self.holder = holder

    def validate(self):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        cursor.execute("""
        SELECT "balance" FROM "Card" WHERE "number" = ? and "cvc" =?
        """, [self.number, self.cvc])
        result = cursor.fetchall()

        if result:
            balance = result[0][0]
            if balance >= result:
                connection.execute("""
                UPDATE "CARD" SET "balance" =?  WHERE "number" = ? and "cvc" =?
                """, [balance-result, self.number, self.cvc])
                connection.commit()
                connection.close()
                return True

class Ticket:

    def __init__(self, user, price, seat_number):
        self.user = user
        self.price = price
        self.id = "".join([random.choice(string.ascii_letters) for i in range(8)])
        self.seat_number = seat_number

    def to_pdf(self):
        pass



