#######################################################
##############         Exercise 1    ##################
#######################################################

# Choice 1 Write a function that returns a tuple containing the sum of two tuples

def getSumTuples(tup1, tup2):

    # Convert the two tuples to lists
    lst1 = list(tup1)
    lst2 = list(tup2)

    # Find the larger list in length and extend the smaller one
    if len(lst1) > len(lst2):
        lenLarger = len(lst1)
        lst2.extend([0] * (lenLarger - len(lst2)))
    else:
        lenLarger = len(lst2)
        lst1.extend([0] * (lenLarger - len(lst1)))
    
    # Initialize the list that contains the sum of the two lists
    lstSum = []

    # fill up the list with the sum of the two lists
    for i in range(lenLarger):
        lstSum.append(lst1[i] + lst2[i])

    # convert the final list to a tuple and return it
    return tuple(lstSum)


# Choice 2 Write a Function that would export the elements of a Python Dictionary into a JSON File

def exportJSON(dictionary,fileName):
    
    # Write the new file 
    with open(fileName, 'w') as file:
        # count to find the index of the file
        count = 0
        # we start the json file with a {
        file.write("{ \n")
        # to extract the dictionary's key and value and place it in the json file
        for key, value in dictionary.items():
            file.write(f' "{key}": "{value}"')
            # increment the index (count)
            count += 1
            # check if the count is not the last element 
            # since it is better practice not to leave
            # trailing commas in json files
            if count < len(dictionary):
                file.write(",")
            file.write("\n")
        # end the json file with a } 
        file.write("}")

# Choice 2 Write a Function that would export the elements of a JSON File into a python Dictionary

def importJSON(fileName):
    # initalize a dictionary
    dictionary = {}
    # Open the file for reading
    with open(fileName, 'r') as file:
        # remove the empty spaces
        json_contents = file.read().strip()

    #Remove the { and }
    json_contents = json_contents[1:-1] 
    key_and_value = json_contents.split(", ")

    # we loop and split the key and values
    for i in key_and_value:
        key, value = i.split(":")
        # add the key and values to the dictionary
        dictionary[key.strip().replace('"','')] = value.strip().replace('"', '')
    
    # Return the dictionary
    return dictionary

def menu():
    # Loop 
    while True:
        # The options
        print("1. Sum Tuples")
        print("2. Export JSON")
        print("3. Import JSON")
        print("4. Exit")
        # The line segmenting the options and the choice prompt
        for i in range(15):
            print("-",end=" ")
        
        print()
        # Choice input
        choice = int(input("Enter a choice: "))

        if(choice == 1): #Sum Tuples
            tuple_one = {int(num) for num in input("For tuple 1 enter numbers seperated by space: ").split()}
            tuple_two = {int(num) for num in input("For tuple 2 enter numbers seperated by space: ").split()}
            tuple_sum = getSumTuples(tuple_one,tuple_two)
            print(tuple_sum)
        
        elif(choice == 2): #export JSON
            
            dictionary_one = {}
            
            while True:
                key = input("Enter the key type 'finish' to finish: ")
                if key.lower() == "finish":
                    break
                key_value = input(f"Enter value for the {key} :")
                dictionary_one[key] = key_value

            file_name = str(input("Enter what do you want to name the without the .JSON suffix: "))
            exportJSON(dictionary_one,file_name + ".json")
        
        elif(choice == 3): #Import JSON
            file_name = str(input("Enter what do you want to name the without the .JSON suffix: "))
            dictionary_two = importJSON(file_name + ".json")
            print(dictionary_two)
        
        elif(choice == 4): #Exit the program
            print("Program exited successfully")
            break

        else:
            choice = int(input("Enter a choice (Between 1 and four): "))

menu() #Call the menu


#######################################################
##############         Exercise 2    ##################
#######################################################

'''
a. 1/6N+8000N3+24
= 8000N3 + 1/6N + 14 
=> O(n^3)

b. 1/6N3
= 1/6N3
=> O(n^3)


c. 1/6N! +200N4
=> O(N!)

d. NlogN +1000
=> O(n log n)

e. logN +N
=> O(m)

f. 1/2N(N-1)
= 1/2N@ - 1/2N
=> O(n^2)

g. N2+220NlogN2+3N+9000
=> O(n^2)
h. N!+3N+2N+N3+N2
=> O(n!)
'''
