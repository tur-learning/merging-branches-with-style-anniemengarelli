def add(a, b):
    res = a + b
    return res

def multiply(a, b):
    res = a * b 
    return res


if __name__ == "__main__": # only executed when you run utils.py, not main, use this for modules that you are importing
    print("You are into utils.py")
    result = add(10, 20)
    print(result)
