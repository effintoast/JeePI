#Buttons Modified version of http://pygame.org/project-Button+drawer-2541-.html
import pygame
from pygame.locals import *
pygame.init()

class MenuOption:
    def create_button(self, surface, color, x, y, text, text_color):
        global test;
        myFont = pygame.font.SysFont("Calibri", 30)
        myText = myFont.render(text, 1, text_color)
        surface.blit(myText, ((200-myText.get_width()),y))
        self.rect = pygame.Rect((200-myText.get_width()),y, myText.get_width(),myText.get_height())
        return surface



    def pressed(self, mouse):
        if mouse[0] > self.rect.topleft[0]:
            if mouse[1] > self.rect.topleft[1]:
                if mouse[0] < self.rect.bottomright[0]:
                    if mouse[1] < self.rect.bottomright[1]:
                        return True
                    else: return False
                else: return False
            else: return False
        else: return False

		
class ToggleOption:
    def create_button(self, surface, color, x, y, text, text_color):
        global test;
        myFont = pygame.font.SysFont("Calibri", 22)
        myText = myFont.render(text, 1, text_color)
        buttonHeight = 110
        buttonWidth = 155
        pygame.draw.rect(surface, color, (x,y, buttonWidth, buttonHeight))
        surface.blit(myText, ((buttonWidth/2)-(myText.get_width()/2) + x,(buttonHeight/2)-(myText.get_height()/2) + y))
        self.rect = pygame.Rect(x,y,buttonWidth,buttonHeight)
        return surface



    def pressed(self, mouse):
        if mouse[0] > self.rect.topleft[0]:
            if mouse[1] > self.rect.topleft[1]:
                if mouse[0] < self.rect.bottomright[0]:
                    if mouse[1] < self.rect.bottomright[1]:
                        return True
                    else: return False
                else: return False
            else: return False
        else: return False
