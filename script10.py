import csv
import matplotlib.pyplot as plt
from tkinter import *
import os.path
from os import path
        
def v3():
    with open('AI_160.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ';')
        v3array = []
        v3arrayTime = []
        v3arrayValue = []
        for row in csv_reader:
            if row[0] == 'Sensors\AI-16.VALUE.3':
                v3array.append(row)
        for v3rowTime in v3array:
            v3arrayTime.append(v3rowTime[1])
        for v3rowValue in v3array:
            v3arrayValue.append(v3rowValue[2])
        plt.plot(v3arrayTime, v3arrayValue)
        plt.show()

def v3showLast10min():
    n = 10
    for i in reversed(range(0, 99)):
        stringing = str(i)
        v3Path = 'D:\work\pepsico-scripts\work-scripts-py\AI_16' + stringing + '.csv'
        fileExistsChecking = path.exists(v3Path)
        if fileExistsChecking == True:
            stringing = str(i)
            with open('AI_16' + stringing + '.csv') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter = ';')
                v3array = []
                v3arrayTime = []
                v3arrayValue = []
                for row in csv_reader:
                    if row[0] == 'Sensors\AI-16.VALUE.3':
                        v3array.append(row)
                for v3row in v3array:
                    v3arrayTime.append(v3row[1])
                    v3arrayValue.append(v3row[2])
                v3arrayTimeSorted = v3arrayTime[:-n-1:-1]
                v3arrayValueSorted = v3arrayValue[:-n-1:-1]
                plt.plot(v3arrayTimeSorted, v3arrayValueSorted)
                plt.show()
            break

def v3DateChoice():
    v3btnDate = Button(Tk(), text = 'Показать график за последние 10 мин', command = v3showLast10min)
    v3btnDate.pack()
    
v3btn = Button(Tk(), text = 'AI-16.VALUE.3', command = v3DateChoice)
v3btn.pack()
    
