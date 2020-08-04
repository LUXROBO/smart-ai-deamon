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
        """
        Do Unix double fork magic: fork a second child and exit immediately to prevent zombie
        """
        try:
            # fork child process
            pid = os.fork()
            
            # if pid > 0, parent process
            if pid > 0: 
                sys.exit(0)
        except OSError as e:
            sys.stderr.write(f"fork #1 failed: {e.errno, e.strerror} \n")
            sys.exit(1)

        # decouple parent process
        os.chdir("/")
        os.setsid()
        os.umask(0)

            # do second fork
        try:
            pid = os.fork
            if pid > 0:
                sys.exit(0)
        except OSError as e:
            sys.stderr.write(f"fork #2 failed: {e.errno, e.strerror}")
            sys.exit(1)

        # redirect standard file descriptors 
        sys.stdout.flush()
        sys.stderr.flush()
        si = file(self.stdin, 'r')
        so = file(self.stdout, 'a+')
        se = file(self.stderr, 'a+', 0)
        os.dup2(si.fileno(), sys.stdin.fileno())
        os.dup2(so.fileno(), sys.stdout.fileno())
        os.dup2(se.fileno(), sys.stderr.fileno())
    
        # write pidfile
        atexit.register(self.delpid)
        pid = str(os.getpid())
        file(self.pidfile,'w+').write("%s\n" % pid)

    def delpid(self):
        os.remove(self.pidfile)
    
    def start(self):
        """
        Start the daemon
        """
        try:
            pf = file(self.pidfile,'r')
            pid = int(pf.read().strip())
            pf.close()
        except IOError:
            pid = None
    
        if pid:
            message = "pidfile %s already exist. Daemon already running?\n"
            sys.stderr.write(message % self.pidfile)
            sys.exit(1)
        
        # Start the daemon
        self.daemonize()
        self.run()

    def stop(self):
        """
        Stop the daemon
        """

        try:
            pf = file(self.pidfile, 'r')
            pid = int(pf.read().strip())
            pf.close()
        except: 
            pid = None

        if not pid:
            message = "pidfile %s does not exist. Daemon not running? \n"
            sys.stderr.write(message % self.pidfile)
            return 
        # Try killing the daemon process	
        try:
            while 1:
                os.kill(pid, SIGTERM)
                time.sleep(0.1)
        except OSError as err:
            err = str(err)
            if err.find("No such process") > 0:
                if os.path.exists(self.pidfile):
                    os.remove(self.pidfile)
            else:
                print(str(err))
                sys.exit(1)

    def restart(self):
        """
        Restart the daemon
        """
        self.stop()
        self.start()
    
    def run(self):
        """
        You should override this method.
        """