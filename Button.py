from typing import Text
from TextBox import TextBox
from pygame.math import Vector2 as vec


class Button(TextBox):
    def __init__(self, x, y, width, height, onClick, bgColour=(128, 128, 128), activeColour=(200, 200, 200), 
                 text="", textSize = 16, textColour=(0, 0, 0), ):
        super().__init__(x, y, width, height, bgColour=bgColour, activeColour=activeColour, static=False, text=text, textSize=textSize, textColour=textColour, border=True)
        self.onClick = onClick

    def MouseUp(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                self.isActive = False
                self.onClick()
        else:
            self.isActive = False

    def EditText(self, letter):
        pass

    def RenderText(self, surface):
        text = self.font.render(self.text, False, self.textColour)
        # print(text.get_width())
        surface.blit(text, (self.width/2 - text.get_width()/2, self.height/2 - text.get_height()/2))