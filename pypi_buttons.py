import pygame,pygame.gfxdraw

from pypi_settings import Settings

pygame.init()

class MenuOption:

	def create(self, surface, x, y, text, button):
		text_color = Settings.MENU_COLOR
		tmpFont = pygame.font.SysFont(Settings.FONT, Settings.MENU_TEXT_SIZE)
		tmpText = tmpFont.render(text, 1, text_color)
	
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

class ButtonOption

	def create(self, surface, x, y, text, button):
		text_color = Settings.BUTTON_TEXT_COLOR
		bg_color = Settings.BUTTON_BG_COLOR
		tmpFont = pygame.font.SysFont(Settings.FONT, Settings.BUTTON_TEXT_SIZE)
		tmpText = tmpFont.render(text, 1, text_color)
		
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