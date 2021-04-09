# 3. Write a statement that creates a Frame widget. Its parent should be self.main_ window

import tkinter


class MyGui:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.frame = tkinter.Frame(self.main_window)
        self.label1 = tkinter.Label(self.frame, text="Label1")
        self.label1.pack()
        self.frame.pack()
        tkinter.mainloop()


myGUI = MyGui()
