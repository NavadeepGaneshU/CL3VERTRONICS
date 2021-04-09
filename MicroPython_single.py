#Blogs @ https://clevertronics.blogspot.com/search/label/MicroPython
#------------------------------------------BLOG POST #1------------------------------------------------------------
# Hello world, The below are MicroPython codes which are tested on ESP 8266 V.3. All details are mentioned at clevertronics.blogspot.com
#Turn LED on

# Hello world, The below are MicroPython codes which are tested on ESP 8266 V.3. All details are mentioned at clevertronics.blogspot.com
#Turn LED ON

import machine
pin = machine.Pin(2, machine.Pin.OUT)
pin.on()

#------------------------------------------BLOG POST #1------------------------------------------------------------
# Hello world, The below are MicroPython codes which are tested on ESP 8266 V.3. All details are mentioned at clevertronics.blogspot.com
#Blink with Delay

import machine
import time
pin = machine.Pin(2, machine.Pin.OUT)
while True:
    pin.on()
    time.sleep(0.5)
    pin.off()
    time.sleep(0.5)
    
#-----------------------------------------BLOG POST #2------------------------------------------------------
# Hello world, The below are MicroPython codes which are tested on ESP 8266 V.3. All details are mentioned at clevertronics.blogspot.com
#Blink custom number of times

import machine
import time
pin = machine.Pin(2, machine.Pin.OUT)
n=int(input("Enter the number of Blinks you need : "))
for i in range(n):
    pin.off()
    time.sleep(0.5)
    pin.on()
    time.sleep(0.5)
    
#-----------------------------------------BLOG POST #3----------------------------------------------------
# Hello world, The below are MicroPython codes which are tested on ESP 8266 V.3. All details are mentioned at clevertronics.blogspot.com
#PWM, LED fade

from machine import Pin, PWM
from time import sleep
frequency = 5000
led = PWM(Pin(2), frequency)
while True:
  for duty_cycle in range(0, 1024):
    led.duty(duty_cycle)
    sleep(0.005)

#--------------------------------------BLOG POST #4--------------------------------------------------
# Hello world, The below are MicroPython codes which are tested on ESP 8266 V.3. All details are mentioned at clevertronics.blogspot.com
#Read Temperature Sensor

from machine import Pin
from time import sleep
import dht
sensor = dht.DHT11(Pin(14))
while True:
  try:
    sleep(2)
    sensor.measure()
    temp = print('Temperature:',sensor.temperature(),'*C','\n')
    hum = print('Humidity:',sensor.humidity(),'%','\n','-----------')
  except OSError as e:
    print('Failed to read sensor.')

#-------------------------------------BLOG POST #4-----------------------------------------------
# Hello world, The below are MicroPython codes which are tested on ESP 8266 V.3. All details are mentioned at clevertronics.blogspot.com
#DHT-11 based simple temperature alert system.

import machine
pin1 = machine.Pin(5, machine.Pin.OUT)
pin2 = machine.Pin(14, machine.Pin.OUT)
from machine import Pin
from time import sleep
import dht

sensor = dht.DHT11(Pin(4))

while True:
  try:
    sleep(2)
    sensor.measure()
    print('Temperature:',sensor.temperature(),'*C','\n')
    print('Humidity:',sensor.humidity(),'%','\n','-------------------')
  except OSError as e:
    print('Failed to read sensor.')

  if sensor.temperature() >33:
      pin1.on()
      print('Temperature:',sensor.temperature(),'*C',"Temperature is High(>33*C)",'\n')
  else:
      pin1.off()
        
  if sensor.humidity() > 90:
      pin2.on()
      print('Humidity:',sensor.humidity(),'%',"Humidity is High(>90%)",'\n','-------------------')
  else:
      pin2.off()
