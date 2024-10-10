class person:
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Person {self.name} is created.")
    
    # Destructor

    def __del__(self):
        print(f"Person {self.name} is deleted.")
    
# Usage

per1 = person("Kyra", 20)
per2 = person("salim", 34)

print(per1)

# Deleting the objects

