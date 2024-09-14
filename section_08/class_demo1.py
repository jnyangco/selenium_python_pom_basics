"""
Object Oriented Programming
"""


class Car(object):
    def __init__(self, make, model="Default Car Model"):  # init -> is like Constructor
        self.make = make  # code can be -> self.brand = make
        self.model = model


c1 = Car('Bmw')
print(c1.make)
print(c1.model)

print('---------------------')
c2 = Car('Mazda', 'CX5')
print(c2.make)
print(c2.model)