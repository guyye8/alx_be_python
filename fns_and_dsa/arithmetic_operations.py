def perform_operation(num1: float, num2: float, operation: str) -> float:
    """
    Performs basic arithmetic operations on two numbers.
    
    Args:
        num1: First number
        num2: Second number
        operation: Type of operation ('add', 'subtract', 'multiply', 'divide')
    
    Returns:
        Result of the arithmetic operation or None for invalid operations/division by zero
    """
    operation = operation.lower().strip()
    
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return None  # Or you could return "Error: Division by zero"
        return num1 / num2
    else:
        return None  # Invalid operation
