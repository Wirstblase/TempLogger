import datetime
import matplotlib.pyplot as plt
from time import sleep
import os

def savePlot():
    x = []
    y = []
    yfl = []
    today = str(datetime.datetime.now().strftime(" %d/%m/%Y"))

    file1 = str(__file__)
    file2 = file1.replace("tempplotter.py","")

    x_file = open((file2 + "time.dat"),"r")
    x = x_file.read().split(',')
    x_file.close()

    y_file = open((file2 + "temp.dat"),"r")
    y = y_file.read().split(',')
    y_file.close()

    if(len(x) != len(y)):
        print("file item count error!")

    for i in y:
        yfl.append(float(i))

    plt.figure(figsize=(18,8))

    plt.plot(x,yfl)
    plt.xlabel('time', color='#1e8bc3')
    plt.ylabel('temperature (°C)', color='#e74c3c')
    plt.title(('living room temp'+today), color='#34495e')


    #plt.show()
    day = str(datetime.datetime.now().strftime("%d"))
    year = str(datetime.datetime.now().strftime("%Y"))
    month = str(datetime.datetime.now().strftime("%m"))
    fileformat = ".pdf"
    savepath = file2 + year + "\\" + month + "\\" + day + fileformat
    plt.savefig(savepath)

print("welcome! temp plotting started (plots at the end of each day)")

while True:
    now = datetime.datetime.now()
    hour = now.strftime("%H")
    minute = now.strftime("%M")
    #print("hour:"+hour+" minute:"+minute)

    if(hour == "23"):
        if(minute == "58"):
            savePlot()
            print("plot saved on:"+str(now))

    sleep(10)


    
