//ARDUINO IDE CODE

int sensorPin = A0; 
int sensorValue = 0;
void setup() {
  Serial.begin(9600);
  pinMode(sensorPin, INPUT); 
}
void loop() {
  sensorValue = analogRead(sensorPin);
  Serial.println(sensorValue);
  delay(100);
}

--------------------------------------------------------------------------------------
# VPYTHON CODE

import serial 
from vpython import *
arduinoSerialData = serial.Serial('com10', 9600)
AudioLabel = label(pos=vector(0,5,0), height=80)
dot=sphere(pos=vector(-7,-2,0), radius=0.5,color=color.blue)

dot=sphere(pos=vector(-7,-2,0), radius=0.5,color=color.blue)
dot=sphere(pos=vector(-5,-2,0), radius=0.5,color=color.green)
dot=sphere(pos=vector(-3,-2,0), radius=0.5,color=color.green)
dot=sphere(pos=vector(-1,-2,0), radius=0.5,color=color.green)
dot=sphere(pos=vector(1,-2,0), radius=0.5,color=color.green)
dot=sphere(pos=vector(3,-2,0), radius=0.5,color=color.green)
dot=sphere(pos=vector(5,-2,0), radius=0.5,color=color.blue)
dot=sphere(pos=vector(7,-2,0), radius=0.5,color=color.blue)
dot=sphere(pos=vector(9,-2,0), radius=0.5,color=color.blue)
dot=sphere(pos=vector(11,-2,0), radius=0.5,color=color.blue)
dot=sphere(pos=vector(13,-2,0), radius=0.5,color=color.blue)
dot=sphere(pos=vector(15,-2,0), radius=0.5,color=color.red)
dot=sphere(pos=vector(17,-2,0), radius=0.5,color=color.red)
dot=sphere(pos=vector(20,-2,0), radius=0.5,color=color.red)
dot=sphere(pos=vector(22,-2,0), radius=0.5,color=color.red)
dot=sphere(pos=vector(24,-2,0), radius=0.5,color=color.red)
dot=sphere(pos=vector(-7,-9,0), radius=0.5,color=color.blue)
dot=sphere(pos=vector(-5,-9,0), radius=0.5,color=color.green)
dot=sphere(pos=vector(-3,-9,0), radius=0.5,color=color.green)
dot=sphere(pos=vector(-1,-9,0), radius=0.5,color=color.green)
dot=sphere(pos=vector(1,-9,0), radius=0.5,color=color.green)
dot=sphere(pos=vector(3,-9,0), radius=0.5,color=color.green)
dot=sphere(pos=vector(5,-9,0), radius=0.5,color=color.blue)
dot=sphere(pos=vector(7,-9,0), radius=0.5,color=color.blue)
dot=sphere(pos=vector(9,-9,0), radius=0.5,color=color.blue)
dot=sphere(pos=vector(11,-9,0), radius=0.5,color=color.blue)
dot=sphere(pos=vector(13,-9,0), radius=0.5,color=color.blue)
dot=sphere(pos=vector(15,-9,0), radius=0.5,color=color.red)
dot=sphere(pos=vector(17,-9,0), radius=0.5,color=color.red)
dot=sphere(pos=vector(20,-9,0), radius=0.5,color=color.red)
dot=sphere(pos=vector(22,-9,0), radius=0.5,color=color.red)
dot=sphere(pos=vector(24,-9,0), radius=0.5,color=color.red)
measuringRod = cylinder( radius= 0.4, length=100, color=color.red, pos=vector(-7,-2,0))
target=box(pos=vector(0,-2,0), length=0.5, width=4, height=9, color=color.red)
while (1==1): 
    rate(20)
    if (arduinoSerialData.inWaiting()>0):  
        myData = arduinoSerialData.readline() 
        print (myData) 
        Audio = float(myData)
        measuringRod.length=Audio
        target.pos=vector(Audio,-5,0)
        myLabel= Audio
        AudioLabel.text = "Audio:{}".format(Audio)
