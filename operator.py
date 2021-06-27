"""
created by Nagaj at 27/06/2021
"""

from abc import ABC, abstractmethod


class Operator(ABC):
    @abstractmethod
    def perform(self, age, other):
        pass


class Eq(Operator):
    def perform(self, age, other):
        if age.is_valid_age(other):
            return age.value == other.value
        if age.is_valid_number(other):
            return age.value == other


class Lt(Operator):
    def perform(self, age, other):
        if age.is_valid_age(other):
            return age.value < other.value
        if age.is_valid_number(other):
            return age.value < other


class Le(Operator):
    def perform(self, age, other):
        if age.is_valid_age(other):
            return age.value <= other.value
        if age.is_valid_number(other):
            return age.value <= other


class Gt(Operator):
    def perform(self, age, other):
        if age.is_valid_age(other):
            return age.value > other.value
        if age.is_valid_number(other):
            return age.value > other


class Ge(Operator):
    def perform(self, age, other):
        if age.is_valid_age(other):
            return age.value >= other.value
        if age.is_valid_number(other):
            return age.value >= other
