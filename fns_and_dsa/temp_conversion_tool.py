# Global conversion factors
FAHRENHEIT_TO_CELSIUS = 5.0 / 9.0
CELSIUS_TO_FAHRENHEIT = 9.0 / 5.0

def convert_f_to_c(f_temp):
    """Convert Fahrenheit to Celsius"""
    return (f_temp - 32) * FAHRENHEIT_TO_CELSIUS

def convert_c_to_f(c_temp):
    """Convert Celsius to Fahrenheit"""
    return c_temp * CELSIUS_TO_FAHRENHEIT + 32

def main():
    try:
        temp = float(input("Enter temperature: "))
        unit = input("Celsius or Fahrenheit (C/F): ").upper()
        
        if unit == 'C':
            result = convert_c_to_f(temp)
            print(f"{temp}C = {result}F")
        elif unit == 'F':
            result = convert_f_to_c(temp)
            print(f"{temp}F = {result}C")
        else:
            print("Invalid unit. Enter C or F.")
    except ValueError:
        print("Invalid temperature. Enter a number.")

if __name__ == "__main__":
    main()
