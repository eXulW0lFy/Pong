import time
from tkinter import *

import player
from control import Control
from data import Data


class Main:
    
    def __init__(self):
        # [Поле, Игрок1, Игрок2, Шар]
        self.obj = [False, 0, 0]
        Data.tk = Tk()
        Data.tk.title('Pong')
        Data.tk.resizable(0, 0)
        Data.tk.wm_attributes("-topmost", 1)
        cv_width = 800
        cv_height = 600
        
        Data.play_button = Button(Data.tk, text='Play')
        Data.play_button.bind('<Button-1>', self.btn_play)
        Data.play_button.pack()
        
        Data.cv = Canvas(Data.tk, width=cv_width, height=cv_height,
                         highlightthickness=0, bg='white')
        Data.cv.pack()
        Data.margin_min = 16
        Data.margin_max = 64
        f_left = Data.margin_min
        f_top = Data.margin_max
        f_right = cv_width - Data.margin_min
        f_bottom = cv_height - Data.margin_min
        # поле игры
        Data.field = Data.cv.create_rectangle((f_left, f_top), (f_right, f_bottom),
                                              fill='#393939', outline='black', width=3)
        # player1
        Data.player[0] = player.Player('Player 1', '#FF4500',
                                       f_left + Data.margin_min, (f_top, f_bottom))
        # player2
        Data.player[1] = player.Player('Player 2', '#008080',
                                       f_right - Data.margin_min - 32, (f_top, f_bottom))
        Data.tk.update()
        
        Control.player1()
        Control.player2()

    @staticmethod
    def move_():
        if Data.control[0] and not Data.pause:
            pl = Data.control[1]
            destination = Data.control[2]
            print(pl.name)
            if destination < 0:
                destination = 0
            elif destination > pl.get_pos()['max'] - 64 - pl.get_pos()['height']:
                destination = pl.get_pos()['max'] - 64 - pl.get_pos()['height']
            dist = destination - pl.get_pos()['pos']
            for i in range(abs(dist)):
                Data.cv.move(pl.get_canvas(), 0, dist / abs(dist))
                Data.tk.update()
                time.sleep(0.001)
            pl.set_pos(destination)
            # print(MyThread.move)
            Control.c_[0] = False
            time.sleep(0.001)
        else:
            print('.', end='')
    
    @staticmethod
    def draw(pl):
        pass
    
    @staticmethod
    def btn_play(event):
        if Data.pause:
            Data.pause = False
        else:
            Data.pause = True
        Data.tk.update()
        Data.tk.update()
        Data.tk.update()


if __name__ == '__main__':
    # test.test_old()
    m = Main()
    while True:
        m.move_()
