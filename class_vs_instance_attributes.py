class Example:
    class_attribute = "Shared"

    def __init__(self, instance_value):
        self.instance_value = instance_value

obj1 = Example('Instance 1')
obj2 = Example('Instance 2')

print(obj1.class_attribute) # Shared
print(obj1.class_attribute) # Shared

print(obj1.instance_value) # instance 1
print(obj2.instance_value) # instance 2

Example.class_attribute = 'Modified'
print(obj1.class_attribute) # Modified
print(obj1.class_attribute) # Modified

