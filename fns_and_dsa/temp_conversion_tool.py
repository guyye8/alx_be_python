# Define global conversion factors
FAHRENHEIT_TO_CELSIUS = 5 / 9
CELSIUS_TO_FAHRENHEIT = 9 / 5

def fahrenheit_to_celsius(f_temp):
    """Convert Fahrenheit temperature to Celsius"""
    return (f_temp - 32) * FAHRENHEIT_TO_CELSIUS

def celsius_to_fahrenheit(c_temp):
    """Convert Celsius temperature to Fahrenheit"""
    return (c_temp * CELSIUS_TO_FAHRENHEIT) + 32

def main():
    print("Temperature Conversion Tool")
    
    try:
        temp = float(input("Enter temperature value: "))
        unit = input("Convert from (C/F): ").upper()
        
        if unit == 'C':
            converted = celsius_to_fahrenheit(temp)
            print(f"{temp}°C = {converted:.2f}°F")
        elif unit == 'F':
            converted = fahrenheit_to_celsius(temp)
            print(f"{temp}°F = {converted:.2f}°C")
        else:
            print("Error: Please enter 'C' or 'F' for temperature unit")
    except ValueError:
        print("Error: Please enter a valid numeric temperature")

if __name__ == "__main__":
    main()
