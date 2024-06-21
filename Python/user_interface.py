"""
User Input

A user interface contains two types of user input controls: Textinput,
which accepts all characters and Numericinput, which accepts only digits.

Implement the class Textinput that contains:

Method add(self, character) - adds the given character to the current value

Method get_value(self) - returns the current value

Implement the class Numericinput that

Inherits TextInput

Overrides the add method so that each non-numeric character is ignored

For example, the following code should output 10:

input NumericInput()

input.add("1")

input.add("a")

input.add("0")


print(input.get_value())
"""



class TextInput:
    # current_value = ""

    def __init__(self):
        self.current_value = ""

    def add(self, value):
        self.current_value += value

    def get_value(self):
        return self.current_value


class NumericInput(TextInput):

    def __init__(self):
        super().__init__()

    def add(sef, value):
        if value.isnumeric():
            sef.current_value += value

if __name__ == '__main__':
   input = NumericInput()
   input.add("1")
   input.add("a")
   input.add("0")
   print(input.get_value())