# 6. Joe’s Automotive
# Joe’s Automotive performs the following routine maintenance services:
# • Oil change—$30.00
# • Lube job—$20.00
# • Radiator flush—$40.00
# • Transmission flush—$100.00
# • Inspection—$35.00
# • Muffler replacement—$200.00
# • Tire rotation—$20.00
# Write a GUI program with check buttons that allow the user to select any or all of these
# services. When the user clicks a button, the total charges should be displayed.

import tkinter as tk
from tkinter import messagebox, Canvas

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Joe's Automotive")
        self.master.geometry("560x560")
        self.master.resizable(False, False)
        self.pack()
        self.main_window()

    def main_window(self):
        self.top_frame = tk.Frame(self.master)
        self.mid_frame = tk.Frame(self.master)
        self.bottom_frame = tk.Frame(self.master)
        self.head = tk.Label(self.top_frame, text='Welcome')
        self.service_head = tk.Label(self.top_frame,"Service")
        self.charge_head = tk.Label(self.top_frame,"Charges")
        self.check_1 = tk.IntVar()
        self.check_2 = tk.IntVar()
        self.check_3 = tk.IntVar()
        self.check_4 = tk.IntVar()
        self.check_5 = tk.IntVar()
        self.check_6 = tk.IntVar()
        self.check_7 = tk.IntVar()
        self.check_1.set(0)
        self.check_2.set(0)
        self.check_3.set(0)
        self.check_4.set(0)
        self.check_5.set(0)
        self.check_6.set(0)
        self.check_7.set(0)
        self.chckbox_1 = tk.Checkbutton(self.mid_frame, text='Oil Change 30$\n', variable=self.check_1)
        self.chckbox_2 = tk.Checkbutton(self.mid_frame, text='Lube Job 20$\n', variable=self.check_2)
        self.chckbox_3 = tk.Checkbutton(self.mid_frame, text='Radiator Flush 40$\n', variable=self.check_3)
        self.chckbox_4 = tk.Checkbutton(self.mid_frame, text='Transmission Flush 100$\n', variable=self.check_4)
        self.chckbox_5 = tk.Checkbutton(self.mid_frame, text='Inspection 35$\n', variable=self.check_5)
        self.chckbox_6 = tk.Checkbutton(self.mid_frame, text='Muffler Replacement 200$\n', variable=self.check_6)
        self.chckbox_7 = tk.Checkbutton(self.mid_frame, text='Tire Rotation 20$\n', variable=self.check_7)
        self.calc_btn = tk.Button(self.bottom_frame, text='Total Charge', variable=self.get_total)
        self.total_desc = tk.Label(self.bottom_frame, text='Total Charge')
        self.sum_str = tk.StringVar()
        self.total_val=tk.Label(self.bottom_frame, textvariable=self.sum_str)
        self.calc_btn.pack()
        self.head.pack(anchor='c')
        self.service_head.pack(side='left', anchor='w')
        self.charge_head.pack(anchor='e')
        self.chckbox_1.pack(anchor='w')
        self.chckbox_2.pack(anchor='w')
        self.chckbox_3.pack(anchor='w')
        self.chckbox_4.pack(anchor='w')
        self.chckbox_5.pack(anchor='w')
        self.chckbox_6.pack(anchor='w')
        self.chckbox_7.pack(anchor='w')
        self.calc_btn.pack()
        self.total_desc.pack()
        self.total_val.pack()
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

    def get_total(self):
        self.sum = 0.00
        if self.check_1.get() == 1:
            self.sum +=30.00
        if self.check_2.get() == 1:
            self.sum +=20.00
        if self.check_3.get() == 1:
            self.sum +=40.00
        if self.check_4.get() == 1:
            self.sum +=100.00
        if self.check_5.get() == 1:
            self.sum +=35.00
        if self.check_6.get() == 1:
            self.sum +=200.00
        if self.check_7.get() == 1:
            self.sum +=20.00
        self.sum_str.set(self.sum)


root = tk.Tk()
app = Application(master=root)
app.mainloop()