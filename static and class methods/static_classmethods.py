class MyClass:
    static_variable = "This is a static variable"

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

    @staticmethod
    def static_method():
        print("This is a static method")
        print("Accessing static variable:", MyClass.static_variable)

    @classmethod
    def class_method(cls):
        print("This is a class method")
        print("Accessing static variable:", cls.static_variable)

    def instance_method(self):
        print("This is an instance method")
        print("Accessing instance variable:", self.instance_variable)


# Example usage:
# Static method can be called directly on the class
MyClass.static_method()

# Class method can also be called directly on the class
MyClass.class_method()

# Instance method requires an instance of the class
my_instance = MyClass("Instance data")
my_instance.instance_method()


#in this revised example, the static method and class method both access the static variable static_variable. However, the key difference lies in how they can access and modify class-level data:

# Static Method:

# The static method static_method() is defined with the @staticmethod decorator and does not take any implicit parameters such as cls or self.
# It can access the static variable static_variable directly using the class name MyClass.static_variable.
# The static method cannot modify the static variable or any instance variables because it doesn't have access to self or cls.
# Class Method:

# The class method class_method(cls) is defined with the @classmethod decorator and takes the class itself as the first parameter, conventionally named cls.
# It can access the static variable static_variable using either the class name MyClass.static_variable or the cls parameter.
# The class method can modify the static variable or perform operations related to class-level data using the cls parameter.
# In summary, the primary difference between static methods and class methods is that static methods do not have access to the class or instance-specific data, while class methods can access and modify class-level data through the cls parameter.