def add_numbers(num1, num2):
    return num1 + num2


print(add_numbers(2, 4))
print('-------------------')


# Positional Parameters
# def multiply_numbers(num1=1, num2=1):
#     return num1 * num2

def multiply_numbers(num1=1, num2=1):
    return num1 * num2


print(multiply_numbers(2, 4))
print(multiply_numbers(2))
print(multiply_numbers())

print(multiply_numbers(num1=2, num2=8))
print(multiply_numbers(num2=2, num1=8))
print(multiply_numbers(num2=8))