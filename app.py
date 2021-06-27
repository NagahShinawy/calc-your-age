"""
created by Nagaj at 27/06/2021
"""
from config import AgeUI


if __name__ == '__main__':
    ui = AgeUI()
    ui.config(title="Calc Your Age", is_center=True,  width=500, height=300)
    ui.run()