#!/usr/bin/python3
""" Defines a class Student."""


class Student:
    """Represent a class Student"""

    def __init__(self, first_name, last_name, age):
        """init our data

        Args:
            first_name (str): the first name
            last_name (str): the last name
            age (int): the age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ return a dicts from an obj """
        return self.__dict__
