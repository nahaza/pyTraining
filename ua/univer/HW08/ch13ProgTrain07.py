# . Long-Distance Calls
# A long-distance provider charges the following rates for telephone calls:
# Rate Category Rate per Minute
# Daytime (6:00 a.m. through 5:59 p.m.) $0.07
# Evening (6:00 p.m. through 11:59 p.m.) $0.12
# Off-Peak (midnight through 5:59 a.m.) $0.05
# Write a GUI application that allows the user to select a rate category (from a set of radio
# buttons), and enter the number of minutes of the call into an Entry widget. An info dialog
# box should display the charge for the call.

import tkinter
import tkinter.messagebox

class CallGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Long-Distance Calls")
        self.main_window.geometry("500x500")
        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        self.call_rate = tkinter.DoubleVar()
        self.call_rate.set(1)
        self.rb1 = tkinter.Radiobutton(self.top_frame, text='Daytime 6AM through 5:59PM: $0.07 per minute',
                                       variable=self.call_rate, value=0.07)
        self.rb2 = tkinter.Radiobutton(self.top_frame, text='Evening 6PM through 11:59PM: $0.12 per minute',
                                       variable=self.call_rate, value=0.12)
        self.rb3 = tkinter.Radiobutton(self.top_frame, text='Off-peak midnight through 5:50AM: $0.05 per minute',
                                       variable=self.call_rate, value=0.05)
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()
        self.prompt_label = tkinter.Label(self.mid_frame, text="How many minutes: ")
        self.entry = tkinter.Entry(self.mid_frame)
        self.prompt_label.pack()
        self.entry.pack(side='left')
        self.calc_button = tkinter.Button(self.bottom_frame, text='Calculate the cost', command=self.CalculateCost)
        self.quit_button = tkinter.Button(self.bottom_frame, text='QUIT', command=self.main_window.destroy)
        self.calc_button.pack()
        self.quit_button.pack()
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()
        self.main_window.mainloop()

    def CalculateCost(self):
        self.calculated_total = float(self.entry.get()) * float(self.call_rate.get())
        tkinter.messagebox.showinfo("Total cost", "Total: ${total:.2f}".format(total=self.calculated_total))


example=CallGUI()
