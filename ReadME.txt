This is a Polynomial class built in Python.

In the Polinomi.py file you can find the class written in Python.

I suggest to use the Polinomi.ipynb to work with, because, thanks to sympy, it has the same functions of the Polinomi.py file, but 
its output is in latex, and, again thanks to sympy, it is then better to work with polymomials.

ONE IMPORTANT THING TO KEEP IN MIND:
If you want to use the sympy output use the operators "+" "*", "-", and the .latex() method, so for example:

c = polinomio([1, 1, 1])
d = polinomio([1, 1])
(c+d).latex()

The output will be x^2 + 2x + 2 written in latex

For the division instead it is already implemented by deafault, so:

c = polinomio([1, 2, 1])
d = polinomio([1, 1])
c/d

The output will be x + 1 written in latex

If you use the print function instead, so the __str__() method, you will have to use print(c+d) and you will see exactly this:
x^2 + 2x + 2

This will not work for the division, due to the .latex() method already implemented.
In the future all the methods will have latex output as deafault

IMPORTANT:

Due to an issue, when you do the division the first result is correct. When you load again the cell, or do another divsion, the result is not
correct. This is something I have to fix, but for now, when you are doing your second division, after having inizialized the polinomi class, reload again 
also that cell