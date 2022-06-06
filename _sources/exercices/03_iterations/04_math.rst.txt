Exercice 4
++++++++++

Write a Python program that approximates the `inverse square root <https://en.wikipedia.org/wiki/Fast_inverse_square_root>`_ given by 

.. math ::

    y = f(x) = \frac{1}{\sqrt{x}}

without the use of the :code:`math` module. For example, the inverse square root of :math:`x=0.15625` is approximately equal to :math:`y\approx 2.52982`.

To compute the inverse square root :math:`y` we propose to find the root 
:math:`g(y) = 0` where :math:`g(y)=\frac{1}{y^2} -x` using the Newton's method. After some computations, it can be checked that the application 
of the Newton's method leads to the following iterative procedure.

1. Initialize the value :math:`y_0=1`
2. Update the value of :math:`y` using the iterative procedure

.. math ::

    y_{n+1} = \frac{y_n (3-xy_n^2)}{2}

At the end the Lth iteration, the approximate value of :math:`y` is given by :code:`y_{L}`. In your implementation, you will use :code:`L=5` iterations to approximate :math:`y`.

**Specifications**

* Program Name: :code:`chap3_ex4.py`
* Input: a float :code:`x` (must be provided by the user using :code:`input` function)
