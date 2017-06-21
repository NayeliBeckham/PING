from pynput import keyboard
from threading import Thread 
import sys

def on_release(key):
    if key == keyboard.Key.esc:
		# Stop listener
		isWorking = False
		print ("Exit ..................]\n\n")
		sys.exit(0)
		return False

t = Thread(target=do_work)
t.start()



# Collect events until released
with keyboard.Listener(on_release=on_release) as listener:
    listener.join()
