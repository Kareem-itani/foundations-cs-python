# Choice 1

# This program recursively counts the number of digits of an integer

def countDigits(integer_exercise_one):
    if integer_exercise_one == 0:
        return 0
    return 1 + countDigits(integer_exercise_one // 10)

# Choice 2

# This program recursively finds the maximum valued integer in a list

def findMax(list_exercise_two,index,maximium_value_index):
   
   if len(list_exercise_two) == 0:
       return 0
   
   if index == len(list_exercise_two):
       return list_exercise_two[maximium_value_index]
   
   if list_exercise_two[index] > list_exercise_two[maximium_value_index]:
       maximium_value_index = index
    
   return findMax(list_exercise_two,index + 1 , maximium_value_index) 
    

# Choice 3

# This program counts the number of html tags in the code recurisvely

def countHtmlTags(html_code, html_tag_wanted):
    
    starting_tag = "<" + html_tag_wanted
    closing_tag = "</" + html_tag_wanted + ">"
    self_closing_tag = "<" + html_tag_wanted

    self_closing_position = html_code.find(self_closing_tag)
    if self_closing_position != -1:
        return 1 + countHtmlTags(html_code[self_closing_position + len(self_closing_tag):], html_tag_wanted)

    starting_tag_position = html_code.find(starting_tag)
    if starting_tag_position == -1:
        return 0
    
    closing_tag_position = html_code.find(closing_tag,starting_tag_position)
    if closing_tag_position == -1:
        return 0
    
    
    return 1 + countHtmlTags(html_code[closing_tag_position + len(closing_tag) :], html_tag_wanted)



# Choice 4 is part of the menu function 

def menu():
    while (True):
        
        print("1. Count Digits")
        print("2. Find Max")
        print("3. Find Tags")
        print("4. Exit")

        for i in range(15):
            print("-",end=" ")
        
        print()
        
        menu_choice = int(input("Enter a choice: "))

        if (menu_choice == 1):
            integer_choice_one = int(input("Enter an integer to find its number of digits: "))
            result_choice_one = countDigits(integer_choice_one)
            print("Input:",integer_choice_one, "Output:", result_choice_one)
            print()    

        elif (menu_choice == 2):
            integer_list_choice_two = [int(num) for num in input("Enter numbers seperated by space: ").split()]
            result_choice_two = findMax(integer_list_choice_two,0,0)
            print("Input:",integer_list_choice_two,"Output:",result_choice_two)
            print()

        elif (menu_choice == 3):
            html_code_choice_three = str(input("Enter your html code here: "))
            html_tag_choice_three = str(input("Enter the html tag you want to find the count of: "))
            number_of_wanted_html_tags = countHtmlTags(html_code_choice_three,html_tag_choice_three.lower())
            print('The number of "' + html_tag_choice_three.lower() + '" tags is ', number_of_wanted_html_tags)
            print()

        elif (menu_choice == 4):
            print("Program Exited Successfully")
            break
        else:
            menu_choice = int(input("Enter a choice (1 to 4):"))

menu()
