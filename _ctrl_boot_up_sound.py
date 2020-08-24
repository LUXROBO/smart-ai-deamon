import sounddevice as sd
import soundfile as sf

data, fs = sf.read('/home/pi/rpi-daemon-py/sound/beep.wav', dtype="float32")
sd.play(data, fs)

