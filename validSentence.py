#imports
import re

'''This program takes in a string and checks if it meets certain criteria.
The criteria for this program are:
-Starts with a capital letter
-Has an even number of quotation marks
-Ends with a ".", "?", or "!"
-Has no period characters other than the last character
-Has all numbers below 13 spelled out'''

# This method takes in a string and checks if it starts with a captial letter.
def isUpper(inputString):
    if (not inputString[0].isalpha()):  # if the string doesn't start with a letter
        return False
    if (not inputString[0].isupper()):  # if the string doesn't start with a capital letter
        return False
    return True

# This method takes in a string and checks if the amount of quotation marks is even.
def quotationCount(inputString):
    if (inputString.count('"')%2 == 1):  # if the amount of quotation marks is not even (odd numbers mod 2 return 1)
        return False
    return True

# This method takes in a string and checks if it ends with a period, question mark, or exclamation mark.
def finalChar(inputString):
    if (inputString[-1] != "." and inputString[-1] != "?" and inputString[-1] != "!"):  # if the string's final char isn't ".", "?", or "!"
        return False
    return True

# This method takes in a string and checks if the only period present is at the end.
def singlePeriod(inputString):
    if (inputString.find(".") != len(inputString)-1 and inputString.find(".") != -1):  # if there is a "." present, and the first occurence is not the end of the string
        return False
    return True

# This method takes in a string and checks if all numbers below 13 are spelled out.
def below13(inputString):
    # the regex picks up single digits 0-9, and digits 0-2 following a 1. It finds them at the start, in, and at the end of a string, without picking up digits as part of larger numbers.
    if (bool(re.search("^[0-9]\s|\s[0-9]\s|\s[0-9][.,!?]|^[1][0-2]\s|\s[1][0-2]\s|\s[1][0-2][.,!?]", inputString))):  # if any of the regex expressions are matched
        return False
    return True


# This method takes in a string and runs it through all the above methods
# If the string meets all of the criteria, it is valid, and the method returns true
# If it fails any of the criteria, it is invalid, and the method returns false
def isValid(inputString):
    #inputString = str(inputString)  # convert inputString to a string to avoid errors with improper types
    if (isUpper(inputString)):
        if (quotationCount(inputString)):
            if (finalChar(inputString)):
                if (singlePeriod(inputString)):
                    if below13(inputString):
                        return True
    
    return False

# This method accepts a custom input
def customInput():
    stringInput = str(input("Enter string\n>>>: "))
    return isValid(stringInput)

# This method runs the unit tests
def unitTests():
    #Method 1
    print("\nTesting 'isUpper' method. Checking for Capital letter at start of string.\
        \nTest 1: String: 'The quick brown fox'. Result: " + str(isUpper('The quick brown fox')) +  # String starts with capital. Should return True
        "\nTest 2: String: 'the quick brown fox'. Result: " + str(isUpper('the quick brown fox')) +  # String starts without capital. Should return False 
        "\nTest 3: String: '15 quick brown foxes'. Result: " + str(isUpper('15 quick brown foxes')))  # String starts with a number. Should return False 

    #Method 2
    print("\nTesting 'quotationCount' method. Checking for an even amount of quotation marks.\
        \nTest 1: String: 'The quick brown fox'. Result: " + str(quotationCount('The quick brown fox')) +  # String has no quotations, should return True 
        "\nTest 2:String: 'The \"quick brown\" fox'. Result: " + str(quotationCount('The "quick brown" fox')) +  # String has 2 quotations, should return True
        "\nTest 3: String: 'The \"quick\" \"brown fox'. Result: " + str(quotationCount('The "quick" "brown fox')))  # String has 3 quotations, should return False

    #Method 3
    print("\nTesting 'finalChar' method. Checking that the final character is '.', '!', or '?'.\
        \nTest 1: String: 'The quick brown fox.'. Result: " + str(finalChar('The quick brown fox.')) +  # String ends with a period. Should return True
        "\nTest 2:String: 'The quick brown fox!'. Result: " + str(finalChar('The quick brown fox!')) +  # String ends with an exclamation mark. Should return True
        "\nTest 3: String: 'The quick brown fox?'. Result: " + str(finalChar('The quick brown fox?')) +  # String ends with a question mark. Should return True
        "\nTest 4: String: 'The quick brown fox'. Resut: " + str(finalChar('The quick brown fox')))  # String ends with no punctuation. should return False

    #Method 4
    print("\nTesting 'singlePeriod' method. Checking that the string has no period characters other than the last character.\
        \nTest 1: String: 'The quick brown fox.'. Result: " + str(finalChar('The quick brown fox.')) +  # String has a period at the end. Should return True
        "\nTest 2: String: 'The quick brown fox'. Resut: " + str(finalChar('The quick brown fox')) +  # String has no periods. Should return True
        "\nTest 3: String: 'The quick. brown fox.'. Result: " + str(finalChar('The quick. brown fox.')) +  # String has a period in the middle, and at the end. Should return False
        "\nTest 2: String: 'The quick. brown fox'. Resut: " + str(finalChar('The quick. brown fox')))  # String has a period in the middle. Should return False

    #Method 5
    print("\nTesting 'below13' method. Checking that the string has all numbers below 13 written out (one, two, three...).\
        \nTest 1: String: 'There are no quick brown foxes.'. Result: " + str(below13('There are no quick brown foxes.')) +  # String does not contain any numbers. Should return True
        "\nTest 2: String: 'There are 10 or 13 quick brown foxes.'. Result: " + str(below13('There are 10 or 13 quick brown foxes.')) +  # String contains a number below 13 in digits, and a number not below 13. Should return False
        "\nTest 3: String: 'There are 10 quick brown foxes.'. Result: " + str(below13('There are 10 quick brown foxes.')) +  # String contains a number below 13 in digits. Should return False
        "\nTest 2: String: 'There are 13 quick brown foxes.'. Result: " + str(below13('There are 13 quick brown foxes.')))  # String contains a number not below 13. Should return True

    #Method 6
    print("\nTesting 'isValid' method. Checking a string meets all given requirements.\
        \nTest 1: String: 'The quick brown fox said \"hello Mr lazy dog\".'. Result: " + str(isValid('The quick brown fox said "hello Mr lazy dog".')) +  # String has a capital start, even quotes, ends in a period, has only one period, and no numbers. Should return True
        "\nTest 2: String: 'One lazy dog is too few, thirteen is too many.'. Result: " + str(isValid('One lazy dog is too few, thirteen is too many.')) +  # String has a capital start, no quotes, ends in a period, has only one period, and all numbers below 13 are spelled out. Should return True
        "\nTest 3: String: '\"The quick brown fox said \"hello Mr lazy dog.\"'. Result: " + str(isValid('"The quick brown fox said "hello Mr lazy dog."')) +  # String has a capital, odd quotes, one period, ends with a period, and no numbers. Should return False
        "\nTest 4: String: 'Are there 11, 12, or 13 lazy dogs?'. Result: " + str(isValid('Are there 11, 12, or 13 lazy dogs?'))) # String has a capital, no quotes, no periods, ends with a question mark, and has numbers below 13 as digits. Should return False

# Main method. Runs a small menu to allow user to choose methods to run    
def main():
    while True:
        print("1) Check custom input\n2) Run unit tests\n3) Quit")
        userInput = int(input(">>>: "))
        if (userInput == 1):
            if (customInput()):
                print("Valid entry")
            else:
                print("Invalid entry")
        if (userInput == 2):
            unitTests()
        if (userInput == 3):
            break

main()