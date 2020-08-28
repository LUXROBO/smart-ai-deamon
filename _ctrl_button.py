import os
import time
import signal
import subprocess

import RPi.GPIO as GPIO

from concurrent.futures import ThreadPoolExecutor

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

        self.flag_pool = ThreadPoolExecutor(max_workers=1)

    def run(self):
        try:
            while True:
                self.flag_pool.submit(self._run_file)
        except ValueError:
            print("wrong")

    def _run_file(self):
         pin = GPIO.wait_for_edge(6, GPIO.FALLING, timeout=1000)
         if pin is None:
             print("timeout")
         else:
             print("edge detected")
             if self.run_flag:
                 print('process kill')
                 os.kill(self.p.pid, signal.SIGTERM)
                 self.run_flag = False
             else:
                 cmd = ["sudo python3 /home/pi/workspace/run.py"]
                 self.p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
                 print(self.p.pid)
                 self.run_flag = True
                 time.sleep(1)

    def exit(self):
        self.run_flag = False
