import tkinter
from tkinter import messagebox
import applicants


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Applicant full info")
        self.main_window.geometry("300x100")
        self.top_frame = tkinter.Frame(self.main_window)
        self.mid1_frame = tkinter.Frame(self.main_window)
        self.prompt_label = tkinter.Label(self.top_frame, text="Name: ")
        self.entry_name = tkinter.Entry(self.top_frame)
        self.prompt_label.pack(side='left')
        self.entry_name.pack(side='left')
        self.show_info_button = tkinter.Button(self.mid1_frame, text="Show info",
                                               command=self.show_info)
        self.show_grades_button = tkinter.Button(self.mid1_frame, text="Show grades",
                                                 command=self.show_grades)
        self.show_info_button.pack(side='left')
        self.show_grades_button.pack(side='left')
        self.top_frame.pack()
        self.mid1_frame.pack()
        self.main_window.mainloop()

    def show_info(self):
        messagebox.showinfo("Applicant's info", applicants.get_info_by_applicant_name(self.entry_name.get()))

    def show_grades(self):
        messagebox.showinfo("Applicant's grades", applicants.get_grades_by_applicant_name(self.entry_name.get()))
