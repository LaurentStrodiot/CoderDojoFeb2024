import neopixel
from machine import Pin
from time import sleep

PixNum = 18
PixPin = 4
speed = 5

np=neopixel.NeoPixel(Pin(PixPin), PixNum)


def getRGB(deg): 							# translate HSV to RGB value (see https://www.youtube.com/watch?v=Qmm_sxpYIEc)

    m=1/60
    if deg>=0 and deg<60:
        R=1
        G=0
        B=m*deg
    if deg>=60 and deg<120:
        R=1-m*(deg-60)
        G=0
        B=1
    if deg>=120 and deg<180:
        R=0
        G=m*(deg-120)
        B=1
    if deg>=180 and deg<240:
        R=0
        G=1
        B=1-m*(deg-180)
    if deg>=240 and deg<300:
        R=m*(deg-240)
        G=1
        B=0
    if deg>=300 and deg<360:
        R=1
        G=1-m*(deg-300)
        B=0
    myColor=(int(R*50),int(G*50),int(B*50))
    return myColor


while True:
    for deg in range(0,360,speed): 			# to go around the HSV color wheel (0-360 deg)
        for j in range(0,18,1):				# to put the rainbow across the 18 pixels on the PCB
            value = deg+j*20				# each pixel is separted by 360/18 = 20 degrees
            if value>=360:					# if the value is above the max of 360 degrees, you come back to start
                value=value-360
            color=getRGB(value)				# call the function to convert HSV degree to RGB values (R, G, B)
            np[j]=color						# assign the color to the pixel
        np.write()							# push the buffer to the real pixels
        sleep(0.01) 						# wait 10 ms before moving to the next step
            
