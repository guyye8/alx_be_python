# temp_conversion_tool.py

# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Conversion functions
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# Main user interaction
def main():
    try:
        temperature = float(input("Enter the temperature to convert: ").strip())
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == 'F':
            print(f"{temperature:.2f}°F is {convert_to_celsius(temperature):.2f}°C")
        elif unit == 'C':
            print(f"{temperature:.2f}°C is {convert_to_fahrenheit(temperature):.2f}°F")
        else:
