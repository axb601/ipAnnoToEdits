import os
import csv
import numpy as np
import pandas as pd

path = 'C:/Users/alexbirc/Desktop/ipAnnoToEdits/testCase/Kabilil-1_Annotations.txt'
#fileList = os.listdir(path)
casings = []
edits = []
#for file in path:
#code to transform Interative Petrophysics (IP) annotations export file format into IP Multi-Well Notes file format for loading back into IP or TGS FMB
with open(path, 'r') as inFile:
    #for each line in IP annotations export file format
    for line in inFile:
        #ignore first line in file
        if "Annotation set" in line:
            pass
        #a double quotation mark is an indicator that this line contains a casing depth comment - following code block takes that line and transforms data into desired format
        elif '""' in line:
            newLine = line.replace('"','')
            caseDepth = [i for i in newLine.split()][1]
            caseSize = [i for i in newLine.split()][14:]
            caseName = caseSize[0].rsplit(':',1)[1] + ' ' + ' '.join(caseSize[1:])
            caseText = caseName.casefold().replace(' casing','" casing') + ' @' + caseDepth.split('.')[0] + 'm'
            casings.append(caseText)
        elif '""' not in line:
            newLine = line.replace('"','')
            test = [i for i in newLine.split()][1]
print(casings)
print('Done')
