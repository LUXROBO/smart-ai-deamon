import os
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

        self._temp_flag = False

        self._temp_pool = ThreadPoolExecutor(max_workers=1)

    def run(self):
        try:
            while 1:
                self._temp_pool.submit(self._get_temp)
                if self._temp_flag:
                    GPIO.output(13, True)
                    time.sleep(0.01)

        except KeyboardInterrupt:
            GPIO.cleanup()
            sys.exit(0)
                
        finally:
            GPIO.cleanup()
        
    def _get_temp(self):
        temp = os.popen("vcgencmd measure_temp").readline()
        temp = temp.replace("temp=","")
        token = temp.split("'")
        temp = token[0]
        temp = float(temp)
        
        if 50 < temp:
            self._temp_flag = True
        else:
            self._temp_flag = False
    
    def exit(self):
        self._temp_flag = False
        GPIO.output(13, False)

if __name__ == "__main__":
    fan = CtrlFan()
    fan.run()
