# function definiton
def minimum(number_list):

    min = number_list[0]
    for index in range(1, len(number_list)):

        if (number_list[index] < min):
        
            min = number_list[index]

    return min

# main program
my_list = [2, 10, 25, 32, -105, 2]
my_list2 = [2, 10, 25, -32, 135, 2]

output = minimum(my_list)
output2 = minimum(my_list2)
print(output)
print(output2)

