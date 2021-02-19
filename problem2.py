def accept_user(inputUser):
    if(inputUser.isalpha()):
        strCatch = str(inputUser)
    else:
        print("You must enter a string!")
        return 0

    #check for above max value
    if (len(strCatch) > 10):
        print("The inputted string is above the allowed range!")
        return 0
    #check for below max value
    if (len(strCatch ) < 7):
        print("The inputted string is below the allowed range!")
        return 0
    return strCatch



def main():
    print("Please enter the username with no spaces: ")
    theVal = input()
    result = accept_user(theVal)
    if(result != 0):
        print(result)


main()