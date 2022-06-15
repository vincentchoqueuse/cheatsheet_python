Exercice 6
++++++++++

Create a Python function that draw a sinewave with the module and matplotlib modules using the mathematical expression 

.. math ::

    x[n] = a\sin(2\pi f n/Fe)

for :math:`n=0,1,2,..., N-1`

**Prototype**

    :name: `show_sine`
    :inputs: 
        * f (a float)
        * a (a float)
        * Fe (a float)
        * N (an integer)
    :outputs: None (the function only plots a figure)

.. note ::

    To evaluate the mathematical expression, it is recommended to use the :code:`arange` and :code:`sin` function of the Numpy module.