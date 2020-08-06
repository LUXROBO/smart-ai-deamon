import sys
import time
import socket

import board
import neopixel

import RPi.GPIO as GPIO

from concurrent.futures import ThreadPoolExecutor

class CtrlLed:
    _instance = None

    @classmethod
    def _getInstance(cls):
        return cls._instance

    @classmethod
    def instance(cls, *args, **kargs):
        cls._instance = cls(*args, **kargs)
        cls._instance = cls._getInstance
        return cls._instance

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(12, GPIO.OUT)
        GPIO.output(12, True)        

        self.pixels = neopixel.NeoPixel(board.D12, 1)

        self._jupyter_flag = False
        self._unstable_flag = False

        self.flag_pool = ThreadPoolExecutor(max_workers=1)

    def run(self):
        try:
            while 1:
                self.flag_pool.submit(self.__monitoring_kernel)

                if self._jupyter_flag:
                    self.pixels[0] = (0, 255, 0)
                else:
                    self.pixels[0] = (255, 0, 0)
                
        except KeyboardInterrupt:
            self.exit()
            sys.exit(0)
        
    def __monitoring_kernel(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        res = sock.connect_ex(('127.0.0.1', 8888))

        if res == 0: 
            self._jupyter_flag = True

        else:
            self._jupyter_flag = False

    def exit(self):
        self._jupyter_flag = False
        self.pixels[0] = (0, 0, 0)

if __name__ == "__main__":
    led = CtrlLed()
    led.run()