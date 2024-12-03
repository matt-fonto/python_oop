person = {"name":"Matt", "age":28}
# In Python, dictionaries require the use of bracket notation `person["age"]`
# in python, we can't access dictionary properties with dot notation `person.name`, as we would in JS

# Get values from the key
print(person["name"]) # use it when we're sure the certain key exists
print(person.get('name')) # use it when unsure if certain key exists. safe retrieve. If key doesn't exist, doesn't throw error as the bracket notation would, and returns None

person.keys() # get all dict keys
person.values() # get all dict values
person.items() # get all key:value pair as a tuple
person.update() # updates values and overrides the previous ones
person.pop(key) # removes and returns the value of the specified key


# people = [
#     {"name": "Alice", "age": 30, "profession": "Teacher"},
#     {"name": "Bob", "age": 25, "profession": "Doctor"},
#     {"name": "Charlie", "age": 35, "profession": "Driver"}
# ]
# for person in people:
#     print(f"{person['name']} is {person['age']} years old and is a {person['profession'].lower()}")
