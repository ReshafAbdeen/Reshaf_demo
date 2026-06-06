info = [
    ('Zaynul', 'Math'),
    ('Yasmin', 'Arabic'),
    ('Cutie', 'englice'),
    ('Zaynul', 'Science'),
    ('Yasmin', 'Urdu'),
    ('Varish', 'Math')
]

dict = {}
for name, courses in info:
  if(dict.get(name) == None): 
    dict.update({name:set()})
    dict[name].add(courses)
  else:
    dict[name].add(courses)
print(dict)