# 4. Write a statement that displays an info dialog box with the title “Program Paused”
# and the message “Click OK when you are ready to continue.”

import tkinter
import tkinter.messagebox

class MyGui:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.my_button = tkinter.Button(self.main_window, text="Press Me", command=self.do_something)
        self.my_button.pack()
        tkinter.mainloop()

    def do_something(self):
        tkinter.messagebox.showinfo("Program Paused", "Click OK when you are ready to continue.")


myGUI = MyGui()
