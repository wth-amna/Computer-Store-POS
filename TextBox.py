import pygame
from pygame.math import Vector2 as vec
from pygame import font

class TextBox:
    def __init__(self, x, y, width, height, bgColour=(128, 128, 128), activeColour=(200, 200, 200), static=False, 
                 text="", textSize = 16, textColour=(0, 0, 0), border=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.pos = vec(x, y)
        self.size = vec(width, height)

        self.rect = pygame.Rect(0, 0, width, height)
        
        self.isActive = False
        self.static = static

        self.text = text
        self.textSize = textSize
        self.textColour = textColour
        self.textPos = (10, 10)
        self.textCenterY = False

        self.border = border

        self.isPassword = False
        self.passwordText = ""

        self.font = font.Font("Assets/Roboto.ttf", textSize)
        # self.font = font.SysFont("Arial", textSize)

        if bgColour:
            self.image = pygame.Surface((width, height))
            self.bgColour = bgColour
            self.activeColour = activeColour
        else:
            self.image = pygame.Surface((width, height), pygame.SRCALPHA)
            self.bgColour = (0, 0, 0, 0)
            self.activeColour = (0, 0, 0, 0)


    def Draw(self, screen):
        if not self.static and self.isActive:
            self.image.fill(self.activeColour)
            if self.border:
                pygame.draw.rect(self.image, self.activeColour, self.rect,  2, 3)
            self.RenderText(self.image)
        else:
            self.image.fill(self.bgColour)
            if self.border:
                pygame.draw.rect(self.image, self.activeColour, self.rect,  2, 3)
            self.RenderText(self.image)
        screen.blit(self.image, self.pos)
    
    def MouseUp(self, pos):
        pass

    def CheckInside(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                self.isActive = True
            else:
                self.isActive =  False
        else:
            self.isActive = False
    
    def EditText(self, letter):
        try:
            if self.isPassword:
                key = chr(letter)
                if key.isalpha() or key.isdigit():
                    self.text += "*"
                    self.passwordText += key
                elif letter == 8:
                    self.text = self.text[:-1]
                    self.passwordText = self.passwordText[:-1]
                elif letter == 32:
                    self.text += "*"
                    self.passwordText += " "
            else:
                key = chr(letter)
                if key.isalpha() or key.isdigit():
                    self.text += key
                elif letter == 8:
                    self.text = self.text[:-1]
                elif letter == 32:
                    self.text += " "
        except ValueError:
            pass

    def RenderText(self, surface):
        text = self.font.render(self.text, False, self.textColour)
        if self.textCenterY:
            self.textPos = (10, self.height/2 - text.get_height()/2)
        # print(text.get_width())
        surface.blit(text, self.textPos)

    def CenterTextY(self):
        self.textCenterY = True