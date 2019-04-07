# demonstrate template string functions

from string import Template
def main():
    instructor = "Joe Marini"
    teaching = "Advanced Python"
    # Usual string formatting with format()
    str1 = "You're watching {0} by {1}".format("Advanced Python", "Joe Marini")
    print(str1)
    
    # TODO: create a template with placeholders
    t1= Template("You're watching ${classroom} by ${name}")

    # TODO: use the substitute method with keyword arguments
    str2 = t1.substitute(classroom= teaching, name= instructor)
    print(str2)
    # TODO: use the substitute method with a dictionary
    names = {
        "name": instructor,
        "classroom": teaching
    }
    strinDic= t1.substitute(names)
    print(strinDic)
if __name__ == "__main__":
    main()
    