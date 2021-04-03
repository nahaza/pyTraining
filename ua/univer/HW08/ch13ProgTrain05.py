# 5. Property Tax
# A county collects property taxes on the assessment value of property, which is 60 percent of
# the property’s actual value. If an acre of land is valued at $10,000, its assessment value is
# $6,000. The property tax is then $0.75 for each $100 of the assessment value. The tax for
# the acre assessed at $6,000 will be $45.00. Write a GUI program that displays the assessment
# value and property tax when a user enters the actual value of a property


import tkinter


class PropertyTaxGUI():
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Property Tax Calculator")
        self.main_window.geometry("400x400")
        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame1 = tkinter.Frame(self.main_window)
        self.mid_frame2 = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        self.prompt_label = tkinter.Label(self.top_frame, text="Enter the actual value of the property: $")
        self.entry_act_value = tkinter.Entry(self.top_frame, width=10)
        self.prompt_label.pack(side="left")
        self.entry_act_value.pack(side="left")
        self.display_message1 = tkinter.Label(self.mid_frame1, text="Assessment value is: $")
        self.assessment_value = tkinter.StringVar()
        self.show_assess_value = tkinter.Label(self.mid_frame1, textvariable = self.assessment_value)
        self.display_message1.pack(side="left")
        self.show_assess_value.pack(side="left")
        self.display_message2 = tkinter.Label(self.mid_frame2, text="Property tax is: $")
        self.tax_value = tkinter.StringVar()
        self.show_tax_value = tkinter.Label(self.mid_frame2, textvariable = self.tax_value)
        self.display_message2.pack(side="left")
        self.show_tax_value.pack(side="left")
        self.calc_button = tkinter.Button(self.bottom_frame, text = "Calculate the values", command = self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame, text="Quit", bg="red", command=self.main_window.destroy)
        self.calc_button.pack(side="left")
        self.quit_button.pack(side="left")
        self.top_frame.pack()
        self.mid_frame1.pack()
        self.mid_frame2.pack()
        self.bottom_frame.pack()
        self.main_window.mainloop()

    def convert(self):
        self.assessed_value = float(self.entry_act_value.get()) * 0.60
        self.calculated_tax = self.assessed_value * (0.75 / 100)
        self.assessment_value.set(format(self.assessed_value, ",.2f"))
        self.tax_value.set(format(self.calculated_tax, ",.2f"))


example = PropertyTaxGUI()
