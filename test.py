# main2
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
            print('.')
            
# main1
@staticmethod
def move_():
    if Control.c_[0] and not Data.pause:
        print(Control.c_[1].name)
        
        Control.c_[1].move_to(Control.c_[2])
        Data.tk.update()
        # print(MyThread.move)
        Control.c_[0] = False
        time.sleep(0.001)
    else:
        print('.')

# player
    def move_to(self, destination: int):
        if destination < 0:
            destination = 0
        elif destination > self._bottom - 64 - self._height:
            destination = self._bottom - 64 - self._height
        dist = destination - self._pos
        for i in range(abs(dist)):
            Data.cv.move(self._cv_player, 0, dist / abs(dist))
            Data.tk.update()
            time.sleep(0.001)
        self._pos = destination


        