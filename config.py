"""
created by Nagaj at 27/06/2021
"""
from tkinter import Tk


class AgeUI(Tk):
    """"
    ui class for app
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def config(self, title, image=None, is_center=False, **kwargs):
        """

        :param title: window title
        :param image: image title bar
        :param is_center: window to center ?
        :param kwargs: more options like widht, height
        :return:
        """
        self.title(title)
        super().config(**kwargs)
        if is_center:
            self.center(self["width"], self["height"])
        if image:
            self.iconbitmap(image)

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
        """
        keep app opened
        :return:
        """
        self.mainloop()
