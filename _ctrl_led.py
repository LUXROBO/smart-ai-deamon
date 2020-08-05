import sys
import time

import board
import neopixel

import RPi.GPIO as GPIO

class CtrlLed:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(12, GPIO.OUT)
        GPIO.output(12, True)        

        self.pixels = neopixel.NeoPixel(borad.D12, 1)

    def run(self):
        while 1:
            try:
                pixels[0] = (0, 255, 0)
                print("All system boot up")

            except OSError as e:
                print("There is no shield")

            except KeyboardInterrupt:
                self.pixels[0] = (0, 0, 0)
                print("Terminate the program")
                sys.exit(0)
        
    def exit(self):
        self.pixels[0] = (0, 0, 0)
        print("Terminate the program")
        sys.exit(0)
        
if __name__ == "__main__":
    led = CtrlLed()
    led.run()
