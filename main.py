# This is a sample Python script.

import random

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


primerNumero = random.randint(1,6)
SegundoNumero =random.randint(1,6)
print(f"El primer dado es: {primerNumero}")
print(f"El segundo dado es: {SegundoNumero}")
print(f"El resultado es {primerNumero+ SegundoNumero}")