#!/usr/bin/env python

"""Answers to linear algebra questions.

Each test yielding an error means the answer is "not defined."

>>> A.shape
(2, 3)
>>> B.shape
(2, 2)
>>> C.shape
(3, 2)
>>> D.shape
(2, 3)
>>> u.shape
(4,)
>>> w.shape
(4, 1)
>>> print(u + v)
[ 9  7 -4  9]
>>> print(u - v)
[ 3 -3 -2  1]
>>> print(6 * u)
[ 36  12 -18  30]
>>> print(u.dot(v))
51
>>> print(la.norm(u))  # doctest: +ELLIPSIS
8.602...
>>> A + C  # doctest: +ELLIPSIS
Traceback (most recent call last):
...
ValueError: operands could not be broadcast together with shapes ...
>>> print(A - C.transpose())
[[-4 -7 -3]
 [ 3  6  4]]
>>> print(C.transpose() + 3 * D)
[[14  3  3]
 [ 2  7  9]]
>>> print(B.dot(A))
[[-1 -5 -1]
 [ 2  7  4]]
>>> print(B.dot(A.transpose()))  # doctest: +ELLIPSIS
Traceback (most recent call last):
...
ValueError: shapes ... not aligned: ...
>>> print(B.dot(C))  # doctest: +ELLIPSIS
Traceback (most recent call last):
...
ValueError: shapes ... not aligned: ...
>>> print(C.dot(B))
[[ 5 -6]
 [ 9 -8]
 [ 6 -6]]
>>> print(B.dot(B).dot(B).dot(B))
[[ 1 -4]
 [ 0  1]]
>>> print(A.dot(A.transpose()))
[[14 28]
 [28 69]]
>>> print(D.transpose().dot(D))
[[10 -4  0]
 [-4  8  8]
 [ 0  8 10]]
"""

from numpy import linalg as la
import doctest
import numpy as np

A = np.array([[1, 2, 3], [2, 7, 4]])
B = np.array([[1, -1], [0, 1]])
C = np.array([[5, -1], [9, 1], [6, 0]])
D = np.array([[3, -2, -1], [1, 2, 3]])
u = np.array([6, 2, -3, 5])
v = np.array([3, 5, -1, 4])
w = np.array([[1], [8], [0], [5]])


if __name__ == '__main__':
    doctest.testmod()
