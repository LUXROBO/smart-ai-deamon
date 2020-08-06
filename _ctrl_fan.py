import sys
import time

import RPi.GPIO as GPIO

from concurrent.futures import ThreadPoolExecutor

class CtrlFan:
    _instance = None

    @classmethod
    def _getInstance(cls):
        return cls._instance

    @classmethod
    def instance(cls, *args, **kargs):
        cls._instance = cls(*args, **kargs)
        cls._instance = _getInstance
        return cls._instance

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