import webbrowser
import time
import pyautogui
import clipboard
from pynput.keyboard import Key, Controller



# key_f = open('english_keys.txt','r',encoding="utf8")
values_f = open('english_values.txt',encoding="utf8")

# keys = key_f.readlines()
values = values_f.readlines()

tf = open('tranlated.txt','a',encoding="utf8")
chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"+" %s"
url = 'https://translate.google.com/?hl=en&sl=en&tl=ar&op=translate'
webbrowser.get(chrome_path).open(url)
pyautogui.click(525, 638)

Keyboard = Controller()
def translation(keyline,word):
   
    time.sleep(2)
    Keyboard.type(word)

    time.sleep(4)
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
  
    data = clipboard.paste()
    tf.write(keyline+''+data+"\n")
    time.sleep(2)
    with Keyboard.pressed(Key.shift):
        Keyboard.press(Key.tab)
        Keyboard.release(Key.tab)
    
    with Keyboard.pressed(Key.shift):
        Keyboard.press(Key.tab)
        Keyboard.release(Key.tab)

    with Keyboard.pressed(Key.shift):
        Keyboard.press(Key.tab)
        Keyboard.release(Key.tab)
    with Keyboard.pressed(Key.shift):
        Keyboard.press(Key.tab)
        Keyboard.release(Key.tab)
    with Keyboard.pressed(Key.shift):
        Keyboard.press(Key.tab)
        Keyboard.release(Key.tab)
    
    with Keyboard.pressed(Key.shift):
        Keyboard.press(Key.tab)
        Keyboard.release(Key.tab)

    with Keyboard.pressed(Key.shift):
        Keyboard.press(Key.tab)
        Keyboard.release(Key.tab)


    Keyboard.press(Key.enter)
    Keyboard.release(Key.enter)

x=0
for valueline in values:
        time.sleep(2)
        with open('english_keys.txt', 'r') as fp:
            keys = fp.readlines()[x]
        translation(keys,valueline.strip())
        x=x+1



# print(data)
