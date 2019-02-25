from dasher import Dasher
from mileage import Mileage

class Menu:

    def __init__(self):
        self.loop = True
        self.init = False
        self.mile_init = False

    def print_menu(self):
        print (30 * "-" , "MENU", 30 * "-")
        print ("1. Dash Info Init")
        print ("2. Milage/Gas Info Init")
        print ("3. Display Tips Made")
        print ("4. Display Calculated Minimum Pay")
        print ("5. Display Dash Info")
        print ("6: Display Gallons of Gas Used")
        print ("7. Display Cost of Gas Used")
        print ("8. Display Amount of Gas purchased")
        print ("9. Display net income gain of Dash")
        print ("10. Exit")

        print (67 * "-")
        print (1 * "\n") 
        
    def menu_loop(self):
        menu = Menu()
        error_message = "Dasher info not initiated, select 1  to initiate"
        mile_message = "Mileage info not initiated, select 2 to initate"

        while self.loop:
            choice = input("Enter your choice: ")

            if choice == "1":
                print ("Initiating Dash Information...")
                dasher = Dasher()
                dasher.init_info()
                dasher.get_info()
                print("\n")
                menu.print_menu()
                self.init = True

            elif choice == "2":
                car = Mileage()
                car.init_info()
                self.mile_init = True
                menu.print_menu()             
                
            elif choice == "3":
                if self.init == True:
                    dasher.tips_made()
                else:
                    print(error_message)
                menu.print_menu()

            elif choice == "4":
                if self.init == True:
                    dasher.calc_min_pay()
                else:
                    print(error_message)
                menu.print_menu()

            elif choice == "5":
                if self.init == True:
                    dasher.get_info()
                else:
                    print(error_message)
                menu.print_menu()

            elif choice == "6":
                if self.mile_init == True:
                    car.calculate_gas_used()
                else:
                    print(mile_message)
                menu.print_menu()

            elif choice == "7":
                if self.mile_init == True:
                    car.gallons_used()
                else:
                    print(mile_message)
                menu.print_menu()
            
            elif choice == "8":
                if self.mile_init == True:
                    car.calculate_gallons_bought()
                else:
                    print(mile_message)
                menu.print_menu()

            elif choice == "9":
                if self.mile_init == True & self.init == True:
                    total_made = float(dasher.total_made) - float(car.amount_spent) 
                    print("Net income of this Dash: " + "%.2f" % total_made)
                else:
                    print(mile_message)
                menu.print_menu()


            elif choice == "10":
                print ("Exiting Menu...")
                self.loop = False
            else:
                input("Wrong option selected. Enter any key to try again: ")

