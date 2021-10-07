

# function to calculate the rest time for slothmobile
def rest_time(miles_driven, brake_count):
    # variables for storing the results
    total_miles = int(miles_driven/brake_count)
    count_time = 0
    # for loop for interating thru total miles divided by times braked
    for i in range(total_miles):
        # if statements to check for cases to pull information about slothmobile
        # rest time
        if (total_miles % 2 == 0) and (total_miles == 0):
           #breaks out of loop and starts over
            break
        elif total_miles % 2 == 0:
            count_time += 1
            total_miles = int(total_miles/brake_count)  
        else:
            count_time += 0
            #breaks out of the loop and starts over
            break
    return(count_time)


# Function to define which speedy superhero saved the world
def which_speedster(feature_value):
    # initial variable for funciton
    product_value = 1
    sum_value = 0
    # for loop to go through items in list
    for num in feature_value:
        # if statement to check if item is float or not
        if (type(num) == float) == True:
            product_value *= num
        else:
            sum_value += num
    final_value = int(product_value/sum_value)
    return(final_value)

# Function to figure lifespan for Habugabuped
def lifespan(fingers_list, num_toes):
    digit = 1
    life_count = 0
    #for loop for iterating over list
    for num in fingers_list:
        #while loop for iterating over numbers up to digit from
        #list
        while digit <= num:
            #if statement to filter out for the correct digits
            #to figure lifespan of Habugabuped
            if (digit % num_toes == 0)and (digit != 0):
                life_count += 1
                digit +=1
                if digit > num:
                    digit = 0
                    break
            elif digit == num:
                digit = 0
                break
            elif num < num_toes:
                digit = 0
                break
            else:
                digit +=1
    return(life_count)


#the harry potter function for spells and figuring O.W.L. of students
def wiz_level(spell_list, owl_lower_bound, owl_upper_bound):
    #initializing the variables needed to complete this function
    unforgive_curses = ['Crucio', 'Imperio', 'Avada_Kedavra']
    danger_curses = ['Confringo', 'Sectumsempra', 'Fiendfyre']
    spell_points = 0
    mega_spell=""
    #for loop for getting the spells from list
    for spell in spell_list:
        #if statements to verify if spells are in hardcoded list- and configure
        #points
        if spell in danger_curses and spell_points >= owl_lower_bound:
            spell_points += 5
            mega_spell += spell
        elif spell in danger_curses and spell_points <= owl_lower_bound:
            spell_points += 7
            mega_spell += spell
        elif spell not in unforgive_curses and danger_curses:
            spell_points += 10
            mega_spell += spell
        else:
            spell_points += 0
            mega_spell += spell
            
    # I thought about making this its own seperate function tht pulled its
    # information from wiz_level, but was not sure if allowed. 
    # this if block breaks down the cases to figure what is return        
    if spell_points < owl_lower_bound:
        #print statement I want return for this case
        print_statement =str('Below O.W.L. Mega Spell: {}'.format(mega_spell))
        return(print_statement)
    elif owl_lower_bound <= spell_points <= owl_upper_bound:
       #print statement I want return for this case
        print_statement =str('On O.W.L. Mega Spell: {}'.format(mega_spell))
        return(print_statement) 
    elif spell_points > owl_upper_bound:
        #print statement I want return for this case
        print_statement =str('Beyond O.W.L. Mega Spell: {}'.format(mega_spell))
        return(print_statement)
