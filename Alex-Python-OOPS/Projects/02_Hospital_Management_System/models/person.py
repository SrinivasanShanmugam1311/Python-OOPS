# ============================================================
# Project 02 : Hospital Management System
# File        : models/person.py
# Purpose     : Base class for people in the hospital
# ============================================================


class Person:
    """
    Base class representing a person.

    Common information:
        - ID
        - Name
        - Age
        - Phone
    """

    def __init__(self, person_id, name, age, phone):

        self.person_id = person_id
        self.name = name
        self.age = age
        self.phone = phone

    def display(self):
        """
        Display basic person information.
        """

        print("ID    :", self.person_id)
        print("Name  :", self.name)
        print("Age   :", self.age)
        print("Phone :", self.phone)

    def __str__(self):
        """
        Return a readable representation.
        """

        return f"{self.person_id} - {self.name}"