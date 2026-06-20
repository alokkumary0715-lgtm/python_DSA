"""Hide unnecessary details from clients and show only that which is necessary"""
"""Think of a car:

You use the steering wheel, brake, and accelerator.
You don't need to know how the engine works internally.

This is abstraction: show what is necessary, hide what is unnecessary."""


#with abstraction
from abc import ABC, abstractmethod

class Employee(ABC):

    @classmethod
    @abstractmethod
    def company_name(cls):
        pass


class Developer(Employee):

    @classmethod
    def company_name(cls):
        print("nice")


Developer.company_name()

