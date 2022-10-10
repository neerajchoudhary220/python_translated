from base64 import encode
import os
from datetime import datetime
from fnmatch import translate
class FileToSplit:
    def SplitLineByLine(fileName):
        f = open(fileName)
        lines = f.readlines()
        x, values = 1,''
        for line in lines:
            values += line.split('=>', x)[1]    
        return values
    def WriteTranslatedFile(fileName,translated_data):
        temp_file = open('temp.txt','w',encoding='utf8')
        temp_file = temp_file.write(translated_data)
        translateFileName = datetime.now().strftime('%d-%m-%y_%H_%M_%S')+'_translated.txt'
        translated_file = open(translateFileName,'a',encoding='utf8')
        with open(fileName,'r') as f1:
            lines = f1.readlines()
        x,keys,i =1,'',0
        for line in lines:
            keys = line.split('=>', x)[0]+'=>'
            with open('temp.txt','r',encoding='utf8') as translated_val:
                translated_values = translated_val.readlines()[i]
                translated_file.write(keys+' '+translated_values)
            i=i+2
        translated_file.close()
        os.remove('temp.txt')
        print("done")




        
