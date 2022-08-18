import os, time, serial
import datetime

serialPort = serial.Serial(port = "COM4", baudrate=115200,
                           bytesize=8, timeout=200, stopbits=serial.STOPBITS_ONE)

hour = ""
previousHour = "06" # make this show the actual previous hour of the current time
# implemented = false !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

averageList = []
average = 0.00

# every time this program starts it should check if temp file and hour file
# have the same amount of items inside of them, and equalize it
# in order to avoid errors
#
# implemented = false

# every time this program starts it should also check if the date modified
# of the hour file and temp file is the same as today's date, and if not
# it should call resetFiles(), otherwise erronated data from the past could leak
# into the f u t u r e
#
# implemented = false

file1 = str(__file__)
file2 = file1.replace("templogger.py","")


def resetFiles():
    print("reset files")
    open((file2 + "time.dat"), 'w').close()
    open((file2 + "temp.dat"), 'w').close()


def appendHour(hourr):
    isEmpty = 0
    if(os.path.getsize((file2 + "time.dat"))) == 0:
        isEmpty = 1
    
    print("append time")
    timefile = open((file2 + "time.dat"),'a')
    if(isEmpty == 0):
        timefile.write(",")
    timefile.write(str(hourr))
    timefile.close()


def appendTemp(tempp):
    isEmpty = 0
    if(os.path.getsize((file2 + "temp.dat"))) == 0:
        isEmpty = 1
    
    print("append temp")
    tempfile = open((file2 + "temp.dat"),'a')
    if(isEmpty == 0):
        tempfile.write(",")
    tempfile.write(str(tempp))
    tempfile.close()

print("welcome! temp logging started")

while True:
    #os.system("cls")
    s = serialPort.readline().decode() #this makes the whole code wait until new msg
    s1 = s.replace(" ", "")
    s = s1
    #print(s)

    if(s == "sensor disconnected"):
        print("sensor disconnected! check hardware and wiring")
    else:

        currentTemp = float(s)
        #print("current temp: "+str(currentTemp))
        averageList.append(currentTemp)
        #print(averageList)
        
        average = 0.00
        for i in averageList:
            average = average+i
        average = average / len(averageList)
        average1 = round(average,1)
        print("number of temp values for current hour: " + str(len(averageList)))
        print("average: " + str(average) + " rounded:" + str(average1))
        
    now = datetime.datetime.now()
    hour = str(now.strftime("%H"))
    minute = str(now.strftime("%M"))


    if(minute == "01" ): 
        if(hour != previousHour):
            #new hour, write current average to file and reset average counter
            print("new hour!")
            appendTemp(average1)
            appendHour(previousHour)
            previousHour = hour
            averageList = []

    if(minute == "01"):
        if(hour == "00"):
            os.system("cls")
            print("new day!")
            resetFiles()
            
    time.sleep(30) #redundant

