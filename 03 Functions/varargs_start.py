# Demonstrate the use of variable argument lists


# TODO: define a function that takes variable arguments
def addition(*args):
    result = 0
    for arg in args:
        result +=arg
    return result

def main():
    # TODO: pass different arguments
    print(addition(5,10,20,30))
    print(addition(1,2,3))

    # TODO: pass an existing list
    Mynums = [4 , 8 ,10 ,12]
    print (addition(*Mynums))

if __name__ == "__main__":
    main()
