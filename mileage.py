from dasher import Dasher

class Mileage:

    def __init__(self):
        print("Making Mileage Object...")
        self.miles = 0.00
        self.price_of_gas = 0.00
        self.mpg = 0.00
        self.amount_spent = 0.00
        self.amount_used = 0.00
        self.gallons_spent = 0.00

    def init_info(self):
        self.miles = input("Enter number of miles driven: ")
        self.price_of_gas = input("Enter price of gas per gallon: ")
        self.mpg = input("Enter car's MPG: ")
        self.amount_spent = input("Enter amount spent on gas: ")

    def calculate_gas_used(self):
        self.gallons_spent = (float(self.miles) / float(self.mpg))
        print("Gallons of gas used: " + "%.2f" % self.gallons_spent)

    def gallons_used(self):
        self.amount_used = (float(self.price_of_gas) * float(self.gallons_spent))
        print("Amount of gas money actually used: " + "%.2f" % self.amount_used)

    def calculate_gallons_bought(self):
        bought = (float(self.amount_spent) / float(self.price_of_gas))
        print("Amount of gas purchashed in gallons: " + "%.2f" % bought)


