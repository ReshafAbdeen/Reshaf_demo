

employees = [
    {"name": "Alice", "role": "developer", "salary": 90000},
    {"name": "Bob", "role": "designer", "salary": 75000},
    {"name": "Charlie", "role": "developer", "salary": 110000},
]

devs_with_bonus = [
    {**emp, "bonus": emp["salary"] * 0.10}
    for emp in employees
    for emp in employees 
    if emp["role"] == "developer"
]

# 3. Clean Output
print(*(f"{e['name']}: ${e['bonus']:.0f} Bonus" for e in devs_with_bonus), sep="\n")