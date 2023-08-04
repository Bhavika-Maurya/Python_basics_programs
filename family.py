# Parent class Father
class Father:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print("Father's Name:", self.name)
        print("Father's Age:", self.age)

# Parent class Mother
class Mother:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print("Mother's Name:", self.name)
        print("Mother's Age:", self.age)

# Child class Kids inheriting from both Father and Mother
class Kids(Father, Mother):
    def __init__(self, name, age, hobby):
        # Initializing attributes from both parent classes
        Father.__init__(self, name, age)
        Mother.__init__(self, name, age)
        self.hobby = hobby

    def display_info(self):
        print("Kid's Name:", self.name)
        print("Kid's Age:", self.age)
        print("Kid's Hobby:", self.hobby)

# Example usage:
kid1 = Kids("Alice", 10, "Drawing")
kid1.display_info()
