"""
How to use test class to wrap methods under one class -> which is "test_class_demo"
Learn about 'autouse' keywords in fixtures
Assert the result to create a real test scenario
"""

class SomeClassToTest: # Class

    def __init__(self, num3=0): # Constructor
        self.num3 = num3


    def sum_numbers(self, num1, num2):
        return num1 + num2 + self.num3

