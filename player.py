from tkinter import *
import time
from main import Main
from data import Data


class Player:
    def __init__(self, name: str, color: str,
                 left: int, top_bottom: tuple):
        self.name = name
        self.color = color
        self._margin_min = 16
        self._margin_max = 64
        self._width = 32
        self._height = 128
        self._left = left - self._margin_min
        self._top = 0
        self._right = left + self._width
        self._bottom = top_bottom[1] - top_bottom[0]
        self._pos = 0
        self._cv_player = Data.cv.create_rectangle(
            (left, top_bottom[0]), (self._right, top_bottom[0] + self._height),
            fill=self.color, outline='black', width=1)
    
    def get_canvas(self):
        return self._cv_player
    
    def get_pos(self):
        return {'left': self._left,
                'min': self._top,
                'max': self._bottom,
                'height': self._height,
                'pos': self._pos}
    
    def set_pos(self, pos):
        self._pos = pos
        
  