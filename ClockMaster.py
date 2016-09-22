import threading
import time
import sys
import signal


sys.path.append("./libs")

from Clock import Clock
from Ntp import Ntp
from Server import ClockServer



class ClockMaster(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.clock = Clock()
        self.clock.setPoint(True)
        self.clock.showError(True)
        self.server = ClockServer(9090,self)
        self.started=False
        self.ntp = Ntp()

    def stop(self):
        self.started=False


    def updateNtp(self):
        if (self.ntp.time != None):
            number = None
            h = self.ntp.time.hour
            m = self.ntp.time.minute
            if h < 10:
                number = '0'+str(h)
            else:
                number = str(h)
            if m < 10:
                number = number + '0'+str(m)
            else:
                number = number + str(m)
            self.clock.writeNumberString(number)

    def killServer(self):
        self.server.stop();

    def run(self):
        self.clock.start()
        self.ntp.start()
        self.server.start();
        self.started=True
        while self.started:

            self.updateNtp()
        #    self.clock.switchPoint();
            if (self.ntp.time != None):
                if (self.ntp.error == False):
                    self.clock.showError(False)
                    self.ntp.addSecond()
                else:
                    self.clock.showError(True);
            time.sleep(0.5)
        print("Coda principale terminata")

clockMaster = ClockMaster()

def terminate(signal, frame):
    try:
        clockMaster.clock.switchOff();
        clockMaster.clock.stop()
        clockMaster.ntp.stop();
        clockMaster.server.stop();
        clockMaster.stop()

    except:
        print("Eccezione")
        print(sys.exc_info()[0])
    finally:
        sys.exit(0)
signal.signal(signal.SIGINT, terminate)
clockMaster.start()
signal.pause()
