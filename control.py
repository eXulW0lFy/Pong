import random
import time
from threading import Thread
from data import Data


class Control:
    c_ = [False, 1, 0]
    
    def __init__(self):
        pass
    
    @staticmethod
    def player1():
        # player1 = Thread(target=control, args=(tk, players[1], pos))
        pl = Thread(target=Control.control, args=(0, ))
        pl.start()
        
    @staticmethod
    def player2():
        # player2 = Thread(target=control, args=(tk, players[1], pos))
        pl = Thread(target=Control.move, args=(1, ))
        pl.start()
    
    @staticmethod
    def control(n):
        while True:
            Control.move(n)
            # n = random.randint(1, 2)
            # Control.move(n)
            
    @staticmethod
    def move(n):
        while True:
            destination = random.randint(0, 392)
            Data.control = [True, Data.player[n], destination]
            time.sleep(0.001)
        
        # player1 = Thread(target=Main().control(1), args=(1, ))
        # player1 = Thread(target=self.down(self.tk, self.obj[1], 1), args=(0.002, ))
        # player1.start()
