#-------------------------------------------------------------------------------
# Name: Teddy Wyatt
# Assignment: 1
# Due Date: 9/6/2021
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on tis assignment that
# violates the ethical guidelines set forth by the professor and class syllabus. 
##-------------------------------------------------------------------------------
# References: 
#-------------------------------------------------------------------------------
# Comments and assumptions: Assumations were from the promt. The user will always
# enter the correct data type asked for. Every number the user enters will be a
# posqitive real number when testing this project. The width of a specific item
# will be less than half the width of the lot. The length of a specific item 
# will be less than half the length of the lot. The program will out only integer
# values. Each Sim lot measuring unit is 4 ft x 4 ft
#-------------------------------------------------------------------------------
# NOTE: width of source code should be <= 80 characters to be readable on screen.
#-------------------------------------------------------------------------------

# Greetings message
print("Welcome to the Sims4 Builder Helper!")

# Width of the lot in Sim units
width = float(input('What is the width of your lot in Sim units? '))

# Length of the lot in Sim units
length = float(input('What is the length of your lot in Sim units? '))

# The name of specific item
specific_item = input('What is your specific item? ')

# The width of specific item
s_i_width = float(input('What is the width of your specific item in Sim units? '))

# The length of the specific item
s_i_length = float(input('What is the length of your specific item in Sim units? '))

# calculate Sim lot area and display the result
sim_lot_area = width * length
print('The area of your lot in Sim units is',  int(sim_lot_area), 'square units')

# calculate area of the lot in square feet and display result
squarefoot_width = width * 4
squarefoot_length = length * 4
squarefoot_area = squarefoot_width * squarefoot_length
print('The area of your lot in square feet is',  int(squarefoot_area), 'square ft')

# convert inputed item dimensions to feet. 
s_i_width_sqft = s_i_width * 4
s_i_length_sqft = s_i_length * 4 
print('The', specific_item, 'in the real world is about', int(s_i_width_sqft), 'ft by', int(s_i_length_sqft), 'ft')

# calculate how many items can fit in the lot by taking the sqft of lot width and length and dividing it by sqft of item. 
# you can fit half an item so only the whole number is needed. Used floor divison operator for this. 
item_cal_width = squarefoot_width//s_i_width_sqft
item_cal_length = squarefoot_length//s_i_length_sqft
item_total = item_cal_width * item_cal_length
print('About', int(item_total), specific_item +'s', 'can fit in this lot')

# calculate the percentage of covered units by the item
s_i_total_sqft = s_i_length_sqft * s_i_width_sqft
s_i_total_used = item_total * s_i_total_sqft
percentage_used = (s_i_total_used/squarefoot_area)*100
print('About', str(int(percentage_used)) +'%', 'of the lot is covered by the', specific_item +'s')

# calculate the number of unused squares
num_unused = sim_lot_area - ((s_i_length*s_i_width) * item_total)  
print('About', int(num_unused), 'square units is left uncovered')

# calculate the percentage of unused squares
percentage_unused = 100 - percentage_used
print('About', str(int(percentage_unused)) + '%', 'of the lot is left uncovered')

# outgoing message
print('Have fun building!')
