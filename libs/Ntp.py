from socket import AF_INET, SOCK_DGRAM
import sys
import socket
import struct
import datetime
import threading
import time

class Ntp(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.time=None
        self.started=False
        self.locked=False


    def run(self):
        self.started = True
        while self.started:
            self.getNTPTime()
            time.sleep(20)

    def addSecond(self):
        if self.locked==False:
            self.time=self.time+datetime.timedelta(0,1)




    def getNTPTime(self,host = "ntp1.inrim.it"):
            self.locked=True
            port = 123
            buf = 1024
            address = (host,port)
            msg = '\x1b' + 47 * '\0'

            # reference time (in seconds since 1900-01-01 00:00:00)
            TIME1970 = 2208988800L # 1970-01-01 00:00:00

            # connect to server
            client = socket.socket( AF_INET, SOCK_DGRAM)
            client.sendto(msg, address)
            msg, address = client.recvfrom( buf )

            utc_secs = struct.unpack('!12I', msg)[10]
            utc_secs -= 2208988800L
            utc_secs = time.ctime(utc_secs)
            ntp_time = datetime.datetime.strptime(utc_secs, "%c")
            #formatted_time = datetime.datetime.strftime(ntp_time, "%Y-%m-%d %H:%M:%S")
            self.time = ntp_time
            print(self.time)
            self.locked=False

def test():
    ntp = Ntp();
    ntp.getNTPTime()
    print(ntp.time);
    ntp.addSecond()
    print(ntp.time)

#test()
