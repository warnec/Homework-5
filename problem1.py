def date_field(inputDate):

    try:
        intCatch = int(inputDate)
    except ValueError:
        print("You must enter an integer!")
        return 0
    # check for above max value
    if (intCatch > 31):
        print("The inputted value is above the allowed range!")
        return 0
    #check for below max value
    if (intCatch < 1):
        print("The inputted value is below the allowed range!")
        return 0
    return inputDate



def main():
    print("Please enter the calendar value: ")
    theVal = input()
    result = date_field(theVal)
    if(result != 0):
        print(result)


main()