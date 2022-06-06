Exercice 3
++++++++++

Create a Python function that compute the running average of a list of numbers. A running average is computed as follows

.. math ::

    y[n] = \frac{x[n] + x[n-1]}{2}

where :math:`x[n]` and :math:`y[n]` for :math:`n=0,1,...,N-1` corresponds to the input and output arguments of the function.
For the first value :math:`n=0`, it is assumed that :math:`x[-1]=0`.

**Prototype**

    :name: `fir`
    :inputs: number_list (a list of float)
    :outputs: output_list (a list of float)

**Test**

After the instruction :code:`output = fir([19, 15, 5, 11])`,  the value of output must be :code:`[9.5, 17, 10, 8]`