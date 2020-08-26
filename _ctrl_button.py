import os
import signal
import subprocess
import RPi.GPIO as GPIO

run_state_flag = False

def button_callback(channel):
    if run_state_flag:
        cmd = subprocess.run(["sudo", "/usr/bin/python3", "/home/pi/workspace/run.py"])

        pro = subprocess.Popen()

        run_state_flag = False
    else:
        subprocess.run
    print("button was pushed")

GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(6, GPIO.RISING, callback=button_callback)

message = input("Press enter to quit\n\n")

GPIO.cleanup()
