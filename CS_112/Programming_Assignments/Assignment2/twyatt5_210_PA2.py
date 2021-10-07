#-------------------------------------------------------------------------------
# Name: Teddy Wyatt
# Assignment: 2
# Due Date: 9/20/2021
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on tis assignment that
# violates the ethical guidelines set forth by the professor and class syllabus. 
##-------------------------------------------------------------------------------
# References: 
#-------------------------------------------------------------------------------
# Comments and assumptions: assume that the types of values that are sent to the
# functions are proper ones. Not actually making body of code. Just making
# functions to be called by the tester and ran against it. I had this assignment
# completed with in 1st hour after class with dicitionaries. I added so much
# lines of code when I took them out and made if else statements.
#-------------------------------------------------------------------------------
# NOTE: width of source code should be <= 80 characters to be readable on screen.
#-------------------------------------------------------------------------------

# This function creates a "Title of the Movie of your Life" which is a string
# formed by the concatenatin of return value of the other called functions 
# the following 5 functions give the value of the string

def myMovieLife(lastname_fstletter, birth_month, cell_digit):
    month_or_months = months(cell_digit)

# for proper grammar of the sentence if you return 1 month for months
# the string of the movie will return month, if more than 1 month than
# string of the movie return months
    if month_or_months == 1:
        month_or_months ='month'
    else:
        month_or_months = 'months'

# This is the string formatted to retrieve each value from the other functions
    rv = 'The {} {} {} {} in {} {}'. format(status(cell_digit),\
    adjective(lastname_fstletter), subject(birth_month),\
    complement(cell_digit), months(cell_digit), month_or_months)
    
    return rv

# This function gets the last digit of your cellphone and returns a boolean 
# (True/False). Its parameters is the last digit of your cellphone 
# which is converted to interger and then we evalute the digit and find the
# modulo of digit by 2. We know that the modulo of any even number by 2 is 0
# the modulo of any odd number by 2 is 1 thus if even return true if odd 
# return false

def status(cell_digit):
    status = ''
    if cell_digit%2 == 0:
        status = True
    else:
        status = False 
    return status

# This function iterates through a list of if/else statements finding the 
# value of the first letter of last name and returning a adjective for 
# title of the movie

def adjective(lastname_fstletter):
    if lastname_fstletter == 'A':
        adjective = 'awesome'
    elif lastname_fstletter == 'B':
        adjective = 'shocking'
    elif lastname_fstletter == 'C':
        adjective = 'hilarious'
    elif lastname_fstletter == 'D':
        adjective = 'fascinating'
    elif lastname_fstletter == 'E':
        adjective = 'marvelous'
    elif lastname_fstletter == 'F':
        adjective = 'unbelievable'
    elif lastname_fstletter == 'G':
        adjective = 'funny'
    elif lastname_fstletter == 'H':
        adjective = 'epic'
    elif lastname_fstletter == 'I':
        adjective = 'thrilling'
    elif lastname_fstletter == 'J':
        adjective = 'wonderful'
    elif lastname_fstletter == 'K':
        adjective = 'dramatic'
    elif lastname_fstletter == 'L':
        adjective = 'intriguing'
    elif lastname_fstletter == 'M':
        adjective = 'courageous'
    elif lastname_fstletter == 'N':
        adjective = 'beautiful'
    elif lastname_fstletter == 'O':
        adjective = 'bracing'
    elif lastname_fstletter == 'P':
        adjective = 'lively'
    elif lastname_fstletter == 'Q':
        adjective = 'dangerous'
    elif lastname_fstletter == 'R':
        adjective = 'impressive'
    elif lastname_fstletter == 'S':
        adjective = 'astonishing'
    elif lastname_fstletter == 'T':
        adjective = 'interesting'
    elif lastname_fstletter == 'U':
        adjective = 'unexpected'
    elif lastname_fstletter == 'V':
        adjective = 'suprising'
    elif lastname_fstletter == 'W':
        adjective = 'lovely'
    elif lastname_fstletter == 'X':
        adjective = 'electrifying'
    elif lastname_fstletter == 'Y':
        adjective = 'commoving'
    else:
        adjective = 'overwhelming'
    return adjective

# This function iterates through a list of if/else statements finding the value
# of the first three letters of the birth month and returning a subject 
# corresponding to that month for title of the movie

def subject(birth_month):

    if birth_month == 'Jan':
        subject = 'biography'
    elif birth_month == 'Feb':
        subject = 'history'
    elif birth_month == 'Mar':
        subject = 'legend'
    elif birth_month == 'Apr':
        subject = 'life'
    elif birth_month == 'May':
        subject = 'anecdote'
    elif birth_month == 'Jun':
        subject = 'revenge'
    elif birth_month == 'Jul':
        subject = 'mission'
    elif birth_month == 'Aug':
        subject = 'existence'
    elif birth_month == 'Sep':
        subject = 'battle'
    elif birth_month == 'Oct':
        subject = 'chronicle'
    elif birth_month == 'Nov':
        subject = 'combat'
    elif birth_month == 'Dec':
        subject = 'fairy tale'
    return subject

# This function iterates through a list of if/else statements finding the value
# of the cell_digit give and returning a complement for title of the movie
def complement(cell_digit):
    if cell_digit == 0:
        complement = 'of an adventurer'
    elif cell_digit == 1:
        complement = 'of a warrior'
    elif cell_digit == 2:
        complement = 'of a genius'
    elif cell_digit == 3:
        complement = 'of a movie star'
    elif cell_digit == 4:
        complement = 'of a hero'
    elif cell_digit == 5:
        complement = 'of a scientific'
    elif cell_digit == 6:
        complement = 'of a dreamer'
    elif cell_digit == 7:
        complement = 'of a cowboy'
    elif cell_digit == 8:
        complement = 'of a jedi'
    else:
        complement = 'of an ogre'
    return complement

# This function gets the last digit of your cellphone and returns an integer that
# will be months used for your movie title
def months(cell_digit):
# formula to calculate how much each digit is worth in days
    days = ((cell_digit)**((cell_digit%2)+1)*(cell_digit))
# if statement to take the number of days in convert it to months
    if days/30 <= 1:
        months = 1
# compound if statement adds 1 to the integer of number of days if the modulo of
# number of days is less than 29 and the number of days divided by 30 is greater
# than 1
    elif days/30 > 1 and (days%30) <= 29:
        months = int(((days/30) + (1)))
    return months
