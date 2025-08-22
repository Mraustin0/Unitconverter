
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def km_to_miles(kilometers):
    return kilometers * 0.621371

def miles_to_km(miles):
    return miles / 0.621371

def main():
    while True:
        print("\n=== Unit Converter Menu ===")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Kilometers to Miles")
        print("4. Miles to Kilometers")
        print("5. Exit")


if __name__ == "__main__":
    main()
