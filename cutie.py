python_students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
scores = sorted(list(set([scores for names, scores in python_students])))
second_lowest = scores[1]
names = [names for names, scores in python_students if scores == second_lowest]
names.sort()
for name in names:
    print(name)