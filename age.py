"""
created by Nagaj at 27/06/2021
"""
from collections import namedtuple

from operator_ import Equal, LessThan, LessThanOrEqual, GreaterThan, GreaterThanOrEqual

MONTHS_IN_YEAR = 12
WEEKS_IN_YEAR = 52
DAYS_IN_YEAR = 365
MIN_AGE = 1
MAX_AGE = 120


class Age:
    """
    present age
    """

    INVALID_INT = "Invalid Integer Value for {}"
    INVALID_AGE = "Age Can not be {}. accept only from 1 to 120"
    EMPTY = "Empty Age, Please Type Your Age."

    def __init__(self, value):
        self.value = value
        self.AgeInNumbers = namedtuple(  # pylint: disable=C0103
            "AgeInNumbers", ["months", "weeks", "days"]
        )  # pylint: disable=C0103

    def __repr__(self):
        return f"Age(value={self.value})"

    def __setattr__(self, key, value):
        error = None
        if key == "value":
            try:
                value = int(value)
                if value not in range(MIN_AGE, MAX_AGE):
                    error = self.INVALID_AGE.format(value)

            except ValueError:
                if value == "":
                    error = self.EMPTY
                else:
                    error = self.INVALID_INT.format(value)

            setattr(self, "error", error)
        super().__setattr__(key, value)

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
        months = self.value * MONTHS_IN_YEAR
        weeks = self.value * WEEKS_IN_YEAR
        days = self.value * DAYS_IN_YEAR
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
