from translate import Translator
translator= Translator(from_lang="english",to_lang="hindi")
# translation = 

translated = open('translatedfile.txt','a',encoding='utf8')
with open('main.txt', 'r', encoding='utf8') as f:
    lines = f.readlines()
for line in lines:
    value = line.strip()+"\n"
    trns =translator.translate(value)
    translated.write(trns+"\n")
