"""
How to use test class to wrap methods under one class -> which is "test_class_demo"
Learn about 'autouse' keywords in fixtures
Assert the result to create a real test scenario
"""

class SomeClassToTest: # Class

    def __init__(self, num1=0): # Constructor
        self.num1 = num1


    def sum_numbers(self, num2, num3):
        return self.num1 + num2 + num3

