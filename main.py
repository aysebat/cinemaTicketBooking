import random
import sqlite3
import string

from fpdf import FPDF


class User:

    def __init__(self, name):
        self.name = name

    def buy(self, seat, card):
        """ Buys teh ticket if the card is valid and the seat is free"""
        if seat.is_free():
            if card.validate(price=seat.get_price()):
                seat.occupy()
                ticket = Ticket(user=self.name, price=seat.get_price(), seat_number=seat_id)
                ticket.to_pdf()
                return "Your payment successful"

            else:
                return "There was a problem with your card"
        else:
            return "Seat is taken"


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


class Card:
    database = "banking.db"

    def __init__(self, type, number, cvc, holder):
        self.type = type
        self.number = number
        self.cvc = cvc
        self.holder = holder

    def validate(self, price):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        cursor.execute("""
        SELECT "balance" FROM "Card" WHERE "number" = ? and "cvc" =?
        """, [self.number, self.cvc])
        result = cursor.fetchall()[0][0]
        print(result)

        if result:
            balance = result
            print(balance)
            if balance >= price:
                connection.execute("""
                UPDATE "CARD" SET "balance" =?  WHERE "number" = ? and "cvc" =?
                """, [balance - result, self.number, self.cvc])
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
        "Create a pdf ticket"
        pdf = FPDF(orientation='p', unit='pt', format='A4')
        pdf.add_page()

        pdf.set_font(family='Times', style='B', size=24)
        pdf.cell(w=0, h=80, txt="Your Digital Ticket", border=1, ln=1, align='C')

        pdf.set_font(family='Times', style='B', size=14)
        pdf.cell(w=100, h=25, txt="Name: ", border=1)
        pdf.set_font(family='Times', style='', size=12)
        pdf.cell(w=0, h=25, txt=self.user, border=1, ln=1)
        pdf.cell(w=0, h=5, txt="", border=0, ln=1)

        pdf.set_font(family='Times', style='B', size=14)
        pdf.cell(w=100, h=25, txt="Price: ", border=1)
        pdf.set_font(family='Times', style="", size=12)
        pdf.cell(w=0, h=25, txt=str(self.price), border=1, ln=1)
        pdf.cell(w=0, h=5, txt="", border=0, ln=1)

        pdf.set_font(family='Times', style='B', size=14)
        pdf.cell(w=100, h=25, txt="Seat Number: ", border=1)
        pdf.set_font(family='Times', style="", size=12)
        pdf.cell(w=0, h=25, txt=str(self.seat_number), border=1, ln=1)
        pdf.cell(w=0, h=5, txt="", border=0, ln=1)

        pdf.output("sample.pdf", "F")


if __name__ == "__main__":
    name = input("Your Full Name: ")
    seat_id = input("Preferred seat number: ")
    card_type = input("Your card type: ")
    card_number = input("Your card number: ")
    card_cvc = input("Your card cvc: ")
    card_holder = input("Card holder name: ")

    user = User(name=name)
    seat = Seat(seat_id=seat_id)
    card = Card(type=card_type,
                number=card_number,
                cvc=card_cvc,
                holder=card_holder)

    print(user.buy(seat=seat, card=card))
