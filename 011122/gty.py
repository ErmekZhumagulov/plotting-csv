import csv
from re import T
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk
import os.path
import numpy as np
from os import path
from tkcalendar import Calendar
import datetime

#unchangable
today = datetime.date.today()

#changable
scaleTemperature0to100 = np.arange(0, 110, step = 5)

def defDateBegin():
    window = Tk()
    window.geometry("400x400")
    cal = Calendar(window, selectmode = 'day', year = today.year, month = today.month, day = today.day, date_pattern = 'dd.mm.y')
    cal.pack(pady = 20)
    
    def dateBegin():
        date.config(text = "от: " + cal.get_date())
        
    Button(window, text = "Выбрать начало", command = lambda: [dateBegin(), defDateEnd()]).pack(pady = 20)
    date = Label(window, text = "")
    date.pack(pady = 20)

    def defDateEnd():
        window = Tk()
        window.geometry("400x400")
        cal = Calendar(window, selectmode = 'day', year = today.year, month = today.month, day = today.day, date_pattern = 'dd.mm.y')
        cal.pack(pady = 20)
        def dateEnd():
            date.config(text = "до: " + cal.get_date())
            
            for i in range(0, 99):
                filePath = r'C:\Users\User\Desktop\271022\script\011122\Первичная пастеризация' + str(i) + '.csv'
                fileExists = path.exists(filePath)
                if fileExists == True:
                    with open('Первичная пастеризация' + str(i) + '.csv') as csvFile:
                        csvReader = csv.reader(csvFile, delimiter = ';')
                        array = []
                        arrayTime = []
                        arrayValue = []
                        arrayTimeCut = []
                        for row in csvReader:
                            if row[0] == 'Sensors\AI-2.VALUE.10_PB1TT60':
                                array.append(row)
                        for row in array:
                            arrayTime.append(row[1])
                            arrayValue.append(row[2])

                        for i in arrayTime:
                            if cal.get_date() in i:
                                arrayTimeCut.append(i)
                            else:
                                print("next step -----------------------------")
                                break
                        print(arrayTimeCut)
                #else:
                #    break
        Button(window, text = "Выбрать конец", command = dateEnd).pack(pady = 20)
        date = Label(window, text = "")
        date.pack(pady = 20)
        window.mainloop()

    window.mainloop()

defDateBegin()
