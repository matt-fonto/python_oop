person = {"name":"Matt", "age":28}
print(person["name"]) # in python, we can't access dictionary properties with dot notation `person.name`, as we would in JS

# In Python, dictionaries require the use of bracket notation `person["age"]`

people = [
    {"name": "Alice", "age": 30, "profession": "Teacher"},
    {"name": "Bob", "age": 25, "profession": "Doctor"},
    {"name": "Charlie", "age": 35, "profession": "Driver"}
]
for person in people:
    print(f"{person['name']} is {person['age']} years old and is a {person['profession'].lower()}")