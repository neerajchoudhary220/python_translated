from filescount import count
import os
import time
total_line = count.fileName('main.txt')
tmp = open('tmp.txt', 'a', encoding='utf8')
value = ''
f1 = open('main.txt','w',encoding='utf8')
with open('main.txt', 'r', encoding='utf8') as f:
    lines = f.readlines()
    i = 0
# if total_line >= 10:
for line in lines:
    value = line.strip()+"\n"
    tmp.write(value)
print(lines)
# f1.writelines(lines)
# else:
#     for line in lines:
#         lines[i]=''
#         value+= line.strip()+"\n"

#     with open('main.txt','w',encoding='utf8') as f1:
#         if total_line>=10:      
#             for line in lines:
#                     value= line.strip()+"\n"
#                     tmp.write(lines[i])
#                     lines[i]=''
#                     if i == 9:
#                             break
#                     i += 1
#             f1.writelines(lines)
#         else:
#             for line in lines:
#                     lines[i]=''
#                     value+= line.strip()+"\n"
#             f1.writelines(lines)
# # value = list(value.split("\n"))
# # print(sorted(value))
# tmp.write(sorted(value))
# total_line = count.fileName('main.txt')
# print("Total Line:",total_line)
# if total_line != 1:
#     os.system('python home.py')
