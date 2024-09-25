# Exercise 1

print("Exercise 1: This program has a function that takes an integer and calculates it's factorial. ")

def getFactorial (number_exercise_one):
    factorial = 1
    for i in range(1, number_exercise_one +1):
        factorial = factorial * i
    print("input:", number_exercise_one , end="")
    print(", Output:", factorial)

# This part for inputing the answer
while (True):
    number_exercise_one = int(input("Enter a positive integer: "))
    if (number_exercise_one < 0):
        number_exercise_one = number_exercise_one * -1
        print("Switched the negative integer to a positive integer")
    getFactorial(number_exercise_one)
    
    choice_exercise_one = input("Enter 'n' to continue with the next program or any other key to restart the program: ")
    if choice_exercise_one == 'n':
        break


# Exercise 2

print()
print ("Exercise 2: This program has a function that takes an integer and returns all the divisors in a list")

def getDivisorsInAList(number_exercise_two):
    divisors = []
    for i in range(1, number_exercise_two + 1):
        if (number_exercise_two % i == 0 ):
            divisors.append(i)
    print("input:", number_exercise_two , end="")
    print(", Output:", divisors)

# This part for inputing the answer
while (True):
    number_exercise_two = int(input("Enter a positive integer: "))
    if (number_exercise_two < 0):
        number_exercise_two = number_exercise_two * -1
        print("Switched the negative integer to a positive integer")
    getDivisorsInAList(number_exercise_two)
    
    choice_exercise_two = input("Enter 'n' to continue with the next program or any other key to restart the program: ")
    if choice_exercise_two == 'n':
        break

# Exercise 3

print()
print ("Exercise 3: This program has a function that reverses a string and returns it")

def getStringReversed(string):
    string_reversed = ""
    for i in range (len(string)):
        string_reversed = string[i] + string_reversed
    return string_reversed

# This part for inputing the answer
while (True):
    string_exercise_three = str(input("Enter a string: "))
    reversed_string = getStringReversed(string_exercise_three)
    print('input: "' + string_exercise_three , end='"')
    print(', Output: "' + reversed_string + '"')

    choice_exercise_three = input("Enter 'n' to continue with the next program or any other key to restart the program: ")
    if choice_exercise_three == 'n':
        break


# Exercise 4

print()
print ("Exercise 4: This program has a function that takes a list of integers and returns a list of even numbers from the original list in the same order")

def getEvenNumbersOfList(numbers_list):
    even_numbers_list = []
    for i in range(len(numbers_list)):
        if (numbers_list[i] % 2 == 0):
            even_numbers_list.append(numbers_list[i])
    return even_numbers_list


# This part for inputing the answer
while (True):
    number_list_exercise_four = []
    while (True):
        number_list_exercise_four.append(int(input("Enter a number to the list: ")))
        option_for_list = str(input("Do you want to put more numbers? Input n to stop, or any other key to continue: ")).lower()
        if (option_for_list == "n"):
            break
    even_number_list_exercise_four = getEvenNumbersOfList(number_list_exercise_four)
    print("input:", number_list_exercise_four , end="")
    print(", Output:", even_number_list_exercise_four)
    
    choice_exercise_four = input("Enter 'n' to continue with the next program or any other key to restart the program: ")
    if choice_exercise_four == 'n':
        break

# Exercise 5

print()
print ("Exercise 5: This program has a function that checks if the password is strong or not. ")

def checkStrongPassword(password):
    special_characters = "#?!$"
    contains_special_character = False
    contains_digit = False
    contains_upper_case = False
    contains_lower_case = False

    if (len(password) < 8):
        return "Weak Password"

    for i in range(len(password)):
        if password[i] in special_characters:
            contains_special_character = True
        elif password[i].isdigit():
            contains_digit = True
        elif password[i].isupper():
            contains_upper_case = True
        elif password[i].islower():
            contains_lower_case = True
    if (contains_special_character and contains_digit and contains_upper_case and contains_lower_case):
        return "Strong password"
    else: 
        return "Weak password"


# This part for inputing the answer
while (True):
    string_exercise_five = str(input("Enter a password: "))
    password_output = checkStrongPassword(string_exercise_five)
    print('input: "' + string_exercise_five , end='"')
    print(' Output: "' + password_output + '"')

    choice_exercise_five = input("Enter 'n' to continue with the next program or any other key to restart the program: ")
    if choice_exercise_five == 'n':
        break

# Exercise 6

print()
print ("Exercise 6: This program has a function that if an IPv4 address is valid or not")

def checkValidityOfIPv4Address(ip_address):
    ip_octets = ip_address.split(".")
    if (len(ip_octets) != 4):
        return False
    for i in range(len(ip_octets)):
        if not ip_octets[i].isdigit():
            return False
        if not 0 <= int(ip_octets[i]) <= 255:
            return False
        if ip_octets[i] != str(int(ip_octets[i])):
            return False
    return True


# This part for inputing the answer
while (True):
    ip_address_exercise_six = str(input("Enter an IP Address: "))
    is_valid = checkValidityOfIPv4Address(ip_address_exercise_six)
    ip_address_outcome = ""
    if (is_valid == True):
        ip_address_outcome = "Valid IPv4 Address"
    else:
        ip_address_outcome = "Invalid IPv4 Address"
    print("input:", ip_address_exercise_six , end="")
    print(", Output: " + ip_address_outcome + '"')
    choice_exercise_six = input("Enter 'n' to continue with the next program or any other key to restart the program: ")
    if choice_exercise_six == 'n':
        break
