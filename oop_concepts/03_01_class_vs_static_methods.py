class Calculator:
    history = []

    @classmethod
    def add_to_history(cls, operation):
        cls.history.append(operation)

    @staticmethod
    def multiply(a,b):
        return a * b
    
    @classmethod
    def create_and_store_multiplication(cls, a, b):
        result = cls.multiply(a, b) # call static method
        cls.add_to_history(f"{a} * {b} = {result}")
        return result