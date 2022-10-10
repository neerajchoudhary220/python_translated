import json
from web import chrome
from mykeyboard import keyboards
from splittxt import split
import clipboard

with open('translate.json') as f:
    translate = json.load(f)

filefortranslate ='main.txt'
words = split.FileToSplit.SplitLineByLine(filefortranslate)
url = translate['translation']['eng_to_arabic']
chrome.myweb.openUrl(url)
keyboards.AutKeyPress.GoogleTransLateLeftSideCopy(words)
translated_data = clipboard.paste()
split.FileToSplit.WriteTranslatedFile(filefortranslate,translated_data)




