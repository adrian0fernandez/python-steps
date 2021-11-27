def decorator_function(parameter_function):
    def inside_function():
        print("Let's do a basis calculus operation: ")
        parameter_function()
        
        # Add additional actions for decorate

        print("We've finished the calculation.\n")
    
    return inside_function

@decorator_function
def add():
    print("Add: ", 25+23)
add()

@decorator_function
def substract():
    print("Substract: ", 253-124)
substract()

@decorator_function
def multiply():
    print("Multiply: ", 25*3)
multiply()

@decorator_function
def divide():
    print("Divide: ", 2500/123)
divide()
