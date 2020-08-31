import os
import signal
import subprocess
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

run_flag = False

p = None
pid = None

while True:
    pin = GPIO.wait_for_edge(6, GPIO.FALLING, timeout=1000)
    if pin is None:
        #print("timeout")
        pass
    else:
        #print("edge detected")
        if run_flag:
            os.killpg(pid, signal.SIGTERM)
            run_flag = False
        else:
            p = subprocess.Popen(['sudo', '/usr/bin/python3', '/home/pi/workspace/run.py'],stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=False,preexec_fn=os.setsid)
            pid = p.pid
            time.sleep(3)
            run_flag = True

