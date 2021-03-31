import os
import re

file = open(input('Enter File name: '), 'r')
fileName, extension = os.path.splitext(file.name)
minifiedFile = open(f'{fileName}.min{extension}', 'w+')
minifiedContent = ""

for line in file:
    minifiedContent += line.strip()
    minifiedContent = minifiedContent.replace(' ', '')

minifiedFile.write(minifiedContent)
print('Minified The file')
minifiedFile.close()
