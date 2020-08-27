iport os
import signal
import subprocess

try :
    cmd = subprocess.run(["sudo", "python3", "/home/pi/workspace/run.py"])

    pro = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                           shell=True, preexec_fn=os.setsid)
    mes = input("quit\n\n")
except KeyboardInterrupt:

    os.killpg(os.getpid(pro.pid), signal.SIGTERM)
