def calculate(operation, a, b, make_int=False, message='The result is'):
    """Perform operation on a + b, ()possibly truncating) & returning w/msg.

    - operation: 'add', 'subtract', 'multiply', or 'divide'
    - a and b: values to operate on
    - make_int: (optional, defaults to False) if True, truncates to integer
    - message: (optional) message to use (if not provided, use 'The result is')

    Performs math operation (truncating if make_int), then returns as
    "[message] [result]"

        >>> calculate('add', 2.5, 4)
        'The result is 6.5'

        >>> calculate('subtract', 4, 1.5, make_int=True)
        'The result is 2'

        >>> calculate('multiply', 1.5, 2)
        'The result is 3.0'

        >>> calculate('divide', 10, 4, message='I got')
        'I got 2.5'

    If a valid operation isn't provided, return None.

        >>> calculate('foo', 2, 3)

    """
    # add function
    if operation == "add" and make_int == False:
        return f"{message} {a + b}"
    elif operation == "add" and make_int == True:
        integer_a = int(a)
        integer_b = int(b)
        return f"{message} {integer_a + integer_b}"

    # subtract function

    if operation == "subtract" and make_int == False:
        return f"{message} {a - b}"
    elif operation == "subtract" and make_int == True:
        integer_a = int(a)
        integer_b = int(b)
        return f"{message} {integer_a - integer_b}"

    # multiply function

    if operation == "multiply" and make_int == False:
        return f"{message} {a * b}"
    elif operation == "multiply" and make_int == True:
        integer_a = int(a)
        integer_b = int(b)
        return f"{message} {integer_a * integer_b}"

    # division function

    if operation == "divide" and make_int == False:
        return f"{message} {a / b}"
    elif operation == "divide" and make_int == True:
        integer_a = int(a)
        integer_b = int(b)
        return f"{message} {integer_a / integer_b}"

    # error message
    if (operation != "add" or "subtract") or (operation != "multiply" or operation != "divide"):
        return "Please enter add, subtract, divide, or multiply as a function"
