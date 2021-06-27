"""
created by Nagaj at 27/06/2021
"""
from collections import namedtuple

from operator import Equal, LessThan, LessThanOrEqual, GreaterThan, GreaterThanOrEqual


class Age:
    """
    present age
    """

    INVALID_INT = "Invalid Value of Int {}"
    INVALID_AGE = "Age Can not be {}"

    def __init__(self, value):
        self.value = value
        self.error = None
        self.AgeInNumbers = namedtuple(  # pylint: disable=C0103
            "AgeInNumbers", ["months", "weeks", "days"]
        )  # pylint: disable=C0103

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

    def know_your_numbers(self):
        """
        calc age from years to months, weeks, days
        :return:
        """
        months = self.value * 12
        weeks = self.value * 52
        days = self.value * 365
        return self.AgeInNumbers(months=months, weeks=weeks, days=days)

    def is_valid(self, other):
        """
        check if other age obj to compare
        :param other:
        :return:
        """
        return self.__class__ == other.__class__

    def __le__(self, other):
        return LessThanOrEqual().perform(self, other)

    def __lt__(self, other):
        return LessThan().perform(self, other)

    def __eq__(self, other):
        return Equal().perform(self, other)

    def __gt__(self, other):
        return GreaterThan().perform(self, other)

    def __ge__(self, other):
        return GreaterThanOrEqual().perform(self, other)
