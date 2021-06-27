"""
created by Nagaj at 27/06/2021
"""
from operator import Eq, Lt, Le, Ge, Gt


class Age:
    INVALID_INT = "Invalid Value of Int {}"
    INVALID_AGE = "Age Can not be {}"

    def __init__(self, value):
        self.value = value
        self.error = None

    def __repr__(self):
        return f"Age(value={self.value})"

    def __setattr__(self, key, value):
        if key == "value":
            try:
                value = int(value)
            except ValueError:
                self.error = self.INVALID_INT.format(value)

            if value not in range(1, 120):
                self.error = self.INVALID_AGE.format(value)

        return super().__setattr__(key, value)

    @staticmethod
    def is_valid_number(other):
        return isinstance(other, (int, float))

    def is_valid_age(self, other):
        return self.__class__ == other.__class__

    def __le__(self, other):
        le = Le()
        return le.perform(self, other)

    def __lt__(self, other):
        lt = Lt()
        return lt.perform(self, other)

    def __eq__(self, other):
        eq = Eq()
        return eq.perform(self, other)

    def __gt__(self, other):
        gt = Gt()
        return gt.perform(self, other)

    def __ge__(self, other):
        ge = Ge()
        return ge.perform(self, other)
