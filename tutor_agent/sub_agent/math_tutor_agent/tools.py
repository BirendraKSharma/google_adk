def calculator(a: float, b: float, operation: str) -> float:
    """
    Perform basic arithmetic operations.

    Args:
        a (float): The first number.
        b (float): The second number.
        operation (str): The operation to perform ('add', 'subtract', 'multiply', 'divide').

    Returns:
        float: The result of the operation.

    Raises:
        ValueError: If the operation is not recognized or if division by zero is attempted.
    """
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
    else:
        raise ValueError(f"Operation '{operation}' is not recognized.")
    
# Example usage:
# result = calculator(10, 5, 'add')
# print(result)  # Output: 15