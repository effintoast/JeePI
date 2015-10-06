import pygame, sys, Buttons, time
from pygame.locals import *

pygame.init()

#settings
BG_COLOR = (20, 20, 20)
LEFT_PANE_BG_COLOR = (8, 8, 8)
LEFT_PANE_WIDTH = 225
S_WIDTH = 800
S_HEIGHT = 480
MENU_COLOR = (87,87,87)
MENU_COLOR_ACTIVE = (255,255,255)
BUTTON_BG_COLOR = (0,0,0)

#setup canvas
windowCanvas = pygame.display.set_mode((S_WIDTH, S_HEIGHT), 0, 32)
pygame.display.set_caption('PyPi Auto')

#send it.
pygame.display.update()
clock = pygame.time.Clock()

#our main menu options
menuOptions = {'lights': 'LIGHTS', 'winch': 'WINCH', 'settings': 'SETTINGS'};
toggleButtons = {
	'lights': [
		{'title': 'TOP LIGHTS', 'toggleIO': 21},
		{'title': 'REAR LIGHTS', 'toggleIO': 22},
		{'title': 'BUMPER LIGHTS', 'toggleIO': 24},
		{'title': 'CABIN LIGHTS', 'toggleIO': 26}
		],
	'winch': [
		{'title': 'WINCH OUT', 'toggleIO': 27},
		{'title': 'WINCH IN', 'toggleIO': 28}
		]
	}

#landing page option
currentPane = 'lights'

for key, title in menuOptions.iteritems():
	menuOptions[key] = [ menuOptions[key],Buttons.MenuOption()]

def drawToggleButtons(targetButton=None):
	topOffset = 25
	leftOffset = LEFT_PANE_WIDTH + 25
	rightCols = 3
	i = 1
	key  = currentPane
	if key in toggleButtons:
		for keyb,data in enumerate(toggleButtons[key]):
			tempLeftOffset = 0;
			tmpBGColor = BUTTON_BG_COLOR
			tmpTxtColor = MENU_COLOR_ACTIVE
			if i > 1:
				tempLeftOffset = (155+25) * (i - 1)
			if targetButton == keyb:
				tmpBGColor = (255,255,255)
				tmpTxtColor = LEFT_PANE_BG_COLOR
			toggleButtons[key][keyb]['button'] = Buttons.ToggleOption()
			toggleButtons[key][keyb]['button'].create_button(windowCanvas, tmpBGColor, (leftOffset+tempLeftOffset), topOffset, toggleButtons[key][keyb]['title'], tmpTxtColor)
			#pygame.draw.rect(windowCanvas, (0,0,0), (leftOffset+tempLeftOffset,topOffset, 155, 110))
			
			i = i + 1;
			if i > rightCols:
				i = 1
				topOffset = topOffset+135;
		pygame.display.flip()
	
#setup right panel based on menu
def setupRightPane():
	clearRightPane()
	drawToggleButtons()
	pygame.display.flip()
	
#clear canvas and redraw menu
def clearRightPane():
	windowCanvas.fill(BG_COLOR)
	pygame.draw.rect(windowCanvas, LEFT_PANE_BG_COLOR, (0, 0, 225, 480))
	updateMainMenu()
	pygame.display.flip()

#for menu redraw
def updateMainMenu():
	start = 1
	for key, title in menuOptions.iteritems():
		menuColor = MENU_COLOR
		if key == currentPane:
			menuColor = MENU_COLOR_ACTIVE
		menuOptions[key][1].create_button(windowCanvas, LEFT_PANE_BG_COLOR, 40, 50+(start*70), menuOptions[key][0], menuColor)
		start = start+1
	pygame.display.flip()

#initial page load
setupRightPane()

# loop?
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == MOUSEBUTTONDOWN:
			for key, title in menuOptions.iteritems():
				if menuOptions[key][1].pressed(pygame.mouse.get_pos()):
					currentPane = key
					setupRightPane()
			if currentPane in toggleButtons:
				for key,data in enumerate(toggleButtons[currentPane]):
					if toggleButtons[currentPane][key]['button'].pressed(pygame.mouse.get_pos()):
						print toggleButtons[currentPane][key]['title']+'- pin '+str(toggleButtons[currentPane][key]['toggleIO']);
						#redraw to show button was clicked
						drawToggleButtons(key)
						time.sleep(.2)
						drawToggleButtons()
	clock.tick(15)