import board
import neopixel

import RPi.GPIO as GPIO

class CtrlLed:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(12, GPIO.OUT)
        GPIO.output(12, True)
        
        pixels = neopixel.NeoPixel(borad.D12, 1)

    def run(self):

        try:
            pixels[0] = (0, 255, 0)
            print("All system boot up")

        except OSError as e:
            print("There is no shield")
    
