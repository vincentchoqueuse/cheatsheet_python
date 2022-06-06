Exercice 5
++++++++++

Create a function that computes the `binomial coefficient <https://en.wikipedia.org/wiki/Binomial_coefficient>`_ :math:`C(n,k)`, which is mathematically defined as
is defined as 

.. math 

    C(n,k) = \frac{n!}{k!(n-k)!}

where :math:`N!=1\times 2\times \cdots \times N` corresponds to the factorial. To evaluate this expression, you should also create
a function :code:`factorial` that computes the factorial (without using the math module). 

**Prototype 1**

    :name: `factorial`
    :inputs: n (an integer)
    :outputs: n_fact (a float)

**Prototype 2**

    :name: `comb`
    :inputs: 
        * n (an integer)
        * k (an integer)
    :outputs: Cnk (a float)

**Test**

After the instruction :code:`output = comb(5, 2)`, the value of output must be 10.
