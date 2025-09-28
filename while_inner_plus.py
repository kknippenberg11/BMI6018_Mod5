# This assignment will have 3 .py files submit via your GitHub repository. Please ensure the .py files are named accordingly:

# while_inner_plus.py
# recursive_inner_plus.py
# function_filter_list.py
 
################
# while_inner_plus.py

# Write a python program that, given an input list of any level of complexity/nestedness, will return the inner most list plus 1. This is to be done with a while loop. Note: the input will contain only integers or lists. 

input_list = [35,2,91,87,[25,74,89,[53,2909]]]

# first look through input_list for INDEXED ITEMS, whether integer or list. 
# input_list has a total of 5 elements indexed 0 through 4, with 0-3 being integers and 4 being a list
i = 0 #since we're dealing with index positions, we'll start at position 0 each time
while i < len(input_list): #handy for not knowing the exact length of our given list
    if isinstance(input_list[i], list):   # we found our list at index 4 (eg, [25,74,89,[53,2909]])
        input_list_ii = input_list[i] #break out this item and rename it, so we do the same thing to this inner list
        j = 0
        while j < len(input_list_ii): #handy for not knowing the exact length of our given list
            if isinstance(input_list_ii[j],list): # we find our list at index 3 (eg, [53,2909])
                input_list_iii = input_list_ii[j] #break out this item and rename

                plus_one_list = [] #Now we're going to create a NEW, EMPTY list and fill it up, based on the innermost list
                k = 0
                while k < len(input_list_iii): #same as before
                    l = input_list_iii[k] + 1
                    plus_one_list.append(l) #filling up our plus_one_list
                    k += 1
                print(input_list_iii) #for comparision's sake
                print(plus_one_list) #our actual answer
            j += 1 #keep looping this while loop
    i += 1 #keep looping this while loop