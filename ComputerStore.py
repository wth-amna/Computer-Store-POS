from os import system
from time import strftime
from User import User
from ItemsManager import Items


class Shop:
    def __init__(self):
        self.items = Items()
        self.shoppingCart = []
        self.currentUser = None
        self.loggedIn = False

    def StartProgram(self):
        system("cls")
        print("WELCOME TO GALAXY.PK")
        print("1. Login/SignUp\n2. Browse items\n3. View Cart\n4. Check Out\n5. Exit")
        if not self.loggedIn:
            userIn = input("Please login/signup to proceed: ")
            if userIn == "5":
                return
            while not self.loggedIn and userIn != "1":
                print("Error! You must be logged in.")
                userIn = input("Press 1 to login/signup: ")
                if userIn == "5":
                    return
        else:
            userIn = input("Select an option: ")
            while userIn not in "12345":
                print("Invalid Response!")
                print("Please enter from the list or 5 to exit.")
                userIn = input("Select an option: ")
        if userIn == "1":
            self.LoginSignup()
        elif userIn == "2":
            self.items.DisplayItems()
            self.items.AddItemsToCart(self, self.shoppingCart)
        elif userIn == "3":
            self.DisplayCart()
        elif userIn == "4":
            self.CheckOut()
        elif userIn == "5":
            self.Exit()

    def LoginSignup(self):
        system("cls")
        currentUser = ""
        print("1. Login\n2. Sign Up")
        login_signup = input("Select an option or type esc to exit: ")
        while login_signup not in ("1", "2", "esc"):
            print("Invalid Response!")
            print("Please enter from the list.")
            login_signup = input("Select an option: ")

        if login_signup == "1":

            username = input("Enter your username: ")
            while username not in User.userDatabase:
                print("That user does not exist. Try again or type esc to exit.")
                username = input("Enter your username: ")
                if username == "esc":
                    self.LoginSignup()

            password = input("Enter your password: ")
            while password != User.userDatabase[username]:
                print("That password is incorrect! Try again.")
                password = input("Enter your password: ")
            currentUser = User.userDatabase[username]
            print("Success!")

        elif login_signup == "2":
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            currentUser = User(username, password)
            print("Success!")

        self.currentUser = currentUser
        self.loggedIn = True
        self.StartProgram()

    def DisplayCart(self):
        system("cls")
        print("You have the following items in your cart:")
        itemDisplay = ""
        for index, item in enumerate(self.shoppingCart, 1):
            itemDisplay += f"{index}. {item}\n"
        print(itemDisplay)
        input("press esc to go back: ")
        self.StartProgram()

    def CheckOut(self):
        system("cls")
        print("===============RECEIPT===============\n"
              "User: {}\n"
              "Date: {}         Time: {}\n"
              "_____________________________________".format(self.currentUser.username4, strftime("%d/%m/%y"),
                                                             strftime("%I:%M %p")))
        print("{0:27} {1:7}".format("ITEM", "PRICE"))
        total = 0
        for item in self.shoppingCart:
            price = self.items.GetPrice(item)
            total += price
            print("{0:27} {1:7}".format(item, "Rs." + str(price)))
        print("_____________________________________\n"
              "Total Amount:              {:8}".format("|Rs." + str(total)))
        input("press esc to exit: ")

    def Exit(self):
        User.StoreUsers()
