import tkinter
from danser import open_danser

class Window:
    def __init__(self):
        self._open = False
        self._window = None

    def open(self):
        self._window = tkinter.Tk('DanserGUI', 'DanserGUI')
        self._window.geometry('800x600')
        self._window.title('DanserGUI')        
        self.draw_elements()
        self._open = True

    def draw_elements(self):        
        btn = tkinter.Button(self._window, text='Run', width=10, height=5, command=lambda: open_danser('RAISE MY SWORD', 'Hard'))
        btn.place(x=0, y=0)

    def loop(self):
       self._window.mainloop()

    def isOpen(self):
        return self._open