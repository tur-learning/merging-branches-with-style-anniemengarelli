import math

def add(a, b):
    """
    Adds two numbers
    """
    res = a + b
    return res

def multiply(a, b):
    """
    Multiplies two numbers
    """
    res = a * b 
    return res

def sqrt(a):
    """
    Calculates square root of a using build-in math library
    """
    result = math.sqrt(a)
    return result


if __name__ == "__main__": # only executed when you run utils.py, not main, use this for modules that you are importing
    print("You are into utils.py")
    result = add(10, 20)
    print(result)
