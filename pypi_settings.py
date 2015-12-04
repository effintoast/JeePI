class Settings:
	#screen / pane 
	CAPTION = 'PyPi Auto'
	FONT = 'Calibri'
	BG_COLOR = (20, 20, 20)
	LEFT_PANE_BG_COLOR = (8, 8, 8)
	LEFT_PANE_WIDTH = 225
	WINDOW_WIDTH = 800
	WINDOW_HEIGHT = 480
	
	#MENU
	MENU_TEXT_SIZE = 30
	MENU_COLOR = (87,87,87)
	MENU_COLOR_ACTIVE = (255,255,255)
	
	#buttons
	BUTTON_TEXT_COLOR = (255,255,255)
	BUTTON_BG_COLOR = (0,0,0)
	BUTTON_TEXT_COLOR_ACTIVE = (8, 8, 8)
	BUTTON_BG_COLOR_ACTIVE = (255,255,255)
	BUTTON_TEXT_SIZE = 22
	
	#landing
	CURRENT_PANE = 'lights'
	
	TOGGLE_BUTTONS = {
		'lights': [
			{'title': 'TOP LIGHTS', 'func': 'toggle_pin', 'pin': 04, 'pin_state': 0, 'active': 0},
			{'title': 'REAR LIGHTS', 'func': 'toggle_pin', 'pin': 17, 'pin_state': 0, 'active': 0},
			{'title': 'BUMPER LIGHTS', 'func': 'toggle_pin', 'pin': 27, 'pin_state': 0, 'active': 0},
			{'title': 'CABIN LIGHTS', 'func': 'toggle_pin', 'pin': 22, 'pin_state': 0, 'active': 0},
			{'title': 'TOGGLE ALL', 'func': 'toggle_lights', 'toggle_state': 0, 'active': 0}
			],
		'winch': [
			{'title': 'WINCH OUT', 'func': 'toggle_pin', 'pin': 05, 'pin_state': 0, 'active': 0, 'id': 'winch_out', 'toggle_off_id': ['winch_in']},
			{'title': 'WINCH IN', 'func': 'toggle_pin', 'pin': 06, 'pin_state': 0, 'active': 0, 'id': 'winch_in', 'toggle_off_id': ['winch_out']},
			{'title': 'WINCH OUT +', 'func': 'momentary_pin', 'pin': 05, 'pin_state': 0, 'active': 0, 'toggle_off_id': ['winch_out','winch_in']},
			{'title': 'WINCH IN -', 'func': 'momentary_pin', 'pin': 06, 'pin_state': 0, 'active': 0, 'toggle_off_id': ['winch_out','winch_in']}
			],
		'settings': [
			{'title': 'EXIT', 'func': 'close_app', 'pin_state': 0, 'active': 0},
			]
		}
		
	MENU_OPTIONS = {'lights': 'LIGHTS', 'winch': 'WINCH', 'settings': 'SETTINGS'};