
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

        choice = input("Select input (1-5): ")

        if choice == "1":
            celsius = float(input("ป้อนอุณหภูมิ (°C): "))
            result = celsius_to_fahrenheit(celsius)
            print(f"{celsius}°C = {result:.2f}°F")

        elif choice == "2":
            fahrenheit = float(input("ป้อนอุณหภูมิ (°F): "))
            result = fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit}°F = {result:.2f}°C")

        elif choice == "3":
            km = float(input("ป้อนระยะทาง (กิโลเมตร): "))
            result = km_to_miles(km)
            print(f"{km} km = {result:.2f} miles")

        elif choice == "4":
            miles = float(input("ป้อนระยะทาง (ไมล์): "))
            result = miles_to_km(miles)
            print(f"{miles} miles = {result:.2f} km")

        elif choice == "5":
            print("ขอบคุณ!")
            break

        else:
            print("กรุณาเลือกตัวเลข 1-5 เท่านั้น")


if __name__ == "__main__":
    main()