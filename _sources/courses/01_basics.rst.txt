Python Basics 
=============

Hello World
-----------

First Program 
+++++++++++++

To test our installation, we will write a simple program that displays the message :code:`"Hello World"` on the standard output.

* Create a file called `01_first.py`,
* Open it with a text editor and write

.. code ::

    print("Hello World")

* open your terminal in the folder of your script and then run the following command 

.. code :: bash

    $ python 01_first.py


This program should print the message :code:`Hello World` in your terminal. 

Let's dive into the code. This simple program is composed of a single line of code. This line of code calls the function :code:`print()`. This function belongs to a list of built-in functions in Python. 
It takes as input argument a string (a message) delimited by :code:`"."`, and outputs the input message on the standard output (your screen).

    **Read the doc :** The documentation of the built-in functions is available `here <https://docs.python.org/3/library/functions.html>`_ .

.. note :: 

    Understand your interpreter ! If your code contains an error, your interpreter will raise an error at runtime. Hopefully, the Python interpreter will give you 
    some indications about your error (type of error, location of the error in your code). For example, replacing your code by
    
    .. code ::
        
        print("Hello World)
        
    will raise the error :code:`SyntaxError: EOL while scanning string literal`. This means that Python has detected an "End of Line" before a string message has been properly closed.

Comments
++++++++

In Python codes, lines beginning with :code:`#` are not interpreted at runtime. 
In practice, these lines can be used to comment on some parts of our code. For example, 
the following code is strictly equivalent to our first code at runtime.

.. code :: python 

    # This is my first Python code 
    print("Hello World")

    # bring out the Champagne bro

You can also comment several lines using the syntax :code:`"""."""`.

.. code :: python 

    """ This is my first Python code
    This code is composed of a long comment. 
    Bring out the Champagne bro !
    """

    print("Hello World")


Variables
---------

In Python, everything is an object. Python is a dynamically typed language, i.e., the type of an object is determined during runtime. 
It is possible to get the type of an object using the built-in function :code:`type()`. For example, the following code displays the type of the number :code:`3.14`.

.. code :: python 

    # display the type of 3.14
    print(type(3.14))

The output shows that the type is :code:`<class 'float'>`. This type belongs to the category of numeric types. 

Built-in Types
++++++++++++++

Built-in Python types can be classified in 6 categories.

* Booleans: :code:`True`, :code:`False`,
* Numeric Types: :code:`int`, :code:`float`, :code:`complex`,
* Text Sequence Type (string): :code:`str`,
* Mapping Types: :code:`dict`,
* Sequence Types: :code:`list`, :code:`tuple`, :code:`range`,
* (Binary Sequence Types: :code:`bytes`, :code:`bytearray`, :code:`memoryview`)


Assignement
+++++++++++

In Python, the content of an object can vary during the code execution. For this reason, we commonly used the 
term variable. A variable is described by its name, which acts like a 
label. This label can be used to easily access its content. 

The content of a variable can be assigned using the operator :code:`=`. For example, the following code shows how to assign the value 3.14 to 
a variable named :code:`my_var`.

.. code ::

    # assign the content of a variable
    my_var = 3.14

It is then possible to print the content of :code:`my_var` as follows

.. code ::

    # print the content of a variable
    print(my_var)


Examples 
````````

.. code ::

    my_boolean = True 
    my_integer = 3
    my_float = 3.245
    my_string = "hello world"
    my_dict = {"firstname": "toto", "lastname": "tata"}
    my_list = [1, 10, 20, 30]
    my_tuple = (1, 10, 20, 30)

Note that Python automatically chooses the "most appropriate" type for each variable based on its content.

Sequence Types
``````````````

For sequence types such as string, list, (the value of) one particular element can be assigned using the syntax :code:`var[index] = value`, where :code:`index` corresponds to 
the index of the element to be changed. 

The following program show how to modify the second element of a list.


.. code :: python 

    # initialisation 
    my_list = [2, 10, 5, 20]

    # algorithm
    print("before: my_list={}".format(my_list))
    my_list[1] = 15
    print("after: my_list={}".format(my_list))

.. note :: 

    In Python, the index of the first element of a sequency type is 0.

It is also possible to assign one particular element of a list to a variable using the following syntax 

.. code :: python 

    # initialisation 
    my_list = [2, 10, 5, 20]

    # algorithm
    value = my_list[2]
    print("Third element: value={}".format(value))


Operations
++++++++++

Each built-in type supports a list of operation. An operation can be described by the general form

.. code ::

    operand1 operator operand1

For example, it is possible to use a mathematical operation between two numbers

.. code ::

    result = 3 + 6
    print(result)

where `operand1` corresponds to the value 3 (an integer), `operation` corresponds to the mathematical addition, and `operand2` corresponds to value 6 (an integer).


    **Read the doc :** The methods and operators of the built-in types are described in the official `documentation <https://docs.python.org/3/library/stdtypes.html>`_ .

It is also possible to perform an operation between two operands with different types. 
When using an operator between two operands with different types, it is important to check if the operand types are compatible. 
For example, it is possible to use a mathematical operator between an integer and a float:

.. code ::

    result = 3 + 3.245 # result will be a float
    print(result)

However, the following code will raise an error.

.. code ::

    result = 3 + "15"
    print(result)

Indeed, Python raises the following error during runtime:

.. code ::

    Type error: TypeError: unsupported operand type(s) for +: 'int' and 'str'

This error means that Python does not know how to add the integer :code:`3` with the string :code:`"15"`.

The operation used between two operands depends on the operand types. Indeed, let us consider the following code 

.. code ::

    result = "3" + "15"
    print(result)

This program displays the result :code:`"315"`. Indeed, when used between two strings, the operation :code:`+` corresponds to a string concatenation. Therefore, 

 

Examples
--------

Mathematical Program
++++++++++++++++++++

In this example, we will create a simple python code that computes the circumference of a circle from its radius. Mathematically, the circumference of 
a circle is given by

.. math ::

    C = 2\pi r

where :math:`r` corresponds to the circle radius. To implement this expression, we first propose to approximate :math:`\pi` by 
:code:`my_pi = 3.14`.

.. code :: python 

    r = 10
    my_pi = 3.14
    output = 2 * my_pi * r
    print(output)

The above code uses a coarse approximation of :math:`\pi`. In python, a better approximation of :math:`\pi` is available in the 
module :code:`math`. The module :code:`math` provides access to some classical mathematical constants and functions. 

    **Read the doc :** The documentation for the module :code:`math` is available `here <https://docs.python.org/3/library/math.html>`_ .

Using the mode :code:`math`, our code can be rewritten as

.. code :: python 

    from math import pi

    r = 10
    result = 2 * pi * r
    print(result)

There are several ways to further improve our program. First, the above example displays the circle circumference without showing any indication to the user (does the output corresponds to the circumference, the radius, or something else ?). 
It is usually a bad practice to display information without contextualization.
To contextualize our output, we can mix both a static message and the content of a variable using the :code:`format` method. 
For example, the next code shows how to display the message :code:`the circumference is {}` where :code:`{}` is replaced by the content of the variable `output`. 

.. code :: python 

    from math import pi

    r = 10
    result = 2 * pi * r
    print("the circumference is={}".format(result))

The method :code:`format()` is a particular function for string. A string calling this method contains literal text or replacement fields delimited by braces :math:`{}`.
This method allows one or multiple arguments, separated by a :code:`,`. The number of provided arguments must match the number 
of :code:`{}` in the message. For example, the next code shows how to print the radius and the circumference. 

.. code :: python 

    from math import pi

    r = 10
    result = 2 * pi * r
    print("the circumference of a circle of radius={} is={}".format(r, result))

To make this code more interactive, we will ask the user for the value of the circle radius :code:`r`. This behavior can be achieved using the :code:`input` built-in function. The built-in function waits for a user input message.
The output of this function is a text sequence. This text sequence can be converted into a numeric value using the 
:code:`float` build-in function. 

.. code :: python 

    from math import pi

    text_value = input("Value of the radius ? ")
    r = float(text_value)
    result = 2 * pi * r
    print("the circumference is={}".format(result))


Turtle Drawing
++++++++++++++

In this example, we will draw a simple shape (a rectangle) using the `Turtle <https://docs.python.org/3/library/turtle.html>`_ drawing module.
A basic usage of the Turtle module is provided below. This example simply draws a solid line. 

.. code ::

    # Import the turtle module
    import turtle

    # Create a new Turtle object called my_turtle
    my_turtle = turtle.Turtle()

    # Call the forward method to move the turtle
    my_turtle.forward(50)

    # display the result
    turtle.done()

Imagine we want to draw a rectangle with width :code:`x` and height :code:`y` using the Turtle Module. To make the program more interactive, we also want that the user
specifies the width and height at runtime n. 

To implement this program, one solution is to use the following procedure

* Create two variables :code:`x` and :code:`y` to store the rectangle width and height. The contents of these variables can be set at runtime by the user using the :code:`input` built-in function,
* Create a :code:`Turtle` object using Turtle Module, 
* Construct the rectangle by using the methods :code:`forward(.)` and :code:`right(.)` (rotation by several degrees)

The final code is provided below

.. code ::

    import turtle

    # get width and height
    x_str = input("Rectangle width ? ") 
    x = float(x_str)
    y_str = input("Rectangle height ? ") 
    y = float(y_str)

    # create the turtle
    my_turtle = turtle.Turtle()
    my_turtle.forward(x)
    my_turtle.right(90)
    my_turtle.forward(y)
    my_turtle.right(90)
    my_turtle.forward(x)
    my_turtle.right(90)
    my_turtle.forward(y)
    my_turtle.right(90)

    turtle.done()

