"""
created by Nagaj at 27/06/2021
"""

from abc import ABC, abstractmethod


class Operator(ABC):  # pylint: disable=R0903
    """"
    abstract class for operator actions
    """

    @abstractmethod
    def perform(self, age, other):  # pylint: disable=C0116
        pass


class Equal(Operator):  # pylint: disable=R0903
    """
    perform eq functionality
    """

    def perform(self, age, other):
        """
        check if age == other obj[age, int, float]
        :param age: age obj
        :param other: age, int, float obj
        :return:
        """
        if age.is_valid_age(other):
            return age.value == other.value
        if age.is_valid_number(other):
            return age.value == other
        return None


class LessThan(Operator):  # pylint: disable=R0903
    """
    perform lt functionality
    """

    def perform(self, age, other):
        """
           check if age <= other obj[age, int, float]
           :param age: age obj
           :param other: age, int, float obj
           :return:
        """
        if age.is_valid_age(other):
            return age.value < other.value
        if age.is_valid_number(other):
            return age.value < other

        return None


class LessThanOrEqual(Operator):  # pylint: disable=R0903
    """
        perform less equal functionality
    """

    def perform(self, age, other):
        """
           check if age < other obj[age, int, float]
           :param age: age obj
           :param other: age, int, float obj
           :return:
        """

        if age.is_valid_age(other):
            return age.value <= other.value
        if age.is_valid_number(other):
            return age.value <= other

        return None


class GreaterThan(Operator):  # pylint: disable=R0903
    """
        perform greater than functionality
    """

    def perform(self, age, other):
        """
           check if age > other obj[age, int, float]
           :param age: age obj
           :param other: age, int, float obj
           :return:
        """
        if age.is_valid_age(other):
            return age.value > other.value
        if age.is_valid_number(other):
            return age.value > other

        return None


class GreaterThanOrEqual(Operator):  # pylint: disable=R0903
    """
            perform greater than or equal functionality
    """

    def perform(self, age, other):
        """
           check if age >= other obj[age, int, float]
           :param age: age obj
           :param other: age, int, float obj
           :return:
        """
        if age.is_valid_age(other):
            return age.value >= other.value
        if age.is_valid_number(other):
            return age.value >= other

        return None
