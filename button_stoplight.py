import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(12,GPIO.IN)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
while True:
    if GPIO.input(12) == 0:
        print("Green on")
       ##Turns the light on then pauses for 5 seconds
        GPIO.output(18,GPIO.HIGH)
        time.sleep(5)
        print("Green off")
        GPIO.output(23,GPIO.HIGH)
       ##Signals that the light is on
        print("Yellow on")
       ##Turns the ligh on and then pauses for 1 second
        time.sleep(1)
        print("Yellow off")
       ##Turns the ligh off
        GPIO.output(18,GPIO.LOW)
       ##Signals that the light is on
        print("Red on")
       ##Turns the ligh on then pauses for 4 seconds
        time.sleep(4)
        print("Red off")
       #Turns the light off
        GPIO.output(23,GPIO.LOW)
    elif GPIO.input(12) == 1:
       continue