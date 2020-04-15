import matplotlib.pyplot as plt
import numpy as np
import serial
import time
import math 

#(the following codes might have some changes before lab, please  view  codes on github as main code, thx)

t = np.arange(0,10,0.1)
x1 = np.arange(0,10,0.1) 
y1 = np.arange(0,10,0.1) 
z1 = np.arange(0,10,0.1)
tilt = np.arange(0,10,0.1)

serdev = '/dev/ttyACM0'
s = serial.Serial(serdev,115200)
for x in range(0, 100):
    line=s.readline() # Read an echo string from K66F terminated with '\n'
    # print line
    x1[x] = float(line)
    line=s.readline() 
    y1[x] = float(line)
    line=s.readline()
    z1[x] = float(line)
    line=s.readline()
    tilt[x] = float(line)

fig, ax = plt.subplots(2,1)
ax[0].plot(t,x1,'b')
ax[0].plot(t,y1,'r')
ax[0].plot(t,z1,'g')
ax[0].set_xlabel('Time')
ax[0].set_ylabel('Acc Vector')
ax[1].plot(t,tilt)
ax[1].set_xlabel('Time')
ax[1].set_ylabel('Tilt')
plt.show()
s.close()
