# -------------------------------------------------------------------------------
# Name: Teddy Wyatt
# Assignment: 4
# Due Date: 10/11/2021
# -------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on tis assignment that
# violates the ethical guidelines set forth by the professor and class syllabus.
# -------------------------------------------------------------------------------
# References:
# -------------------------------------------------------------------------------
# Comments and assumptions: General assumations the types of values that are sent
# to the functions are proper ones. 
#
# function 1 assumption: string funciton in use.
# function 2 assumption: assume the list of ints is greater than 0  and position
# 0 is even.
# function 3 assumption: items can be an empty list.
# function 4 assumption: there is no duplicated items in draft_guest list, the 
# name of the new guest is different from all names in draft_guest list. draft 
# guests list is presorted
# -------------------------------------------------------------------------------
# NOTE: width of source code should be <= 80 characters to be readable on screen.
# -------------------------------------------------------------------------------


def swap_text(text):
# checks the length of text sting and verifies if even or odd
# if even it makes a new version of the text stored in new_text
# it loops through the string starting at the 1st character
# it then swaps the 1st character with the second character
# and then the second character with the first     

# Action to take if text is even
    if len(text)%2==0:
# Strings are inmutable this makes a new string        
        new_text='' 
# Loop thru characters of text 2 charcters at time        
        for i in range(0,len(text),2): 
# Adds the second and the first characer to the new string            
            new_text += (text[i+1] + text[i]) 
# Action to take if text is odd    
    elif len(text)%2==1: 
        new_text='' 
        for i in range(0,(len(text)-1),2): 
            new_text += (text[i+1] + text[i]) 
# Adds the last char from the oringial text to the end of string
        new_text += text[-1] 
#returns the new string as the result of the function when called    
    return new_text 

def which_day(numbers):
# Iterates thru a list of numbers seperating 1st from 2nd etc
# it sums up numbers given in the even indexes and odd indexes
# it takes the absolute value of the even sum - odd sum and 
# divides that by 7. The corresponding number represents a day
# {0: Sunday, 1: Monday, 2: Tuesday, etc}

# Initialize the variables for even and odd sum
    even_sum = 0
    odd_sum = 0
# For loop to iterate over list of numbers     
    for i in range(len(numbers)):
        if i % 2 == 0:
            even_sum += numbers[i]
        elif i % 2 == 1:
            odd_sum += numbers[i]
# Out of for loop take the total of both and subtract
# one from the other and then divide by 7 the result is
# stored in variable called day. Use If/Else Statements
# to return the specfic day required by inputs. 
    day = abs(even_sum - odd_sum)%7
    if day == 0:
        return 'Sunday'
    elif day == 1:
        return 'Monday'
    elif day == 2:
        return 'Tuesday'
    elif day == 3:
        return 'Wednesday'
    elif day == 4:
        return 'Thursday'
    elif day == 5:
        return 'Friday'
    elif day == 6:
        return 'Saturday'
    
def delete_duplicates(item):
# Remove the duplicates values from a list and return a new list

# Initialize a new list
    new_item_list=[]
# for loop to iterate over the list of words
    for word in item:
# if else statement that checks if the word from the list is in
# list and in the new list. If so skips over that word, if not 
# it places that word into the new list
        if (word in item) and (word in new_item_list):
            new_item_list = new_item_list
        else:
            new_item_list.append(word)
# returns new list with duplicates removed. 
    return new_item_list

def final_guests(draft_guests, new_guest): 
# Takes a list which can be empty and a string
# it then sorts the list alphabetically. the string is converted to
# a list if the orginial list. if the orginial draft_guest list
# is empty new guest is added to the new list and and new list is
# returned. 

# Initialize the list for storing the string to iterate over later    
    new_guest_list = []
    new_guest_list.append(new_guest)
 
 # Initializing the list for storing the new compound list       
    guest_list = []
# If/Else branches to store the sorted names in the new list
# this statement is for working with empty draft guests list
    if draft_guests == []:
        guest_list.append(new_guest)
# this statement is for iterating over the draft guest list
# and detemining if the new guest is lower in the alpahbet than
# the names of the people on the current list and placing it on 
# appropriate spote in the new list
    else:
        for name in draft_guests:
            for new_name in new_guest_list:
# if guest name is lower in the aplphabet than the name in orignial
# list it and it is not in the new list it placed into the new list
# followed by the orginial list name                
                if (name  > new_name) and (new_name in guest_list)== False:
                    guest_list.append(new_name)
                    guest_list.append(name)
# If the above is not true than the orignial name is placed in the new list                
                else:
                    guest_list.append(name)
# if after iterating over the list the new name is not added this 
# ensures it is added
        if (new_name in guest_list) == False:
            guest_list.append(new_name)
    return guest_list


