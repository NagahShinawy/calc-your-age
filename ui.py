"""
created by Nagaj at 27/06/2021
"""
from tkinter import Tk, Entry, StringVar, Button, messagebox

from age import Age

KNOW_YOUR_NUMBERS = "Know Your Numbers"


class AgeUI(Tk):
    """"
    ui class for app
    """

    DEFAULT_FONT_CONFIG = ("Arial", 30)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.age_input = None

    def config(self, title, image=None, is_center=False, **kwargs):
        """

        :param title: window title
        :param image: image title bar
        :param is_center: window to center ?
        :param kwargs: more options like width, height
        :return:
        """
        self.title(title)
        super().config(**kwargs)
        if is_center:
            self.center(self["width"], self["height"])
        if image:
            self.iconbitmap(image)
        self.default_value()
        self.create_calc_btn()

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

    def default_value(self):
        """
        set default value for age and init entry input
        :return:
        """
        default_age_value = StringVar()
        default_age_value.set("01")
        self.age_input = Entry(
            width=2, font=self.DEFAULT_FONT_CONFIG, textvariable=default_age_value
        )
        self.age_input.pack()

    def create_calc_btn(self):
        """
        create btn and trigger it with calc age in numbers
        :return:
        """
        btn = Button(
            text="Calculate Age",
            width=20,
            height=2,
            bg="#e91e63",
            fg="white",
            borderwidth=0,
            command=self.show_your_numbers,
        )
        btn.pack()

    def show_your_numbers(self):
        """
        show numbers in message box, knowYourNumbers (kyn)
        :return:
        """
        age = Age(self.age_input.get())
        if age.error:
            message = age.error
            show = messagebox.showerror
        else:
            kyn = age.know_your_numbers()
            message = "\n".join([f"{kyn.months} Months", f"{kyn.weeks} Weeks", f"{kyn.days} Days"])
            show = messagebox.showinfo

        show(title=KNOW_YOUR_NUMBERS, message=message)

    def run(self):
        """
        keep app opened
        :return:
        """
        self.mainloop()
