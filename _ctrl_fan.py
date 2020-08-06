import sys
import time

import RPi.GPIO as GPIO

from concurrent.futures import ThreadPoolExecutor

class CtrlFan:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(13, GPIO.OUT)

    def run(self):
        try:
            while 1:
                GPIO.output(13, True)
                time.sleep(0.01)

        except KeyboardInterrupt:
            GPIO.cleanup()
            sys.exit(0)
                
        finally:
            GPIO.cleanup()

if __name__ == "__main__":
    fan = CtrlFan()
    fan.run()