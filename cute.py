# BMI (Body Mass Index) Calculator

def calculate_bmi(weight, height):
    return weight / (height ** 2)
def get_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"
print("--- BMI Calculator ---")
while True:
    print("\nEnter 'q' to quit at any time.")
    w_input = input("Enter your weight in kg: ")
    if w_input.lower() == 'q': break
    h_input = input("Enter your height in meters (e.g. 1.75): ")
    if h_input.lower() == 'q': break
    try:
        weight = float(w_input)
        height = float(h_input)
        if weight <= 0 or height <= 0:
            print("Values must be greater than zero!")
            continue
        bmi_value = calculate_bmi(weight, height)
        category = get_category(bmi_value)
        print(f"\nYour BMI is: {bmi_value:.2f}")
        print(f"Health Category: {category}")
    except ValueError:
        print("Invalid input! Please enter numbers only.")