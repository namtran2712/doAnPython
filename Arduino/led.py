from pyfirmata import *
import time
from pyfirmata import util
class LED:
    def __init__(self, port,board):
        
        it = util.Iterator(board)
        it.start()
        time.sleep (2)
        self.led_pin = board.get_pin("d:" + port + ":o")  
    def turnOn(self):
        
        self.led_pin.write(1)
    
    def turnOff(self):
        self.led_pin.write(0)

