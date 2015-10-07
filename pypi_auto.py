import pygame, sys, time, pygame.gfxdraw

from pypi_settings import *
from pypi_buttons import *


pygame.init()

#setup window size
windowCanvas = pygame.display.set_mode((Settings.WINDOW_WIDTH, Settings.WINDOW_HEIGHT), 0, 32)
pygame.display.set_caption(Settings.CAPTION)
pygame.display.update()

clock = pygame.time.Clock()


#our main menu options
menuOptions = {'lights': 'LIGHTS', 'winch': 'WINCH', 'settings': 'SETTINGS'};
toggleButtons = {
	'lights': [
		{'title': 'TOP LIGHTS', 'toggleIO': 21, 'status': 0},
		{'title': 'REAR LIGHTS', 'toggleIO': 22, 'status': 0},
		{'title': 'BUMPER LIGHTS', 'toggleIO': 24, 'status': 0},
		{'title': 'CABIN LIGHTS', 'toggleIO': 26, 'status': 0},
		{'title': 'TOGGLE ALL', 'toggleIO': 'sys', 'func': 'toggleAll'}
		],
	'winch': [
		{'title': 'WINCH OUT', 'toggleIO': 27, 'status': 0},
		{'title': 'WINCH IN', 'toggleIO': 28, 'status': 0}
		]
	}
	
for key, title in menuOptions.iteritems():
	menuOptions[key] = { 'title': menuOptions[key], 'button': Buttons.MenuOption()}
	
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == MOUSEBUTTONDOWN:
			print 'mouse'
	clock.tick(15)