# temp_conversion_tool.py
# Demonstrates variable scope using global conversion factors

# ---- Global conversion factors ----
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# ---- Conversion functions ----
def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# ---- Main program (User Interaction) ----
def main():
    try:
        # Ask user for input
        temp_input = input("Enter the temperature to convert: ")

        # Check if it's numeric
        if not temp_input.replace(".", "", 1).isdigit():
            raise ValueError("Invalid temperature. Please enter a numeric value.")

        temp = float(temp_input)

        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == "F":
            result = convert_to_celsius(temp)
            print(f"{temp}°F is {result}°C")
        elif unit == "C":
            result = convert_to_fahrenheit(temp)
            print(f"{temp}°C is {result}°F")
        else:
            raise ValueError("Invalid unit. Please enter C or F.")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
