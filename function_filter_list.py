# Write a python program that, given an input list, will filter the input above a user defined threshold. This is to be done with a standard function.
# That is, given a list [1,2,3,4,5,6,7,8,9], and an argument (6), it should return [1,2,3,4,5,6]

input_list = [35,2,91,87,25,74,89,53,2909]

def filtered_list(input_list, thresh): #standard function with 2 parameters - the list and the threshold
    return [n for n in input_list if thresh > n] #getting rid of any value above the user-defined threshold
            

print(filtered_list(input_list, 100)) #applying a threshold of 100 to my input_list above