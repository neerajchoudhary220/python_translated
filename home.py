from filescount import count
import os,time
total_line = count.fileName('main.txt')
tmp = open('tmp.txt','a',encoding='utf8')
value =''
with open('main.txt', 'r', encoding='utf8') as f:
    lines = f.readlines()
    i = 0
    with open('main.txt','w',encoding='utf8') as f1:
        if total_line>=10:      
            for line in lines:
                    lines[i]=''
                    value+= line.strip()+"\n"
                    if i == 9:
                            break
                    i += 1
            f1.writelines(lines)
        else:
            for line in lines:
                    lines[i]=''
                    value+= line.strip()+"\n"
            f1.writelines(lines)

tmp.write(value)
total_line = count.fileName('main.txt')
print("Total Line:",total_line)
if total_line != 1:
    os.system('python home.py')
