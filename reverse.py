from audioop import reverse
from filescount import count
def reverseLine(inputFile):
    f = open(inputFile,'r',encoding='utf8')
    lines = f.readlines()
    total_lines = count.fileName(inputFile)
    values =''
    for x in reversed(range(total_lines-1)):
        values+= lines[x]

    return values
inputFile = input("Enter input file name:")
outputFile = input("Enter output file:")
open(outputFile,'a',encoding='utf8').write(reverseLine(inputFile))
print("done")
