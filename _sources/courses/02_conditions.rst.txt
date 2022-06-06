Conditional Statements
======================

Introduction
------------

In the previous chapter, we have implemented simple programs where every line of code is executed sequentially.
However, it is pretty common to use **flow control statements**. This section focuses on a particular subclass of flow control statements called conditional statements. 
A condition statement executes a specific line of codes (or block of codes) only if a condition is met.


Usage
-----

General Syntax
++++++++++++++

A condition statement is composed of a :code:`if...else` statement that checks if a boolean condition is :code:`True` or :code:`False`. Then, depending on the 
value of the condition, the program is routed to a particular block of codes.

.. code ::

    if condition: 
        # first block of code 
    else:
        # second block of code


.. warning ::

    In Python, a block of code is delimited by an indentation that is specified using 4 spaces. Each block of codes can contain one or several lines of codes.

.. warning ::

    A :code:`if` statement always ends with the character :code:`:`


Example
+++++++

The following code implements a simple program that generates a random number and checks its parity (odd or even).

.. code ::
    
    from random import randint

    my_number = randint(0,20)

    if (my_number % 2) == 0:
        # code block indented 4 spaces
        print("the number {} is even", format(my_number))
    else:
        # code block indented 4 spaces
        print("the number {} is odd", format(my_number))


Import and Initialization
`````````````````````````

* First, we import the :code:`randint` function of the random module to generate a random number.
* Then, we generate a random number between 0 and 20 (excluded)

Conditional Statement
`````````````````````

The code is composed of the following conditional statement :code:`if (my_number % 2) == 0:`. This particular statement performs multiple operations.

1. First, the modulo arithmetic operator :code:`x % y` computes the remainder of the integer division x/y. In our particular case, the expression :code:`my_number % 2` can only return two values: 

* 0 if :code:`my_number` can be divided by two (even),
* 1 if :code:`my_number` cannot be divided by two (odd).

2. The line :code:`(my_number % 2) == 0` performs an equality test using the operator :code:`==`.

* If :code:`(my_number % 2)` is equal to 0 (i.e., :code:`my_number` is even), the expression returns the boolean value :code:`True`,
* If :code:`(my_number % 2)` is equal to 1 (i.e., :code:`my_number` is odd),  the expression returns the boolean value :code:`False`.

3. Finally, the conditional statement :code:`if ...` routes the program to the appropriate block of code depending on the result of the equality test. 

As highlighted in this first example, making a conditional statement usually requires two main ingredients.

* A condition that returns a :code:`True` or :code:`False` value,
* A :code:`if`, :code:`if / else` or :code:`if / elif / else` statement for routing the program to the appropriate block of code.

Conditions
----------

This section describes the most classical ways to write a condition in Python.

Value comparisons
+++++++++++++++++

For value comparisons, the general syntax is given by 

.. code ::

    value1 operator value2

where :code:`operator` compares the values of two objects. For example, :code:`(my_number % 2) == 0` includes the operator :code:`==`. 
In Python, the most used operators are

* :code:`<`: returns :code:`True` if the left value is lower than the right value,
* :code:`>`: returns :code:`True` if the left value is greater than the right value,
* :code:`==`: returns :code:`True` if the left value is equal to the right value,
* :code:`<=`: returns :code:`True` if the left value is lower or equal to the right value,
* :code:`>=`: returns :code:`True` if the left value is greater or equal to the right value,
* :code:`!=`: returns :code:`True` if the left value is not equal to the right value.

.. warning ::

    * The operator :code:`==` corresponds to a test.
    * The operator :code:`=` corresponds to a variable assignement.


Boolean operations
++++++++++++++++++

The following operators can generate a boolean value from one or two conditions. 

* :code:`or`: returns :code:`True` if either the left boolean or the right boolean is True.
* :code:`and`: returns :code:`True` if the left boolean and the right boolean are True.
* :code:`not`: returns :code:`True` if the boolean is False.

If statements
-------------

In some situations, it is only interesting to route the program to a particular block of codes if the condition is :code:`True`. Other programs also require
explicitly routing the program to another block of codes if the condition is :code:`False`. To take into account the diversity of situations,
the Python language includes different declinations of the :code:`if` statement.

Simple statement
++++++++++++++++

.. code ::

    if boolean_value:
        print("value is true")

The simple :code:`if` statement executes the following block of code only if the condition is met.

If / Else statement
+++++++++++++++++++

.. code ::

    if boolean_value:
        print("show if true")
    else:
        print("show if false")

The simple :code:`if/else` statement executes the first block of code only if the condition is met. Else, it executes the second block of code.

If / Elif / Else statement
++++++++++++++++++++++++++

.. code ::

    if value < 10:
        print("value is lower than 10")
    elif value < 20:
        print("value is between 10 and 20")
    else:
        print("value is greater or equal to 20")

The simple :code:`if/elif/else` statement executes the first block of code only if the condition is met. Else, it evaluates the condition
specified by the :code:`elif`. If this second condition is met, it executes the second block of code. Else, it executes the block of code associated with the :code:`else` statement. Note that the :code:`if/elif/else` statement can be composed of 
multiple :code:`elif`.

