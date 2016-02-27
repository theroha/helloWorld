#import dependencies
import pyxhook #required for hook
from pygame import midi	#required for midi

midi.init()

output = midi.Output(2)

def OnKeyPress(event):
	if event.Key == "Right": #Virtual Key Id of right arrow key
		output.write_short(0xc0, 0)
		
	if event.Ascii == 96:
		new_hook.cancel()

#instantiate HookManager class
new_hook=pyxhook.HookManager()
#listen to all keystrokes
new_hook.KeyDown=OnKeyPress
#hook the keyboard
new_hook.HookKeyboard()
#start the session
new_hook.start()
