
Exercice 4
++++++++++

The Exclusive or (XOR) or exclusive disjunction is a logical operation that is true if and only if its arguments differ. Let us consider two booleans :code:`value1` and :code:`value2`. 
The result of a XOR operation is equal to:

* :code:`1` if **exactly one of the two booleans** is equal to 1,
* :code:`0` in all the other cases.

.. list-table:: XOR Operator
   :widths: 25 25 25
   :header-rows: 0
   :align: center

   * - **XOR**
     - False
     - True
   * - False
     - :code:`False`
     - :code:`True`
   * - True
     - :code:`True`
     - :code:`False`

Write a Python program that takes as inputs two booleans and displays the result of the XOR operation using only :code:`and` and :code:`or` boolean operations.

**Specifications**

* Program Name: :code:`chap2_ex4.py`
* Input: two booleans :code:`value1, value2`  (must be provided by the user using :code:`input` function)
