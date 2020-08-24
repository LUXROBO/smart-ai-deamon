import sounddevice as sd
import soundfile as sf

def play_beep():
    data, fs = sf.read('/home/pi/rpi-daemon-py/sound/beep.wav', dtype="float32")
    sd.play(data, fs)
    sd.wait()

if __name__ == "__main__":
    play_beep()

