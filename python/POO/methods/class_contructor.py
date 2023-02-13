class Account():

    def __init__(self, number, holder, balance, limit):
        print("Construindo objeto")
        self.numero = number
        self.titular = holder
        self.saldo = balance
        self.limite = limit
    
    def extract(self):
        print("You have {}".format(self.saldo))
    
    def deposit(self, value):
        self.saldo += value
    
    def withdraw(self, value):
        self.saldo -= value

    
# self serve como apontador

class Date:

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
    
    def print_date(self):
        print("{}/{}/{}".format(self.day, self.month, self.year))