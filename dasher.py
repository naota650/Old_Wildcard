class Dasher:
    def __init__(self):
        print("Making Dasher Object...")
        self.dashes = 0
        self.pay_per_dash = 6.00
        self.total_made = 0
        self.surge_bonus = 0
        self.min_pay = 0
        
    def init_info(self):
        self.dashes = input("Enter number of dashes: ")
        while int(self.dashes) < 1:
            self.dashes = input("Enter number of dashes: (at least 1) : ")
        
        self.miles = input("Enter number of miles: ")
        while int(self.miles) < 1:
            self.miles = input("Enter number of miles: (at least 1) : ")

        self.total_made = input("Enter total made during dash: ")
        while int(self.total_made) < (int(self.pay_per_dash) * int(self.dashes)):
            self.total_made = input("Enter total made during dash: (at least 6 per delivery) : ")
        
        self.surge_bonus = input("Enter surge bonus if exists: ")
        while int(self.surge_bonus) < 0:
            self.surge_bonus = input("Enter surge bonus if exists: (cannot be negative) : ")

    def get_info(self):
        print("Number of Dashes : " + str(self.dashes))
        print("Number of Miles : " + str(self.miles))
        print("Total Made during Dash: " + str(self.total_made))
        print("Surge Bonus : " + str(self.surge_bonus))

    def calc_min_pay(self):
        self.min_pay = (float(self.pay_per_dash) + float(self.surge_bonus)) * int(self.dashes)
        print("Minimum Pay: " + "%.2f" % self.min_pay)
        
    def tips_made(self):
        tips = float(self.total_made) - ((float(self.pay_per_dash) + float(self.surge_bonus)) * int(self.dashes))
        print("Tips Made: " + "%.2f" % tips)
