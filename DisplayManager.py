from pygame import Rect, display
from pygame import draw

class DisplayManager:
    "Manages everything that needs to be displayed onto the screen."
    def __init__(self, screen):
        self.screen = screen
    
    def MainDisplay(self, textBoxes):
        self.screen.fill((50,50,50))
        draw.rect(self.screen, (100, 100, 100), Rect(0, 0, self.screen.get_width(), 130))
        for textBox in textBoxes:
            textBox.Draw(self.screen)
        display.flip()
