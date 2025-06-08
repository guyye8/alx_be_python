def perform_operation(num1, num2, operation):
    op = operation.lower()
    if op == 'add':
        return num1 + num2
    if op == 'subtract':
        return num1 - num2
    if op == 'multiply':
        return num1 * num2
    if op == 'divide':
        return None if num2 == 0 else num1 / num2
    return None
