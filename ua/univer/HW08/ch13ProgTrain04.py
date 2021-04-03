# 4. Celsius to Fahrenheit
# Write a GUI program that converts Celsius temperatures to Fahrenheit temperatures. The
# user should be able to enter a Celsius temperature, click a button, then see the equivalent
# Fahrenheit temperature. Use the following formula to make the conversion:
# F 5 9 C 1 32
#  5
# F is the Fahrenheit temperature, and C is the Celsius temperature.

import tkinter


class CtoFGUI():
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.geometry("300x300")
        self.main_window.title("Celsius to Fahrenheit")
        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        self.prompt_label = tkinter.Label(self.top_frame, text="Enter the Celsius temperature: ")
        self.entry_celcius=tkinter.Entry(self.top_frame, width=12)
        self.prompt_label.pack(side='left')
        self.entry_celcius.pack(side='left')
        self.display_message = tkinter.Label(self.mid_frame, text='In Fahrenheit it equals to: ')
        self.fahrenheit = tkinter.StringVar()
        self.show_fahrenheit = tkinter.Label(self.mid_frame, textvariabl=self.fahrenheit)
        self.display_message.pack(side='left')
        self.show_fahrenheit.pack(side='left')
        self.calc_button = tkinter.Button(self.bottom_frame, text='Convert to Fahrenheit', command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame, text='QUIT', command=self.main_window.destroy)
        self.calc_button.pack()
        self.quit_button.pack()
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()
        self.main_window.mainloop()

    def convert(self):
        self.calculated_fahrenheit = ((9/5)*float(self.entry_celcius.get())+32)
        self.fahrenheit.set(format(self.calculated_fahrenheit, ',.2f'))


myGUI = CtoFGUI()