# 3. Miles Per Gallon Calculator
# Write a GUI program that calculates a car’s gas mileage. The program’s window should
# have Entry widgets that let the user enter the number of gallons of gas the car holds,
# and the number of miles it can be driven on a full tank. When a Calculate MPG button
# is clicked, the program should display the number of miles that the car may be driven per
# gallon of gas. Use the following formula to calculate miles-per-gallon:
# MPG 5 miles
#  gallons


import tkinter

class MilesPerGallonGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Miles Per Gallon Calculator")
        self.top_frame1 = tkinter.Frame(self.main_window)
        self.top_frame2 = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        self.user_prompt1 = tkinter.Label(self.top_frame1, text="Enter car's volume: ")
        self.entry_capacity = tkinter.Entry(self.top_frame1, width=10)
        self.user_prompt1.pack(side='left')
        self.entry_capacity.pack(side='left')
        self.user_prompt2 = tkinter.Label(self.top_frame2, text="Enter mileage with full tank: ")
        self.entry_miles_driven = tkinter.Entry(self.top_frame2, width=10)
        self.user_prompt2.pack(side='left')
        self.entry_miles_driven.pack(side='left')
        self.display_message = tkinter.Label(self.mid_frame, text="Miles Per Gallon: ")
        self.miles = tkinter.StringVar()
        self.show_miles = tkinter.Label(self.mid_frame, textvariable=self.miles)
        self.display_message.pack(side='left')
        self.show_miles.pack(side='left')
        self.calc_button = tkinter.Button(self.bottom_frame, text="Calculate MPG", command=self.convert_mpg)
        self.quit_button = tkinter.Button(self.bottom_frame, text="QUIT", command=self.main_window.destroy)
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')
        self.top_frame1.pack()
        self.top_frame2.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()
        self.main_window.mainloop()

    def convert_mpg(self):
        mpg = (int(self.entry_miles_driven.get())/int(self.entry_capacity.get()))
        self.miles.set((format(mpg, ",.2f")))


myGUI = MilesPerGallonGUI()