import os
import signal
import subprocess
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

run_flag = False

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
