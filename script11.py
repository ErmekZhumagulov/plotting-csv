import csv
import matplotlib.pyplot as plt
from tkinter import *
import os.path
import numpy as np
from os import path

t = 10
n = t * 11
for i in reversed(range(0, 99)):
    v3Path = r'D:\work\pepsico-scripts\work-scripts-py\Первичная пастеризация' + str(i) + '.csv'
    fileExistsChecking = path.exists(v3Path)
    if fileExistsChecking == True:
        with open('Первичная пастеризация' + str(i) + '.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter = ';')
            v3array = []
            v3arrayTime = []
            v3arrayValue = []
            for row in csv_reader:
                if row[0] == 'Sensors\AI-2.VALUE.10_PB1TT60':
                    v3array.append(row)
            for v3row in v3array:
                v3arrayTime.append(v3row[1])
                v3arrayValue.append(v3row[2])
            # v3arrayRevensed = list(reversed(v3array))
            # v3arrayRevensedPeroid = v3arrayRevensed[:n]
            # v3arrayDRevensed = list(reversed(v3arrayRevensedPeroid))
            # print(v3arrayDRevensed)
            v3arrayTimeRevensed = list(reversed(v3arrayTime))
            v3arrayTimeRevensedPeroid = v3arrayTimeRevensed[:n]
            v3arrayTimeDRevensed = list(reversed(v3arrayTimeRevensedPeroid))

            v3arrayValueRevensed = list(reversed(v3arrayValue))
            v3arrayValueRevensedPeroid = v3arrayValueRevensed[:n]
            v3arrayValueDRevensed = list(reversed(v3arrayValueRevensedPeroid))

            floatedValueArray = []
            for tofloat in v3arrayValueDRevensed:
                floated =  float(tofloat.replace(",", "."))
                floatedValueArray.append(floated)

            plt.title('PB1TT60 | График за последние ' + str(t) + ' мин', fontsize = 12)
            #plt.figure(figsize=(8, 6))
            plt.xlabel('Time', fontsize = 10)
            plt.ylabel('Value', fontsize = 10)
            plt.plot(v3arrayTimeDRevensed, floatedValueArray)
            plt.xticks(rotation = 45)
            plt.yticks(np.arange(25, 35, step = 1))
            plt.grid(True)
            periodArray = []
            for i in range(0, n, 11):
                periodArray.append(i)
            plt.xticks(periodArray)
            plt.show()
        break
