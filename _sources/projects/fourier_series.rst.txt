Fourier Series Synthesizer 
==========================

The goal of this project is to create a `Fourier series synthesizer <https://en.wikipedia.org/wiki/Fourier_series>`_ with a user interface.

Mathematical Model 
------------------

The amplitude-phase form decomposition is given by

.. math :: 

    x(t) = \sum_{l=0}^{L} a_l \cos(2\pi l f_0 t+\phi_l)

where 

* :math:`f_0` is the fundamental frequency,
* :math:`a_l` and :math:`\phi_l` are the Fourier coefficient.

First Part 
----------

The objective of the first part is to draw the waveform :math:`x(t)` with :math:`t=n/F_s` where 
:math:`F_s` is the sampling frequency.

Instructions 
++++++++++++

* Using Numpy, create a time vector ranging from :math:`t=0` s to :math:`t=1` s.
* Using Numpy, compute the vector :math:`x(t)`.
* Using Matplotlib, draw the waveform :math:`x(t)`

Example
+++++++

Parameters :

.. code ::

    Fs = 1000
    f0 = 1
    a = np.array([0, 1, 0, 1/3, 0, 1/5, 0, 1/7, 0])
    phi = (np.pi/2)*np.ones(8)

Result :

.. image:: img/fourier1.png
    :width: 400
    :align: center
    :alt: Alternative text


Second Part 
-----------

The objective of the second part is to create a user interface using tkinter for specifying the values of :math:`a_l` and :math:`phi_l` .

Instructions 
++++++++++++

* Using Tkinter (see tutorials section) with two frames, create the following interface with user entries for specifying the values of :math:`a_l`  

.. image:: img/fourier2.png
    :width: 400
    :align: center
    :alt: Alternative text

* Using Tkinter and the first part of your project, makes the connection between the User Interface (UI) and the numpy/matplotlib code using the default Parameters

.. code ::

    Fs = 1000
    f0 = 1
    phi = (np.pi/2)*np.ones(8) 

.. image:: img/fourier3.png
    :width: 400
    :align: center
    :alt: Alternative text