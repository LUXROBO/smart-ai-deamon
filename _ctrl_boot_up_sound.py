import board
import neopixel

import RPi.GPIO as GPIO

import sounddevice as sd
import soundfile as sf

def play_beep():
    data, fs = sf.read('/usr/src/rpi-daemon-py/sound/beep.wav', dtype="float32")
    sd.play(data, fs)
    sd.wait()

def turn_led():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(12, GPIO.OUT)
    GPIO.output(12, True)

    pixels = neopixel.NeoPixel(board.D12, 1)

    pixels[0] = (0, 0, 30)

if __name__ == "__main__":
    play_beep()
    turn_led()
