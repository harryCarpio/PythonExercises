"""
The objective is to write an interactive calculator. User input is assumed to be a formula that consists of a number, an
 operator (at least + and -), and another number, separated by white space (e.g. 1 + 1). Split user input and check w
 hether the resulting list is valid:
    * If the input does not consist of 3 elements, raise a FormulaError, which is a custom Exception.
    * Convert the first and third input to a float. Handle any ValueError that occurs, and instead raise a FormulaError.
    * If the second input is not '+' or '-', again raise a FormulaError.
If the input is valid, perform the calculation and print out the result. The user is then prompted to provide new input,
and so on, until the user enters quit.
An interaction could look like this:
    >>> 1 + 1
    2.0
    >>> 3.2 - 1.5
    1.7000000000000002
    >>> quit

"""


class FormulaError(Exception):
    def __init__(self, custom_message):
        self.message = custom_message


if __name__ == '__main__':
    operation = ""

    while operation != "quit":
        operation = input(">>> ")
        if operation != "quit":
            op_elements = operation.split(" ")
            if len(op_elements) != 3:
                error_message = "Wrong format! User 'number +/- number'. For example '1 + 1' or 10 - 6"
                raise FormulaError(error_message)

            try:
                first_num = float(op_elements[0])
                second_num = float(op_elements[2])
            except ValueError as valErr:
                raise FormulaError(valErr.args[0]) from None

            operator = op_elements[1]
            if not (operator == '+' or operator == '-'):
                error_message = "Wrong format! Operator should be + or -"
                raise FormulaError(error_message)

            if operator == '+':
                print(first_num + second_num)
            elif operator == '-':
                print(first_num - second_num)