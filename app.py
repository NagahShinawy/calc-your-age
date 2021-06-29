"""
created by Nagaj at 27/06/2021
"""
from ui import AgeUI

IMAGE = "./static/age.ico"
TITLE_BAR = "Calc Your Age [Know Your Numbers]"
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 300


if __name__ == "__main__":
    ui = AgeUI()
    ui.config(title=TITLE_BAR, image=IMAGE, is_center=True, width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    ui.run()
