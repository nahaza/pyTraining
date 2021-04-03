# 2. Assume self.label1 and self.label2 reference two Label widgets. Write code that
# packs the two widgets so they are positioned as far left as possible inside their parent
# widget.

import tkinter

class My_GUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.label1 = tkinter.Label(self.main_window, text="Label1")
        self.label2 = tkinter.Label(self.main_window, text="Label2")
        self.label1.pack(side="left")
        self.label2.pack(side="left")
        tkinter.mainloop()


myGUI = My_GUI()

