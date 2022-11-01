import csv
import matplotlib.pyplot as plt
from tkinter import *
import os.path
import numpy as np
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
    t = 10
    n = t*12
    for i in reversed(range(0, 99)):
        v3Path = r'C:\Users\User\Desktop\271022\script\AI_16' + str(i) + '.csv'
        fileExistsChecking = path.exists(v3Path)
        if fileExistsChecking == True:
            with open('AI_16' + str(i) + '.csv') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter = ';')
                v3array = []
                v3arrayTime = []
                v3arrayValue = []
                for row in csv_reader:
                    if row[0] == 'Sensors\AI-16.VALUE.4_PC20004':
                        v3array.append(row)
                for v3row in v3array:
                    v3arrayTime.append(v3row[1])
                    v3arrayValue.append(v3row[2])

                #print(v3array)
                
                reversedv3arrayTime = list(reversed(v3arrayTime))
                v3arrayTimeSorted = reversedv3arrayTime[:-n-1:-1]
                reversedv3arrayValue = list(reversed(v3arrayValue))
                v3arrayValueSorted = reversedv3arrayValue[:-n-1:-1]
                plt.title('AI-16.VALUE.3 | График за последние ' + str(t) + ' мин', fontsize = 12)
                #plt.figure(figsize=(8, 6))
                plt.xlabel('Time', fontsize = 10)
                plt.ylabel('Value', fontsize = 10)
                plt.plot(v3arrayTime[0:100], v3arrayValue[0:100])
                plt.xticks(rotation = 45)
                plt.yticks(np.arange(0, 8.0, step=0.5))
                plt.grid(True)
                plt.show()
            break

def v3DateChoice():
    v3btnDate = Button(Tk(), text = 'Показать график за последние 10 мин', command = v3showLast10min)
    v3btnDate.pack()
    
v3btn = Button(Tk(), text = 'AI-16.VALUE.3', command = v3DateChoice)
v3btn.pack()
    
