from pyfirmata import *
from pyfirmata import util

import time
class door:
    def __init__(self, in1,in2 ,lts1,lts2, board ):
        it = util.Iterator(board)
        it.start()  
        self.in1 = board.get_pin("d:" + in1 + ":o")
        self.in2 = board.get_pin("d:" + in2 + ":o")
        self.ctmo =board.get_pin("d:"+lts1+":i")
        self.ctdong =board.get_pin("d:"+ lts2 + ":i")
        # self.enA = self.board.get_pin ("d:10:p")
        # self.enB = self.board.get_pin ("d:11:p")
    # def setSpeed (self ,speed ):
    #     self.enA.write (speed)
    #     self.enB.write (speed)
    def dung(self):
        self.in1.write(0)
        self.in2.write(0)
    def mocua(self):
        self.in1.write(1)
        self.in2.write(0)
        while True:
                print (self.ctmo.read())
                if  self.ctmo.read() ==False:  # Khi giá trị của ctmo là False
                    self.dung() # Kết thúc vòng lặp
                    break
    def dongcua(self):
        self.in1.write(0)
        self.in2.write(1)
        while True:
            print (self.ctdong)
            print (self.ctdong.read ())
            if  self.ctdong.read() ==False:  # Khi giá trị của ctmo là False
                self.dung() # Kết thúc vòng lặp
                break
Door = door('8', '9','3','5' ,Arduino ("COM9"))
Door.mocua ()
Door.dongcua ()




