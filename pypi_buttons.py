import pygame,pygame.gfxdraw

from pygame.locals import *
from pypi_settings import Settings

pygame.init()

class MenuOption:

	def create(self, surface, x, y, text, button):
		text_color = Settings.MENU_COLOR
		if button['active'] == 1:
			text_color = Settings.MENU_COLOR_ACTIVE
		tmpFont = pygame.font.SysFont(Settings.FONT, Settings.MENU_TEXT_SIZE)
		tmpText = tmpFont.render(text, 1, text_color)
		surface.blit(tmpText, ((200-tmpText.get_width()),y))
		self.rect = pygame.Rect((200-tmpText.get_width()),y, tmpText.get_width(),tmpText.get_height())
		
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

class ButtonOption:

	def create(self, surface, x, y, text, button):
		text_color = Settings.BUTTON_TEXT_COLOR
		bg_color = Settings.BUTTON_BG_COLOR
		if 'active' in button:
			if button['active'] == 1:
				text_color = Settings.BUTTON_TEXT_COLOR_ACTIVE
				bg_color = Settings.BUTTON_BG_COLOR_ACTIVE
		tmpFont = pygame.font.SysFont(Settings.FONT, Settings.BUTTON_TEXT_SIZE)
		tmpText = tmpFont.render(text, 1, text_color)
		button_height = 110
		button_width = 155
		pygame.draw.rect(surface, bg_color, (x,y, button_width, button_height))
		surface.blit(tmpText, ((button_width/2)-(tmpText.get_width()/2) + x,(button_height/2)-(tmpText.get_height()/2) + y))
		self.rect = pygame.Rect(x,y,button_width,button_height)
		
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