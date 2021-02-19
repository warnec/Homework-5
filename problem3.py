def age_input(inputAge):

    try:
        intCatch = int(inputAge)
    except ValueError:
        print("You must enter an integer!")
        return 0

    # check for above max value
    if (intCatch > 70):
        print("The inputted value is above the allowed range!")
        return 0
    #check for below max value
    if (intCatch < 16):
        print("The inputted value is below the allowed range!")
        return 0
    if ((intCatch >= 60) and (intCatch <= 65)):
        print("The inputted age is between 60 and 65 inclusive")
        return 0
    return inputAge



def main():
    print("Please enter the age value: ")
    theVal = input()
    result = age_input(theVal)
    if(result != 0):
        print(result)


main()