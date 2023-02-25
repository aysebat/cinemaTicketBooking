import sqlite3


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
                """, [balance - price, self.number, self.cvc])
                connection.commit()
                connection.close()
                return True
