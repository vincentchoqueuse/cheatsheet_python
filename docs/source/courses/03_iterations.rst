Iterations
==========

Introduction
------------

This section focuses on another class of flow controls called **iterations**. Iteration is controlled with loop statements that execute one or more statements repeatedly. In many 
programming languages, loops can be implemented using :code:`for` or :code:`while` statements. 

For Loops
---------

In Python, the :code:`for` statement is used to iterate over the elements of a sequence such as a string, tuple, or list.

General Syntax
++++++++++++++

.. code ::

    color_list = ["blue", "white", "red]

    for color in color_list:
        print(color)

This code loops over a list composed of 3 elements. As the list of composed of 3 elements, the :code:`for` loop performs three iterations. 

* In the first iteration, the string :code:`"blue"` is assigned to the :code:`color` variable,
* In the second iteration, the string :code:`"white"` is assigned to the :code:`color` variable,
* In the third iteration, the string :code:`"red"` is assigned to the :code:`color` variable.

The program simply displays the string stored in the :code:`color` variable after each iteration.

Range Object
++++++++++++

It is quite common to loop over a predefined number of iterations. In Python, this behavior can be easily obtained using the :code:`range()` function.
The :code:`range()` function returns a sequence of numbers, starting from 0 by default, increments by 1 (by default), and stops before a specified number.

For illustration purposes, the next code shows how to print all the integers from 0 to 10 (excluded).

.. code ::

    for index in range(10):
        print(index)

This syntax is quite common in Python and can be used in many different contexts. By default, the :code:`range(N_stop)` function generates all the integers from 0 to :code:`N_stop` (excluded).
When a second argument is passed, the :code:`range(N_start, N_stop)` function generates all the integers from :code:`N_start` to :code:`N_stop` (excluded). 
It is also possible to pass a third argument to specify the step between each number.

* The documentation of the :code:`range()` is available here: https://docs.python.org/3/library/stdtypes.html#range).

Example
+++++++


Maximum
```````

The following example shows how to compute the maximum of a list :code:`x` of N elements.

.. math ::

    y = \max_{n=0,1,\cdots, N-1} x[n]

Note that Python already have a function to do that (see `documentation <https://docs.python.org/3/library/functions.html#max>`_ ). 
Nevertheless, we propose to replicate the behavior of this function with the following code.


.. code ::

    x = [10, 23, 50, 10, 2, 5.3, 34, 2]
    
    y = x[0]
    for n in range(1, len(x)):
        if x[n] > y:
            y = x[n]

    print("max={}".format(y))

**Import and Initialization**

To implement the algorithm, we first initialize the maximum to the first element of the list using :code:`y=x[0]`. 

* Initialization: :code:`y = 10`.



**For Loop**

Then, we perform a for loop to compare the maximum with each element of the list. In each iteration, we will perform the following tasks

* Extract the value of :code:`x[n]`
* Compare the value of :code:`x[n]` with the temporary maximum :code:`y`. If :code:`x[n] > y`, replace :code:`y` by the value of :code:`x[n]`


The content of the variable :code:`y` after each iteration is provided below:

* 1st iteration, :code:`y = 23`,
* 2nd iteration, :code:`y = 50`,
* 3rd iteration, :code:`y = 50`,
* 4th iteration, :code:`y = 50`,
* ...

Arithmetic sequence 
`````````````````````

In the following example, we focus on the sum of the arithmetic sequence

.. math ::

    s_n = \sum_{n=1}^{N} = 1 + 2 + 3 + \cdots + N

with :math:`N=100`. Note that this sum can be directly computed using the mathematical formula

.. math ::

    s_n = \frac{N(N+1)}{2} = 5050

For illustration purpose, we propose to compute this sum using a for loop. Specifically, we propose the following code.

.. code ::

    N = 100
    s_n = 0 # initialization of the sum 

    for n in range(1, N+1):
        s_n += n # shortcut for s_n = s_n + n

    print("s_n={}".format(s_n))

**Import and Initialization**

* First, the program initializes the variables :code:`s_n` to 0 and :code:`N` to 100. 

**For Loop**

Then, the program performs a :code:`for` loop statement using the :code:`range()` function. The range object generates a list of integers ranging from 1 to N (included). In each iteration, we performs the incrementation :code:`s_n = s_n + n`.
    
* 1st iteration, :code:`s_n = 0 + 1 = 1`,
* 2nd iteration, :code:`s_n = 1 + 2 = 3`,
* 3rd iteration, :code:`s_n = 3 + 3 = 6`,
* 4th iteration, :code:`s_n = 6 + 4 = 10`,
* ...

At the 100th iteration, we obtain :code:`s_n = 5050`.

While Loops
-----------

In Python, the :code:`while` statement is used to iterate as long as a certain condition is :code:`True`.

General Syntax
++++++++++++++

.. code ::

    x = 0
    while x < 10:
        x_str = input("enter a number greater or equal to 10 ? ")
        x = float(x_str)
        
This code asks for a number greater or equal to 10. If the user provides a number lower than 10, the programs asks for a new number. Note that
it is impossible to predict how many iterations the loop will perform since the number of iterations depends on the user inputs. This is the main difference with the :code:`for` loop statement.
In a :code:`for` statement, it is usually possible to predict exactly the number of iterations before runtime.

We see that the :code:`while` statement is composed of a condition. As for the :code:`if` statement, this condition can be specified using a value comparisons or a boolean expression.

Infinite Loops
++++++++++++++

.. warning ::

    If the condition is always :code:`True`, the program will continue to run forever (infinite loop). To stop a :code:`while` statement, at least one iteration must change the content of the condition to :code:`False`. 

For example, by omitting the line :code:`x = float(x_str)`, the value of :code:`x` will start to 0 and never changes. In this context, the condition :code:`x < 10` is always evaluated to :code:`True`
and the the program will continue to run forever. 

Excepts for particular programs that never ends (such as those implemented in microprocessors), note that infinite loops should **always be avoided**.

Example
+++++++

In the following example, we program a simple mathematical game. The goal is of this program is to count how many 
additions the user can compute without error.


.. code ::

    from random import randint

    counter = 0
    flag = True

    while flag:
        nb_1 = randint(0, 100)
        nb_2 = randint(0, 100)
        result = nb_1 + nb_2

        x_str = input("{} + {} = ".format(nb_1, nb_2))
        x = float(x_str)
        if x == result:
            counter += 1 
        else:
            flag = False

    print("Number of correct operations: {}".format(counter))

**Import and Initialization**

* First, we import the :code:`randint` function of the random module to generate random numbers and additions.
* Then, we initialize two variables. The variable :code:`counter` is initialized at 0 to count how many correct answers the user has given, and the variable :code:`flag` is a boolean that is initialized to :code:`True`.

**While Loop**

The while loop tests the content of the :code:`flag` variable. While :code:`flag` is equal to :code:`True`, we perform the following steps.

* First we generate a random addition. Specifically, we generate two random numbers :code:`nb_1` and :code:`nb_2` and we store the result of the addition in a variable named :code:`result`.
* Then, we ask the user to enter the result of the addition. This result is saved in a variable called :code:`x`.
* Finally, we perform a condition statement to test the equality between the content of the :code:`result` and :code:`x` variables. If :code:`x == result`, we increment the :code:`counter` variable. Else, we change the content of the :code:`flag` variable to :code:`False`.




    