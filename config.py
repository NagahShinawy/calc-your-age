"""
created by Nagaj at 27/06/2021
"""
from tkinter import *


class AgeUI(Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def config(self, title, is_center=False, **kwargs):
        self.title(title)
        super().config(**kwargs)
        if is_center:
            self.center(self["width"], self["height"])

    def center(self, window_width, window_height) -> None:
        """
        add window to the center of screen
        :param window_width: width of the window
        :param window_height: height of the window
        :return:
        """
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))
        self.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

    def run(self):
        self.mainloop()
