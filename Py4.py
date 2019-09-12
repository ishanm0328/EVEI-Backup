import time
import serial
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import keyboard

def waitSeconds(seconds):
    last_time = time.time()
    while time.time()-last_time < 2:
        if keyboard.is_pressed('a'): #if key 'a' is pressed 
            print('You Pressed A Key!')
            return True
            break #finishing the loop
        else:
            pass
    return False

def readport(filename,r):
    ser = serial.Serial(
        port='COM6',\
        baudrate=9600,\
        parity=serial.PARITY_NONE,\
        stopbits=serial.STOPBITS_ONE,\
        bytesize=serial.EIGHTBITS,\
            timeout=0)

    print("connected to: " + ser.portstr)
    count=1
    line = []
    number = ''
    st = ''
    count = 0
    var1 = []
    var2 = []
    var3 = []
    var4 = []
    var5 = []
    var6 = []
    var7 = []

    f = open(filename, 'w')

    plt.ion() ## Note this correction
    fig=plt.figure()


    axes = plt.gca()
    axes.set_ylim([-20,20])

    x = [0]

    # You probably won't need this if you're embedding things in a tkinter plot...
    ##plt.ion()

    ##fig = plt.figure()
    ##ax = fig.add_subplot(111)
    ##line1, = ax.plot((np.array([1,2,3,4,5]), var7, 'r-'))
    xr = []
    xx = []
    xy = []
    xz = []
    xe = []
    

    while True:
        for c in ser.readline():
            #chrlist = [chr(line[i]) for i in range(0, len(line))]
            #print(chr(c))
            if chr(c) == '.' or chr(c) == '+' or chr(c) =='-' or chr(c) =='0' or chr(c) =='1' or chr(c) =='2' or chr(c) =='3' or chr(c) =='4' or chr(c) =='5' or chr(c) =='6' or chr(c) =='7' or chr(c) =='8' or chr(c) =='9':
                number = number + chr(c)
                #print(number)
            elif number!='':
                line.append(float(number))
                f.write(number)
##                print(number)
                f.write(",")
                count=count+1
                #break
                if st == "þEM":
                    count = 1
                    f.write('\n')
##                    print(st, len(st))
                
                if count == 1:
                    var1.append(float(number))
                elif count == 2:
                    var2.append(float(number))
                elif count == 3:
                    var3.append(float(number))
                elif count == 4:
                    var4.append(float(number))
                elif count == 5:
                    var5.append(float(number))
                elif count == 6:
                    var6.append(float(number))
                elif count == 7:
                    var7.append(float(number))
                    count = 0
##                    f.write("\n")
                number = ''
                st = chr(c)
            else:
                st = st + chr(c)

        vr = var2
        ve = var5
        vx = var6
        vy = var7
        vz = var1


        for x in range(0,len(var2),1):
            xr.append(x)
        if len(var2) > r:
            vr = var2[-r:]
            xr = xr[-r:]

        for x in range(0,len(var5),1):
            xe.append(x)
        if len(var5) > r:
            ve = var5[-r:]
            xe = xe[-r:]
        
        for x in range(0,len(var6),1):
            xx.append(x)
        if len(var6) > r:
            vx = var6[-r:]
            xx = xx[-r:]
            
        for x in range(0,len(var7),1):
            xy.append(x)
        if len(var7) > r:
            vy = var7[-r:]
            xy = xy[-r:]
            
        for x in range(0,len(var1),1):
            xz.append(x)
        if len(var1) > r:
            vz = var1[-r:]
            xz = xz[-r:]
            
        
        plt.figure(1)
        plt.subplot(322)
        plt.cla()
        plt.gca().set_ylim([-20,20])
        plt.plot(xx,vx, 'r')
        plt.ylabel('x acc in ms^-2')
        plt.xlabel('time in sec')
        plt.title('x acc in red')
        
        
        plt.subplot(324)
        plt.cla()
        plt.gca().set_ylim([-20,20])
        plt.plot(xy,vy, 'b')
        plt.ylabel('y acc in ms^-2')
        plt.xlabel('time in sec')
        plt.title(' y acc in blue')
        
        
        plt.subplot(326)
        plt.cla()
        plt.gca().set_ylim([-20,20])
        plt.plot(xz,vz, 'g')
        plt.ylabel('z acc in ms^-2')
        plt.xlabel('time in sec')
        plt.title(' z acc in green')

        plt.subplot(323)
        plt.cla()
        plt.plot(xe,ve,'y')
        plt.ylabel('energy in kJ')
        plt.xlabel('time in seconds')
        plt.title('Energy vs Time')

        plt.subplot(321)
        plt.cla()
        plt.plot(xr,vr)
        plt.ylabel('rpm')
        plt.xlabel('time in seconds')
        plt.title('RPM vs time')

        
        plt.show
        plt.pause(0.0001)


    ##    time.sleep(2)
        
        
        pressed = waitSeconds(2)

        xr = []
        xe = []
        xx = []
        
        xy = []
        xz = []

        if keyboard.is_pressed('a') or pressed==True: #if key 'a' is pressed 
            print('You Pressed A Key!')
            break #finishing the loop
        else:
            pass
        #break
    ser.close()
    f.close()
    plt.close('all')


readport("data1.csv",10)
 
