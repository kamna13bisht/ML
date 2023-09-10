#!/usr/bin/env python
# coding: utf-8

import numpy as np
height=[170,130,120,170,111]
me = np.mean(height)
me

height.sort()
med = np.median(height)
med

import statistics as stat
mo = stat.mode(height)
mo

v = np.var(height)
v

sd = np.std(height)
sd

import sympy as sy

def f(x):
	return x**2

x = sy.Symbol("x")
print(sy.integrate(f(x), (x, 0, 2)))

from sympy import symbols , diff
x = symbols('x')
f = x**3 - 2*x**2 -5*x + 1
f_prime = diff(f,x)
f_prime

