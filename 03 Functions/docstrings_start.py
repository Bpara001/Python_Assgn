# Demonstrate the use of function docstrings


def myFunction(arg1, arg2=None):
    """"myFunction(arg1,arg2=None) --> Doesnt do much besides printing
    Parameters:
    arg1: pass w.e
    arg2: does not matter what you pass
    """
    print(arg1, arg2)


def main():
    print(myFunction.__doc__)


if __name__ == "__main__":
    main()
