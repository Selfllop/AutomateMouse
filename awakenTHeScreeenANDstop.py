import pyautogui as py
import time
from pynput import keyboard

py.FAILSAFE = False

# Flag to stop the loop
keep_running = True

# Function to handle key press events
def on_press(key):
    global keep_running
    if key == keyboard.Key.esc:
        print('Escape key pressed. Stopping loop.')
        keep_running = False
        return False

def run():
    # Start the listener to monitor for key presses
    with keyboard.Listener(on_press=on_press) as listener:
        print("Program running...")
        try:
            # Loop until the 'esc' key is pressed
            while keep_running:
                time.sleep(30)
                for i in range(0, 100):
                    py.moveTo(0, i * 5)
                    if not keep_running:
                        break
                for i in range(0, 3):
                    py.press('shift')
                    if not keep_running:
                        break
                time.sleep(0.1)
        except Exception as e:
            print("An error occurred:", e)
        finally:
            print("Program stopped.")
            listener.stop()

run()
