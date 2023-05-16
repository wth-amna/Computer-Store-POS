from os import system

class Items:
    itemsDict = {"Computers": 150000, "Laptops": 200000, "Smartphone Accessories": 300}
    itemsList = ["Computers", "Laptops", "Smartphone Accessories"]
    itemDisplay = ""

    def DisplayItems(self):
        system("cls")
        print("We have the following parts in stock:")
        self.itemDisplay = ""
        for index, item in enumerate(self.itemsDict.keys(), 1):
            self.itemDisplay += f"{index}. {item}\n"
        print(self.itemDisplay)

    def AddItemsToCart(self, shop, cart):
        while True:
            userIn = input("What would you like to buy (press esc to exit): ")
            while userIn not in self.itemDisplay+"esc":
                print("Invalid Response!")
                print("Please enter from the list or type esc to exit.")
                userIn = input("What would you like to buy: ")
            if userIn == "esc":
                break
            item = self.itemsList[int(userIn) - 1]
            if item in cart:
                continue
            cart.append(item)
            print(item + " has been added to cart.")

        shop.StartProgram()

    def GetPrice(self, item):
        return self.itemsDict[item]
