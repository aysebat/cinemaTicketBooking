import random
import string

class User:

    def __init__(self, name):
        self.name = name

    def buy(self, seat, card):
        pass

class Seat:

    databasev = "cinema.db"

    def __init__(self, seat_id):
        self.seat_id = seat_id

    def get_price(self):
        pass

    def is_free(self):
        pass

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
        pass

class Ticket:

    def __init__(self, seat_id, user, price):
        self.seat_id = seat_id
        self.user = user
        self.price = price


