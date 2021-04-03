# 6. Write a statement that creates a Button widget that closes the program when it is
# clicked. Its parent should be self.button_frame, and its text should be 'Quit'.

self.quit_button = tkinter.Button(self.button_frame, text="Quit", command=self.button_frame.destroy)