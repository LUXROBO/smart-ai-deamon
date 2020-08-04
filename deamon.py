import os
import sys
import time

class Daemon:
    """[summary]
    A generic daemon class

    Usage : subclass the Daemon class and override the run() method
    """
    def __init__(self, pidfile, stdin='/dev/null', stdout='/dev/null', stderr='/dev/null'):
        self.stdin = stdin
        self.stdout = stdout
        self.stderr = stderr
        self.pidfile = pidfile
    
    def deamonize(self):
        try:
            # fork child process
            pid = os.fork()
            
            # if pid > 0, parent process
            if pid > 0: 
                sys.exit(0)
        except OSError, e:
                sys.stderr.write(f"fork #1 failed: {e.errno, e.strerror} \n")
                sys.exit(1)

            # decouple parent process
            os.chdir("/")
            os.setsid()
            os.umask(0)

            # do second fork
        try:
            pid = os.fork