# Numerical Intergration 
### Rectangle Integration
##### Left

L = delta<sub>x</sub>( f(x<sub>0</sub>) + f(x<sub>1</sub>) +....+ f(x<sub>n-1</sub>))

##### Right 
R = delta<sub>x</sub>( f(x<sub>0</sub>) + f(x<sub>1</sub>) +....+ f(x<sub>n</sub>))
### Trapezoidal Integration
T = (1/2) delta<sub>x</sub>( f(x<sub>0</sub> + f(x<sub>1</sub>) +....+ f(x<sub>n-1</sub>) ) +
    (1/2) delta<sub>x</sub>( f(x<sub>0</sub>) + f(x<sub>1</sub>) +....+ f(x<sub>n</sub>) )
### Exact Integration
a∫b f(x)dx = F(b) - F(a)
### Installation
Download python 3.85 at:
https://www.python.org/ftp/python/3.8.5/python-3.8.5.exe


To run each python file in linux, please use python3

For Example:

```sh
$ python3 main.py

$ python3 polynomial.py

$ python3 integration.py
```
To run each python file in windows, please use python

For Example:
```sh
$ python main.py

$ python polynomial.py

$ python integration.py
```
Run python3 main.py to compute the integral of polynomials:
```sh
$ python3 main.py

Welcome to the Numerical Integration Computer! 
Given the degree, coeffecients, lower bound, upper bound and number of subdivisions of any polynomial,   
this program will compute the Rectangular, Trapezoidal and Exact Integrals of any polynomial!
Enjoy!
Happy Calc-ing!
Please enter the degree of the polynomial: 2
Please enter the coeficiants seperated by spaces: 1 2 1
What is the lower bound: 0
What is the upper bound: 1
Please choose 1. Rectangular, 2. Trapezoid, 3. Exact: 2
Please choose n: 4
[0.25, 0.5, 0.75, 1.0]

2.34375
Would you like to do another calculation? y or n?: y


```


To test, run python3 integration.py and python3 polynomial.py:
```sh
$ python3 polynomial.py

....
----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK

$ python3 integration.py
....
----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK

```

```sh
Would you like to do another calculation? y or n?: n

Thank you for choosing the Numerical Integrations Challenge
Brought to you by AccuWeather!....All Weather, All the Time!!!
```