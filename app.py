"""
created by Nagaj at 27/06/2021
"""
from config import AgeUI

IMAGE = "./static/age.ico"
TITLE_BAR = "Calc Your Age"


if __name__ == "__main__":
    ui = AgeUI()
    ui.config(title=TITLE_BAR, image=IMAGE, is_center=True, width=500, height=300)
    ui.run()
