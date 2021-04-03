# 5. Write a statement that creates a Button widget. Its parent should be self.button_
# frame, its text should be 'Calculate', and its callback function should be the self.
# calculate method.

self.calcul_button = tkinter.Button(self.button_frame, text="Calculate", command=self.calculate)