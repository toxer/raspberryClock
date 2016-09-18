#GPIO CONFIGURATION
from gpiozero import LED
import time

import threading


class Clock (threading.Thread):

    HIGHT = 0.08


    A=2
    B=3
    C=4
    D=17
    E=27
    F=22
    G=10
    P=9

    L1 = 5
    L2 = 6
    L3 = 13
    L4 = 19

    SWITCH_TIME=0.0001
    started = False



    LINES ={'L1':LED(L1),'L2':LED(L2),'L3':LED(L3),'L4':LED(L4)}
    SEGMENTS = {'A':LED(A),'B':LED(B),'C':LED(C),'D':LED(D),'E':LED(E),'F':LED(F),'G':LED(G),'P':LED(P)}
    NUMBERS = {'0':['A','B','C','D','E','F'],'1':['B','C'],'2':['A','B','G','E','D'],'3':['A','B','G','C','D'],'4':['F','B','G','C'],'5':['A','C','D','F','G'],'6':['A','C','D','F','G','E'],'7':['A','C','B'],'8':['A','B','C','D','E','F','G'],'9':['A','B','C','D','F','G']}

    def __init__(self):
        threading.Thread.__init__(self)
        self.number = None
        self.numberString=None
        self.__point=None




    def writeNumber(self,number):
        self.number = number
        self.numberString=None

    def writeNumberString(self,numberString):
        self.numberString = numberString
        self.number=None




    def lineOn(self,lines):
        for L in self.LINES.keys():
            if L in lines:
                self.LINES[L].on()
            else:
                self.LINES[L].off()

    def segmentOn(self,segments):
        for S in self.SEGMENTS.keys():
            if S in segments:
                #ACCESO A LOW
                self.SEGMENTS[S].off()
            else:
                #SPENTO A 1
                self.SEGMENTS[S].on()

    def pointOn(self,value):
        if self.__point==True:
            self.SEGMENTS['P'].off();
        else:
            self.SEGMENTS['P'].on();

    def stop(self):
        self.started=False


    def switchOff(self):
        self.lineOn([])
        self.segmentOn([])

    def setPoint(self, value):
        self.__point = value





    def run(self):
        self.started = True
        self.pointOn(False)
        while self.started:
            if (self.number != None or self.numberString != None):
                cifra1='0'
                cifra2='0'
                cifra3='0'
                cifra4='0'
                numberString = self.numberString
                if numberString == None:
                    numberString = str(self.number)

                if len(numberString) < 2:
                    cifra1 = numberString
                elif len(numberString) >=2 and len(numberString) < 3:
                    cifra1 = numberString[1]
                    cifra2 = numberString[0]
                elif len(numberString) >=3 and len(numberString) < 4:
                    cifra1 = numberString[2]
                    cifra2 = numberString[1]
                    cifra3 = numberString[0]
                else:
                    cifra1 = numberString[3]
                    cifra2 = numberString[2]
                    cifra3 = numberString[1]
                    cifra4 = numberString[0]


                if cifra1 != None:
                    self.lineOn('L4')
                    self.segmentOn(self.NUMBERS[cifra1])
                    time.sleep(self.SWITCH_TIME)
                    self.switchOff()
                if cifra2 != None:
                    self.lineOn('L3')
                    self.segmentOn(self.NUMBERS[cifra2])
                    time.sleep(self.SWITCH_TIME)
                    self.switchOff()
                if cifra3 != None or (self.__point != None and self.__point == True):
                    self.lineOn('L2')
                    if cifra3 != None:
                        self.segmentOn(self.NUMBERS[cifra3])
                    if self.__point != None:
                        self.pointOn(self.__point)
                    time.sleep(self.SWITCH_TIME)

                    self.switchOff()
                if cifra4 != None:
                    self.lineOn('L1')
                    self.segmentOn(self.NUMBERS[cifra4])
                    time.sleep(self.SWITCH_TIME)
                    self.switchOff()
                self.switchOff()
            else:
                time.sleep(self.SWITCH_TIME)








def test():
    clock =  Clock();
    for L in ['L1','L2','L3','L4']:
        clock.lineOn(L)
        for S in ['A','B','C','D','E','F']:
            clock.segmentOn(S)
            time.sleep(0.1)
    for L in ['L1','L2','L3','L4']:
        clock.lineOn(L)
        for S in ['P']:
            clock.segmentOn(S)
            time.sleep(0.4)
    for L in ['L1','L2','L3','L4']:
        clock.lineOn(L)
        for S in ['G']:
            clock.segmentOn(S)
            time.sleep(0.4)

def test3():
    clock =  Clock();
    clock.start();
    clock.writeNumber(300)
    time.sleep(5)
    clock.stop()

def test2():

    clock =  Clock();
    clock.setPoint(True)
    clock.start();
    start_time = time.time()
    for n in range(2001
    ):
        clock.writeNumberString(str(2000-n))
        time.sleep(0.01)
    print ( str((time.time() - start_time))+" sec.")
    time.sleep(3)
    clock.stop()







#test della classe
if __name__ == "__main__":
    test2()
