import RPi.GPIO as GPIO
import time
##Creates variable for loop
i = 0
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
##Sets all three pins to output power
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
##Loops 3 times
while i < 3:
    ##Signals that the light is on
    print("Green on")
    ##Turns the light on then pauses for 5 seconds
    GPIO.output(18,GPIO.HIGH)
    time.sleep(5)
    print("Green off")
    ##Turns the light off
    GPIO.output(18,GPIO.LOW)
    ##Signals that the light is on
    print("Yellow on")
    ##Turns the ligh on and then pauses for 1 second
    GPIO.output(23,GPIO.HIGH)
    time.sleep(1)
    print("Yellow off")
    ##Turns the ligh off
    GPIO.output(23,GPIO.LOW)
    ##Signals that the light is on
    print("Red on")
    ##Turns the ligh on then pauses for 4 seconds
    GPIO.output(24,GPIO.HIGH)
    time.sleep(4)
    print("Red off")
    #Turns the light off
    GPIO.output(24,GPIO.LOW)
    i += 1
##Signals that the circuit has ended
print("Circuit Over")