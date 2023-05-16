from TextBox import TextBox

class Item:
    def __init__(self, name, price, quantity, description="") -> None:
        self.name = name
        self.price = price
        self.quantity = quantity
        self.description = description

    def ShowItem(self):
        itemName = TextBox(50, 200, 500, 50, text=self.name, textSize=20, textColour=(255, 255, 255), static=True, border=True)
        itemName.CenterTextY()
        
        itemPrice = TextBox(550, 200, 100, 50, text=f"${self.price}", textSize=20, textColour=(255, 255, 255), static=True, border=True)
        itemPrice.CenterTextY()

        itemDescription = TextBox(50, 250, 400, 35, text=self.description, textSize=14, textColour=(255, 255, 255), static=True, border=True)
        itemDescription.CenterTextY()

        itemQuantity = TextBox(550, 250, 100, 35, text=f"x{self.quantity}", textSize=14, textColour=(255, 255, 255), static=True, border=True)
        itemQuantity.CenterTextY()

        return [itemName, itemPrice, itemDescription, itemQuantity]