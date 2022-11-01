import csv
from re import T
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk
import os.path
import numpy as np
from os import path
from tkcalendar import Calendar

scaleTemperature0to100 = np.arange(0, 110, step = 5)

def displayLastChosen():
    t = input('Показать график за (в мин): ')
    n = int(t) * 11
    for i in reversed(range(0, 99)):
        filePath = r'C:\Users\User\Desktop\271022\script\011122\Первичная пастеризация' + str(i) + '.csv'
        fileExists = path.exists(filePath)
        if fileExists == True:
            with open('Первичная пастеризация' + str(i) + '.csv') as csvFile:
                csvReader = csv.reader(csvFile, delimiter = ';')
                array = []
                arrayTime = []
                arrayValue = []
                for row in csvReader:
                    if row[0] == 'Sensors\AI-2.VALUE.10_PB1TT60':
                        array.append(row)
                for row in array:
                    arrayTime.append(row[1])
                    arrayValue.append(row[2])

                #arrayRevensed = list(reversed(array))
                #arrayRevensedPeroid = arrayRevensed[:n]
                #arrayRevensedBack = list(reversed(arrayRevensedPeroid))
                #print(arrayRevensedBack)
                
                arrayTimeRevensed = list(reversed(arrayTime))
                arrayTimeRevensedPeroid = arrayTimeRevensed[:n]
                arrayTimeRevensedBack = list(reversed(arrayTimeRevensedPeroid))

                arrayValueRevensed = list(reversed(arrayValue))
                arrayValueRevensedPeroid = arrayValueRevensed[:n]
                arrayValueRevensedBack = list(reversed(arrayValueRevensedPeroid))

                floatedValueArray = []
                for tofloat in arrayValueRevensedBack:
                    floated =  float(tofloat.replace(",", "."))
                    floatedValueArray.append(floated)

                plt.title('PB1TT60 | График за последние ' + str(t) + ' мин', fontsize = 12)
                #plt.figure(figsize=(8, 6))
                plt.xlabel('Time', fontsize = 10)
                plt.ylabel('Value', fontsize = 10)
                plt.plot(arrayTimeRevensedBack, floatedValueArray)
                plt.xticks(rotation = 45)
                plt.yticks(scaleTemperature0to100)
                plt.grid(True)
                periodArray = []
                for i in range(0, n, 11*100):
                    periodArray.append(i)
                plt.xticks(periodArray)
                plt.show()
            break

def dateChoice():
    dateChoiceWindow = Tk()

    dateChoiceWindow.title("Выберите период времени")
    dateChoiceWindow.geometry("250x200") 

    btnChosen = Button(dateChoiceWindow, text = 'Показать n мин', command = displayLastChosen)
    btnChosen.pack()

def sensorChoice():
    window = Tk()
    window.title("Выберите датчик")
    window.geometry("250x200") 

    btnPP = Button(window, text = 'PB1TT60', command = dateChoice)
    btnPP.pack()

def areaChoice():
    window = Tk()
    window.title("Выберите вкладку")
    window.geometry("250x200") 

    btn = Button(window, text = 'Первичная пастеризация', command = sensorChoice)
    btn.pack()
    window.mainloop()

areaChoice()
