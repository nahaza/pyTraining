# 2. Latin Translator
# Look at the following list of Latin words and their meanings:
# Latin English
# sinister left
# dexter right
# medium center
# Write a GUI program that translates the Latin words to English. The window should have
# three buttons, one for each Latin word. When the user clicks a button, the program displays
# the English translation in a label.

import tkinter


class TranslatorGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.geometry("350x350")
        self.main_window.title("Latin to English")
        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        self.transl1 = tkinter.StringVar()
        self.transl2 = tkinter.StringVar()
        self.transl3 = tkinter.StringVar()
        self.transl_label1 = tkinter.Label(self.top_frame, textvariable=self.transl1)
        self.transl_label2 = tkinter.Label(self.mid_frame, textvariable=self.transl2)
        self.transl_label3 = tkinter.Label(self.bottom_frame, textvariable=self.transl3)
        self.buttton1 = tkinter.Button(self.top_frame, text="sinister", command=self.word1)
        self.buttton2 = tkinter.Button(self.mid_frame, text="dexter", command=self.word2)
        self.buttton3 = tkinter.Button(self.bottom_frame, text="medium", command=self.word3)
        self.buttton1.pack(side='left')
        self.buttton2.pack(side='left')
        self.buttton3.pack(side='left')
        self.transl_label1.pack(side='right')
        self.transl_label2.pack(side='right')
        self.transl_label3.pack(side='right')
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()
        self.main_window.mainloop()

    def word1(self):
        self.word1.set('left')

    def word2(self):
        self.word2.set('right')

    def word3(self):
        self.word3.set('center')


myGUI = TranslatorGUI()
