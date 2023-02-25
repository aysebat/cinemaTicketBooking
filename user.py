from main import seat_id
from ticket import Ticket


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
