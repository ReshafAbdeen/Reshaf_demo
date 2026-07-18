# Unit & Temperature Converter

def convert_units():
    print("\n--- Unit Converter ---")
    print("1. Kilometers to Miles")
    print("2. Miles to Kilometers")
    print("3. Celsius to Fahrenheit")
    print("4. Fahrenheit to Celsius")
    choice = input("Choose an option (1-4): ")
    if choice not in ['1', '2', '3', '4']:
        print("Invalid choice!")
        return
    try:
        val = float(input("Enter value to convert: "))
        if choice == '1':
            print(f"{val} km = {val * 0.621371:.2f} miles")
        elif choice == '2':
            print(f"{val} miles = {val / 0.621371:.2f} km")
        elif choice == '3':
            print(f"{val}°C = {(val * 9/5) + 32:.2f}°F")
        elif choice == '4':
            print(f"{val}°F = {(val - 32) * 5/9:.2f}°C")
    except ValueError:
        print("Please enter a valid number.")
while True:
    convert_units()
    again = input("Convert another? (y/n): ").lower()
    if again != 'y':
        print("Exiting Converter...")
        break
# End of program
print("Goodbye!")