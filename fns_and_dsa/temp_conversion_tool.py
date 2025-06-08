# Global conversion factors
FAHRENHEIT_TO_CELSIUS = 5/9
CELSIUS_TO_FAHRENHEIT = 9/5

def convert_to_celsius(f): return (f-32)*FAHRENHEIT_TO_CELSIUS
def convert_to_fahrenheit(c): return c*CELSIUS_TO_FAHRENHEIT+32

def main():
    try:
        temp = float(input("Enter temperature: "))
        unit = input("Celsius or Fahrenheit (C/F): ").upper()
        if unit == 'C':
            print(f"{temp}°C = {convert_to_fahrenheit(temp):.1f}°F")
        elif unit == 'F':
            print(f"{temp}°F = {convert_to_celsius(temp):.1f}°C")
        else:
            print("Invalid unit. Please enter C or F.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()
