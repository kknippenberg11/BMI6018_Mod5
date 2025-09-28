# Write a python program that, given an input list of any level of complexity/nestedness, will return the inner most list plus 1. This is to be done with recursion. Note: the input will contain only integers or lists. 

input_list = [35,2,91,87,[25,74,89,[53,2909]]]

def recursive_find_list(ls): #creating a recursive function
    for el in ls: #for each element in a given list
        if isinstance(el, list):   # if the element is an instance of a list
            return recursive_find_list(el) #start the recursion on that inner list
    return[n + 1 for n in ls] #and once we can't do any more recursion, add 1 to each number of the list

print(input_list[4][3]) #for comparison
print(recursive_find_list(input_list)) #applying the function recursive_find_list to our original input_list