from Item import Item
from typing import Text
from Button import Button
from TextBox import TextBox


DARKGREY = (50, 50, 50)
WHITE = (255, 255, 255)

def Back(GoBack):
    global backButton
    backButton = Button(10, 100, 50, 25, GoBack, bgColour=DARKGREY, text="Back", textSize=16, textColour=WHITE)


def State0(scrnWidth, scrnHeight, SignUpButton, LoginButton):
    signupButton = Button(scrnWidth/2 - 120, scrnHeight/2 - 50, 240, 50, SignUpButton, bgColour=DARKGREY, text="Sign Up", textSize=32, textColour=WHITE)
    loginButton = Button(scrnWidth/2 - 120, scrnHeight/2 + 50, 240, 50, LoginButton, bgColour=DARKGREY, text="Login", textSize=32, textColour=WHITE)
    return [loginButton, signupButton]

def State012(state, scrnWidth, scrnHeight, SignUpButton, LoginButton):
    username = TextBox(scrnWidth/2 - 150, scrnHeight/2 - 60, 150, 50, bgColour=None, text="Username", textSize=20, textColour=WHITE, static=True)
    username.CenterTextY()
    
    usernameInput = TextBox(scrnWidth/2, scrnHeight/2 - 60, 200, 50, textSize=20, textColour=WHITE, static=False)
    usernameInput.CenterTextY()
    
    password = TextBox(scrnWidth/2 - 150, scrnHeight/2, 150, 50, bgColour=None, text="Password", textSize=20, textColour=WHITE, static=True)
    password.CenterTextY()
    
    passwordInput = TextBox(scrnWidth/2, scrnHeight/2, 200, 50, textSize=20, textColour=WHITE, static=False)
    passwordInput.CenterTextY()
    passwordInput.isPassword = True
    
    if state == 0.1:
        signupButton = Button(scrnWidth/2 - 120, scrnHeight/2 + 100, 240, 50, SignUpButton, bgColour=DARKGREY, text="Sign Up", textSize=32, textColour=WHITE)
        return [username, usernameInput, password, passwordInput, signupButton, backButton]
    else:
        loginButton = Button(scrnWidth/2 - 120, scrnHeight/2 + 100, 240, 50, LoginButton, bgColour=DARKGREY, text="Login", textSize=32, textColour=WHITE)
        return [username, usernameInput, password, passwordInput, loginButton, backButton]

def State1(scrnWidth, scrnHeight, ShowCart, CheckOut):
    showCart = Button(scrnWidth/2 - 210, scrnHeight - 70, 200, 50, ShowCart, bgColour=DARKGREY, text="View Cart", textSize=32, textColour=WHITE)
    checkOut = Button(scrnWidth/2 + 10, scrnHeight - 70, 200, 50, CheckOut, bgColour=DARKGREY, text="Check Out", textSize=32, textColour=WHITE)
    
    welcome = TextBox(50, 140, 200, 50, text="Browse Items", textColour=WHITE, textSize=24, static=True, border=True)
    welcome.CenterTextY()

    item1 = Item("Zotac Nvidia RTX 3090", 1499, 5, "Boost Clock: 1.7GHz  VRAM: 24GB GDDR6X   384 Bit")
    item1Boxes = item1.ShowItem()

    return [showCart, checkOut, welcome] + item1Boxes

def State11():
    textBox1 = TextBox(50, 140, 400, 50, text="You have the following items in your cart.", textSize=20, textColour=WHITE, static=True, border=True)
    return [backButton, textBox1]

def State2(scrnWidth, scrnHeight, ExitButton):
    exitButton = Button(scrnWidth/2 - 100, scrnHeight - 70, 200, 50, ExitButton, bgColour=DARKGREY, text="Exit", textSize=32, textColour=WHITE)
    return [exitButton]
