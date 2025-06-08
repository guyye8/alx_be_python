# temp_conversion_tool.py

# 1️⃣ Definition of Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# 2️⃣ Implement Conversion Functions

def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius.
    """
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.
    """
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

# 3️⃣ User Interaction + Implementation of ValueError Handling

def main():
    try:
        # Prompt user to enter temperature
        temp_input = input("Enter the temperature to convert: ").strip()

        # Attempt to convert input to float → if invalid, ValueError is raised here
        temperature = float(temp_input)

        # Prompt user to specify unit
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        # Perform conversion based on unit
        if unit == 'F':
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature:.2f}°F is {converted_temp:.2f}°C")
        elif unit == 'C':
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature:.2f}°C is {converted_temp:.2f}°F")
        else:
            # Invalid unit entered
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError as e:
        # Catch any ValueError — either from invalid number or from invalid unit
        print(f"Invalid temperature. Please enter a numeric value.\nError: {e}")

# 4️⃣ (Optional) Unit Tests — for grading or self-check

def run_tests():
    print("\nRunning tests...")
    assert round(convert_to_celsius(32), 2) == 0.00
    assert round(convert_to_celsius(212), 2) == 100.00
    assert round(co
