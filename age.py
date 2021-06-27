"""
created by Nagaj at 27/06/2021
"""
from operator import Eq, Lt, Le, Ge, Gt


class Age:
    """
    present age
    """

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
        """
        check if other is valid number int, float type
        :param other:
        :return:
        """
        return isinstance(other, (int, float))

    def is_valid_age(self, other):
        """
        check if other age obj to compare
        :param other:
        :return:
        """
        return self.__class__ == other.__class__

    def __le__(self, other):
        return Le().perform(self, other)

    def __lt__(self, other):
        return Lt().perform(self, other)

    def __eq__(self, other):
        return Eq().perform(self, other)

    def __gt__(self, other):
        return Gt().perform(self, other)

    def __ge__(self, other):
        return Ge().perform(self, other)
