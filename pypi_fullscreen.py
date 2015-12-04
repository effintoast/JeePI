import pygame, sys, time, pygame.gfxdraw
import RPi.GPIO as GPIO
from pygame.locals import *
from pypi_settings import *
from pypi_buttons import *


pygame.init()

#setup window size
window_canvas = pygame.display.set_mode((Settings.WINDOW_WIDTH, Settings.WINDOW_HEIGHT), pygame.FULLSCREEN, 32)
pygame.display.set_caption(Settings.CAPTION)
pygame.display.update()

clock = pygame.time.Clock()

GPIO.setmode(GPIO.BCM)

#our main menu options
menu_options = Settings.MENU_OPTIONS
toggle_buttons = Settings.TOGGLE_BUTTONS
momentary_button = False

for key,data in enumerate(toggle_buttons):
	for key,data in enumerate(toggle_buttons[data]):
		if 'pin' in data:
			GPIO.setup(data['pin'], GPIO.OUT)
			GPIO.output(data['pin'], GPIO.HIGH)
			
for key, data in menu_options.iteritems():
	menu_options[key] = { 'title': menu_options[key], 'button': MenuOption(), 'active': 0}

#change data on toggle button
def update_button(key, attr, value, section=None):
	if section == None:
		section = Settings.CURRENT_PANE
	toggle_buttons[section][key][attr] = value

#function for updating pin state
def set_pin_state(pin,state):
	print "Pin "+str(pin)+" state "+str(state)
	if state == 1:
		GPIO.output(pin, GPIO.HIGH)
	else:
		GPIO.output(pin, GPIO.LOW)
	#raspi pin change code here.

#button function for standard pin toggle
def toggle_pin(key, data):

	#TODO: CLEAN THIS UP
	#this is a little messy
	if data['toggle_off_id']:
		for toggle_id in data['toggle_off_id']:
			toggle_off_key = get_button_key_by_id(toggle_id)
			toggle_off_button = get_button_by_id(toggle_id)
			if toggle_off_button['active'] == 1:
				update_button(toggle_off_key, 'pin_state', 0)
				update_button(toggle_off_key, 'active', 0)
				set_pin_state(toggle_off_button['pin'],0)
				time.sleep(.2)

			
	if data['pin_state'] == 0:
		update_button(key, 'pin_state', 1)
		update_button(key, 'active', 1)
		set_pin_state(data['pin'],1)
	else:
		update_button(key, 'pin_state', 0)
		update_button(key, 'active', 0)
		set_pin_state(data['pin'],0)
	draw_buttons()

#button function for momentary pin toggle
def momentary_pin(key, data):

	global momentary_button
	
	#TODO: CLEAN THIS UP
	#this is a little messy
	if data['toggle_off_id']:
		for toggle_id in data['toggle_off_id']:
			toggle_off_key = get_button_key_by_id(toggle_id)
			toggle_off_button = get_button_by_id(toggle_id)
			if toggle_off_button['active'] == 1:
				update_button(toggle_off_key, 'pin_state', 0)
				update_button(toggle_off_key, 'active', 0)
				set_pin_state(toggle_off_button['pin'],0)
				time.sleep(.2)

	if data['pin_state'] == 0:
		update_button(key, 'pin_state', 1)
		update_button(key, 'active', 1)
		set_pin_state(data['pin'],1)
		momentary_button = key
	else:
		update_button(key, 'pin_state', 0)
		update_button(key, 'active', 0)
		set_pin_state(data['pin'],0)
	draw_buttons()

def get_button_key_by_id(id):
	for key,data in enumerate(toggle_buttons[Settings.CURRENT_PANE]):
		if data['id'] == id:
			return key;
	return 0;
	
def get_button_by_id(id):
	for key,data in enumerate(toggle_buttons[Settings.CURRENT_PANE]):
		if data['id'] == id:
			return data;
	return {};
	
#update all lights status
def toggle_lights(key, data):

	if data['toggle_state'] == 0:
		update_button(key, 'toggle_state', 1)
		toggle_state = 1
	else:
		update_button(key, 'toggle_state', 0)
		toggle_state = 0
		
	if 'lights' in toggle_buttons:
		for lkey,ldata in enumerate(toggle_buttons['lights']):
			if ldata['func'] == 'toggle_pin':
				update_button(lkey, 'active', toggle_state, 'lights')
				update_button(lkey, 'pin_state', toggle_state, 'lights')
				set_pin_state(ldata['pin'], toggle_state)
				
	update_button(key, 'active', 1)
	draw_buttons()
	time.sleep(.2)
	update_button(key, 'active', 0)
	draw_buttons()

#handles drawing of main menu
def draw_menu():
	start = 1
	for key, data in menu_options.iteritems():
		menu_color = Settings.MENU_COLOR
		if key == Settings.CURRENT_PANE:
			menu_options[key]['active'] = 1
		else:
			menu_options[key]['active'] = 0
		menu_options[key]['button'].create(window_canvas, 40, 50+(start*70), menu_options[key]['title'], menu_options[key])
		start = start+1
	pygame.display.flip()

#draw function for right buttons
def draw_buttons():
	top_offset = 25
	left_offset = Settings.LEFT_PANE_WIDTH + 25
	right_cols = 3
	i = 1
	if Settings.CURRENT_PANE in toggle_buttons:
		for key,data in enumerate(toggle_buttons[Settings.CURRENT_PANE]):
			temp_left_offset = 0;
			tmp_bg_color = Settings.BUTTON_BG_COLOR
			tmp_text_color = Settings.BUTTON_TEXT_COLOR
			if i > 1:
				temp_left_offset = (155+25) * (i - 1)

			toggle_buttons[Settings.CURRENT_PANE][key]['button'] = ButtonOption()
			toggle_buttons[Settings.CURRENT_PANE][key]['button'].create(window_canvas, (left_offset+temp_left_offset), top_offset, toggle_buttons[Settings.CURRENT_PANE][key]['title'], toggle_buttons[Settings.CURRENT_PANE][key])
			i = i + 1;
			if i > right_cols:
				i = 1
				top_offset = top_offset+135;
		pygame.display.flip()
	
#clears right pane, and draws menu
def setup_pane():
	window_canvas.fill(Settings.BG_COLOR)
	pygame.draw.rect(window_canvas, (44,44,44), (0, 0, 226, 481))
	pygame.draw.rect(window_canvas, Settings.LEFT_PANE_BG_COLOR, (0, 0, 225, 480))
	draw_menu()
	pygame.display.flip()


#initial run
setup_pane()
draw_buttons()

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == MOUSEBUTTONDOWN:
			#loop to see if menu item clicked
			for key, data in menu_options.iteritems():
				if data['button'].pressed(pygame.mouse.get_pos()):
					Settings.CURRENT_PANE = key
					setup_pane()
					draw_buttons()
			#loop to see if any toggle buttons are clicked
			if Settings.CURRENT_PANE in toggle_buttons:
				for key,data in enumerate(toggle_buttons[Settings.CURRENT_PANE]):
					if data['button'].pressed(pygame.mouse.get_pos()):
						#execute button function and pass button info
						globals()[data['func']](key,data)
		elif event.type == MOUSEBUTTONUP:
			if momentary_button != False:
				toggle_key = momentary_button
				toggle_data = toggle_buttons[Settings.CURRENT_PANE][toggle_key]
				toggle_pin(toggle_key, toggle_data)
				momentary_button = False
	clock.tick(30)
