import os
import time
import signal
import subprocess

import RPi.GPIO as GPIO

class CtrlButton:
    _instance = None
    
    @classmethod
    def _genInstance(self):
        return cls._instance

    @classmethod
    def instance(cls, *args, **kargs):
        cls._instance = cls(*args, **kargs)
        cls._instance = _getInstance
        return cls._instance

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        self.run_flag = False

    def run(self):
        while True:
            pin = GPIO.wait_for_edge(6, GPIO.FALLING, timeout=1000)
            if pin is None:
                print("timeout")
            else:
                print("edge detected")
                if run_flag:
                    pass
                else:
                    cmd = subprocess.check_output(["sudo", "/usr/bin/python3", "/home/pi/workspace/run.py"])
                    run_flag = False
