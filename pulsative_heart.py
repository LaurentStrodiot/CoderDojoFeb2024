from machine import Pin
from neopixel import NeoPixel
from time import sleep

color=[(50,0,0),(0,50,0),(0,0,50)]
select = 0


# NeoPixel( broche_signal, nbre_de_led )
np = NeoPixel(Pin(4), 18)

def button_Pressed(change):
    global select
    select +=1
    if select>2:
        select=0


button = Pin(2, Pin.IN, Pin.PULL_UP)

button.irq(handler=button_Pressed, trigger=Pin.IRQ_FALLING)


while True:
                
    for i in range(0,50):
        a,b,c=color[select]
        np.fill((int((a*i)/50),int((b*i)/50),int((c*i)/50)))
        np.write()
   
    for i in range(50,0,-1):
        a,b,c=color[select]
        np.fill((int((a*i)/50),int((b*i)/50),int((c*i)/50)))
        np.write()
        
    for i in range(0,50):
        a,b,c=color[select]
        np.fill((int((a*i)/50),int((b*i)/50),int((c*i)/50)))
        np.write()   
   
    for i in range(50,0,-1):
        a,b,c=color[select]
        np.fill((int((a*i)/50),int((b*i)/50),int((c*i)/50)))
        np.write()
        sleep(0.02)
        
