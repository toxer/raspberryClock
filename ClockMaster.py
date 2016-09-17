import threading
import time
import sys
sys.path.append("./libs")

from Clock import Clock
from Ntp import Ntp

class ClockMaster(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.clock = Clock()
        self.clock.setPoint(True)
        self.ntp = Ntp()




    def run(self):
        self.clock.start()
        self.ntp.start()

        while True:
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
            time.sleep(1)
            if (self.ntp.time != None):
                self.ntp.addSecond()

clockMaster = ClockMaster()
clockMaster.start()
