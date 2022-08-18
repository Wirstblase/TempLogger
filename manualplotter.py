import datetime
import matplotlib.pyplot as plt
from time import sleep

def savePlot():
    x = []
    y = []
    today = str(datetime.datetime.now().strftime(" %d/%m/%Y"))

    file1 = str(__file__)
    file2 = file1.replace("manualplotter.py","")

    x_file = open((file2 + "time.dat"),"r")
    x = x_file.read().split(',')
    x_file.close()

    y_file = open((file2 + "temp.dat"),"r")
    y = y_file.read().split(',')
    y_file.close()

    if(len(x) != len(y)):
        print("file item count error!")

    plt.figure(figsize=(18,8))

    plt.plot(x,y)
    plt.xlabel('time', color='#1e8bc3')
    plt.ylabel('temperature (°C)', color='#e74c3c')
    plt.title(('living room temp'+today), color='#34495e')

    plt.show()



savePlot()
