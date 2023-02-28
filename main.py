from card import Card
from seat import Seat
from user import User

from flask import Flask, render_template
from wtforms import Form, StringField, SubmitField
from flask.views import MethodView

app = Flask(__name__)


class HomePage(MethodView):

    def get(self):
        return render_template('index.html')


class BookingPage(MethodView):

    def get(self):
        #Get the form from UserForm class
        user_form = UserForm()
        #define the variable nam userform in render_templete
        #to use in html file
        return render_template('booking.html', userform=user_form)

class UserForm(Form):
    name = StringField("Name")
    seat = StringField("Seat Number")
    card_type = StringField("Card Type")
    card_number = StringField("Card Number")
    card_cvc = StringField("Card Cvc Number")
    card_holder = StringField("Card Holder Name")
    button = SubmitField("Get Ticket!")

app.add_url_rule('/', view_func=HomePage.as_view("home_page"))
app.add_url_rule('/booking', view_func=BookingPage.as_view("booking_page"))
app.run(host='0.0.0.0', port='8000', debug=True)

# if __name__ == "__main__":
#     name = input("Your Full Name: ")
#     seat_id = input("Preferred seat number: ")
#     card_type = input("Your card type: ")
#     card_number = input("Your card number: ")
#     card_cvc = input("Your card cvc: ")
#     card_holder = input("Card holder name: ")
#
#     user = User(name=name)
#     seat = Seat(seat_id=seat_id)
#     card = Card(type=card_type,
#                 number=card_number,
#                 cvc=card_cvc,
#                 holder=card_holder)
#
#     print(user.buy(seat=seat, card=card))
