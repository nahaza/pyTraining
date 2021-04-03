# 1. Write a statement that creates a Label widget. Its parent should be self.main_ window,
# and its text shoud be 'Programming is fun!'
import tkinter

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.label = tkinter.Label(self.main_window, text="Programming is fun!")
        self.label.pack()
        tkinter.mainloop()


my_Gui = MyGUI()
