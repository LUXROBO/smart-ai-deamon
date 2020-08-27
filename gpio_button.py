import sys

from _ctrl_button import CtrlButton

from daemon import Daemon

class RPIDaemon(Daemon):
    def run(self):
        try:
            button = CtrlButton()
            button.run()

        except Exception as err:
            print("No button")

    def initialize(self):
        button = CtrlButton()
        print(button)
        button.exit()

if __name__ == "__main__":
    daemon = RPIDaemon('var/run/gpio_button.pid')
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            daemon.start()
        elif 'stop' == sys.argv[1]:
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            daemon.restart()
        else:
            print("Unknown command")
            sys.exit(2)
        sys.exit(0)
    else:
        print(f"usage : {sys.argv[0]} start | stop | restart")
        sys.exit(2)
