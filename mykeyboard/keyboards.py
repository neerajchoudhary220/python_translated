from pynput.keyboard import Key, Controller
import pyautogui
import time
class AutKeyPress:
   def GoogleTransLateLeftSideCopy(word):
    pyautogui.click(525, 638)
    Keyboard = Controller()
    time.sleep(2)
    Keyboard.type(word)

    time.sleep(8)
    Keyboard.press(Key.tab)
    Keyboard.release(Key.tab)
    Keyboard.press(Key.tab)
    Keyboard.release(Key.tab)
    Keyboard.press(Key.tab)
    Keyboard.release(Key.tab)
    Keyboard.press(Key.tab)
    Keyboard.release(Key.tab)
    Keyboard.press(Key.tab)
    Keyboard.release(Key.tab)
    Keyboard.press(Key.tab)
    Keyboard.release(Key.tab)
    Keyboard.press(Key.tab)
    Keyboard.release(Key.tab)
    Keyboard.press(Key.tab)
    Keyboard.release(Key.tab)
    Keyboard.press(Key.enter)
    Keyboard.release(Key.enter)
    time.sleep(2)
    