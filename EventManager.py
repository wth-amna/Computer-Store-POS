import pygame.event as pyEvent
from pygame.constants import KEYDOWN, MOUSEBUTTONDOWN, MOUSEBUTTONUP
from pygame import mouse
from pygame import QUIT
from pygame import quit


class EventHandler:
    "Handles all events inside the program."

    def HandleEvents(self, textBoxes):
        for event in pyEvent.get():
            if event.type == QUIT:
                quit()
                exit()
            if event.type == MOUSEBUTTONDOWN:
                for textBox in textBoxes:
                    if not textBox.static:
                        textBox.CheckInside(mouse.get_pos())
            if event.type == MOUSEBUTTONUP:
                for textBox in textBoxes:
                    if not textBox.static:
                        textBox.MouseUp(mouse.get_pos())
            if event.type == KEYDOWN:
                for textBox in textBoxes:
                    if textBox.isActive:
                        textBox.EditText(event.key)