Exercice 6
++++++++++

Write a Python program that approximates the function :math:`\text{arctan}(x)` using the Taylor serie 

.. math ::

    \text{arctan}(x) = \sum_{n=0}^{L} \frac{(-1)^n}{2n+1}x^{2n+1} = x- \frac{x^3}{3} + \frac{x^5}{5} - \cdots

The program should display:

* the approximate value of :math:`\text{arctan}(x)`,
* the exact value of :math:`\text{arctan}(x)` obtained with the :code:`math` module for comparison.

In your implementation, you will use :code:`L=5`.

**Specifications**

* Program Name: :code:`chap3_ex6.py`
* Library: :code:`math` (see `documentation <https://docs.python.org/3/library/math.html>`__)
* Input: a float :code:`x` (must be provided by the user using :code:`input` function)
