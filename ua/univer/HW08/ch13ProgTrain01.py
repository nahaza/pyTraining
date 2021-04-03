# 1. Name and Address
# Write a GUI program that displays your name and address when a button is clicked. The
# program’s window should appear as the sketch on the left side of Figure 13-42 when it
# runs. When the user clicks the Show Info button, the program should display your name
# and address, as shown in the sketch on the right of the figure.

import tkinter

class NameAddressGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.geometry("200x200")
        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        self.addressName = tkinter.StringVar()
        self.address_label = tkinter.Label(self.top_frame, textvariable=self.addressName)
        self.address_label.pack(side='left')
        self.show_button = tkinter.Button(self.bottom_frame, text="Show info", command=self.show_info)
        self.quit_button = tkinter.Button(self.bottom_frame, text="Quit", command=self.main_window.destroy)
        self.show_button.pack(side='left')
        self.quit_button.pack(side='left')
        self.top_frame.pack()
        self.bottom_frame.pack()
        self.main_window.mainloop()

    def show_info(self):
        self.text = "Steven Marcus\n274 Baily Drive\nWaynesville, NC 27999"
        self.addressName.set(self.text)


myGUI = NameAddressGUI()