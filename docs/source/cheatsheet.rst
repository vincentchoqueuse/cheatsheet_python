Cheatsheet
==========



.. code :: 

    # assignment
    y = 3  # assign the value 3 to the variable y 
    x += 1  # increment the value of the variable x by 1
    my_list = [2, 3]  # assign the list composed of the elements 2 and 3 to the variable my_list
    value = my_list[1]  # assign the second element of my_list (0 indexed) to the variable value


.. code ::

    # conditional statement
    value = (x == 3)  # check if the value of x is equal to 3 (returns True or False)

    if value:   # if value is evaluated to True, do the following stuff
        # do something 
        print("true")

.. code :: 
    
    # iterations 

    ## for loops
    for x in range(10):   # for x ranging from 0 to 10 (excluded), do the following stuff
        # do something
        print(x)

    for x in range(2, 10, 2):   # for x ranging from 2 to 10 (excluded) with increment of 2, do the following stuff
        # do something
        print(x)

    ## while loop
    index = 0  
    while (indice<10):  # while indice is strictly lower than 10
        indice = indice+1

.. code ::

    # function definition
    def sum(a, b):   # create a function named sum with input arguments a and b 
        return a+b   # returns the value of a+b

    r = sum(2, 3)  # call the function sum with input arguments 2 and 3