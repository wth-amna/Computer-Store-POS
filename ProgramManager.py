from os import stat
import Layouts
from User import User
from TextBox import TextBox
from pygame import quit
from EventManager import EventHandler
from DisplayManager import DisplayManager


class ProgramManager:
    def __init__(self, scrn):
        global eventManager, displayManager, programState, topLabel, userLabel, scrnWidth, scrnHeight, layouts, itemsToDisplay
        
        screen = scrn

        self.loggedIn = False
        self.currentUser = User("", "")
        programState = 0

        eventManager = EventHandler()
        displayManager = DisplayManager(screen)

        scrnWidth, scrnHeight = scrn.get_size()

        topLabel = TextBox(scrnWidth/2 - 175, 30, 350, 60, bgColour=None, text="Computer Store", textSize=48, textColour=(255, 255, 255), static=True)
        userLabel = TextBox(5, 70, 100, 40, bgColour=None, text=f"User: {self.currentUser.username}", textSize=14, textColour=Layouts.WHITE, static=True, border=True)

        layouts = self.InitLayouts(programState)
        Layouts.Back(self.GoBack)

        itemsToDisplay = [topLabel, userLabel] + layouts
    
    def GoBack(self):
        self.ChangeState(int(str(programState)[0]))

    def SignUpButton(self):
        if programState == 0:
            self.ChangeState(0.1)
        else:
            print(0.1)
            with open("Assets/userData.txt", "a") as userData:
                userData.write(f"{layouts[1].text},{layouts[3].passwordText}\n")
            self.currentUser = User(layouts[1].text, layouts[3].passwordText)
            userLabel.text = f"User: {layouts[1].text}"
            self.ChangeState(1)

    def LoginButton(self):
        if programState == 0:
            self.ChangeState(0.2)
        else:
            userDict = {}
            with open("Assets/userData.txt", "r") as userData:
                users = userData.read().split("\n")
                for user in users:
                    if user:
                        user = user.split(",")
                        userDict[user[0]] = user[1]
            username = layouts[1].text
            password = layouts[3].passwordText
            try:
                if userDict[username] == password:
                    self.currentUser = User(username, password)
                    userLabel.text = f"User: {username}"
                    self.ChangeState(1)
                else:
                    self.ChangeState(programState)
            except KeyError:
                self.ChangeState(programState)

    def ShowCart(self):
        self.ChangeState(11)

    def CheckOut(self):
        print("Check out")

    def ExitButton(self):
        quit()
        exit()

    def ManageProgram(self):
        eventManager.HandleEvents(itemsToDisplay)
        displayManager.MainDisplay(itemsToDisplay)

    def InitLayouts(self, state):
        if state == 0:
            return Layouts.State0(scrnWidth, scrnHeight, self.SignUpButton, self.LoginButton)
        elif state == 0.1 or state == 0.2:
            return Layouts.State012(state, scrnWidth, scrnHeight, self.SignUpButton, self.LoginButton)
        elif state == 1:
            return Layouts.State1(scrnWidth, scrnHeight, self.ShowCart, self.CheckOut)
        elif state == 11:
            return Layouts.State11()
        elif state == 2:
            return Layouts.State2(scrnWidth, scrnHeight, self.ExitButton)

    def ChangeState(self, state):
        global programState, layouts, itemsToDisplay
        programState = state
        layouts = self.InitLayouts(programState)
        itemsToDisplay = [topLabel, userLabel] + layouts