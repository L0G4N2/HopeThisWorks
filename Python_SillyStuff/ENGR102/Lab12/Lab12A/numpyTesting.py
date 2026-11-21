# By submitting this assignment, all team members agree to the following:
#   “Aggies do not lie, cheat, or steal, or tolerate those who do”
#   “I have not given or received any unauthorized aid on this assignment”
#
# Names:        Logan Gutierrez 737008832
#               Daniel Vicari 738004466
#               Zachary Adams 637008110
#               Harshil Patel 838007668
# Section:      555
# Assignment:   numpy_example
# Date:         12 November 2026

import numpy as np

# The Basics
x = np.array([1, 2, 3])
print("The array: ", x)
print("Dimensions: ", x.ndim)
print("Shape: ", x.shape)
print("Size: ", x.size)
print("Date Type: ", x.dtype)
print("Item Size: ", x.itemsize)
print("Data: ", x.data)
print()

## An Example
a = np.arange(15).reshape(3, 5)
print(a)
print(a.shape)
print(a.ndim)
print(a.dtype.name)
print(a.itemsize)
print(a.size)
print(type(a))
print()

b = np.array([6, 7, 8])
print(b)
print(type(b))
print()

## Array Creation

### Part 1
a = np.array([2, 3, 4])
print(a)
print(a.dtype)
b = np.array([1.2, 3.5, 5.1])
print(b.dtype)
print()

### Error when creating an array
# a = np.array(1, 2, 3, 4)    # WRONG
a = np.array([1, 2, 3, 4])  # RIGHT

### Arrays can transform sequences to the same data type
b = np.array([(1.5, 2, 3), (4, 5, 6)])
print(b)
print()

### The data type of the array can also be specified at creation
c = np.array([[1, 2], [3, 4]], dtype=np.complex128)
print(c)
print()

### There exist two functions .zeroes() and .ones() that create an empty array with contents of 0 and 1
print("Zeroes: \n", np.zeros((3, 4)))
print("Ones: \n", np.ones((2, 3, 4), dtype=np.int16))
print("Empty: \n", np.empty((2, 3)))
print()

### Creating an array using .arange() [uses range() to return an array]
print("Using .arange() to create an array")
print(np.arange(10, 30, 5))
print(np.arange(0, 2, 0.3))  # it accepts float arguments
print()

### Using .linspace() to return a known number of values in a given range
from numpy import pi
print(np.linspace(0, 2, 9))                   # 9 numbers from 0 to 2
x = np.linspace(0, 2 * pi, 100)               # useful to evaluate function at lots of points
print(x)
f = np.sin(x)
print(f)
print()

## Printing Arrays

a = np.arange(6)                    # 1d array
print("1D Array: \n", a)
b = np.arange(12).reshape(4, 3)     # 2d array
print("2D Array: \n", b)
c = np.arange(24).reshape(2, 3, 4)  # 3d array
print("3D Array: \n", c)
print()

### Using .reshape() and understanding the limits to printing an array
print("Printing one dimension: \n", np.arange(10000))
print("Printing three dimesions: \n", np.arange(10000).reshape(100, 100))
# This line changes how Python prints the array (print everything)
# np.set_printoptions(threshold=sys.maxsize)  # sys module should be imported
print()

## Basic Operations

a = np.array([20, 30, 40, 50])
b = np.arange(4)
print(b)
c = a - b
print(c)
print(b**2)
print(10 * np.sin(a))
print(a < 35)
print()

### Matrix Products (Dot Product)
A = np.array([[1, 1],
              [0, 1]])
B = np.array([[2, 0],
              [3, 4]])
print("Element Wise: \n", (A * B))          # elementwise product
print("Matrix Product: \n", (A @ B))        # matrix product
print("Matrix Product: \n", (A.dot(B)))     # another matrix product
print()

### Modifying arrays with the reassignment operators
rg = np.random.default_rng(1)  # create instance of default random number generator
a = np.ones((2, 3), dtype=np.int_)
b = rg.random((2, 3))
a *= 3
print(a)
b += a
print(b)
# a += b  # ERROR: b is not automatically converted to integer type
print()

### Upcasting
a = np.ones(3, dtype=np.int32)
b = np.linspace(0, pi, 3)
print("Data Type Name: ", b.dtype.name)
c = a + b
print(c)
print("Data Type Name: ", c.dtype.name)
d = np.exp(c * 1j)
print(d)
print("Data Type Name: ", (d.dtype.name))
print()

### Using .sum(), .max(), and .min()
a = rg.random((2, 3))
print(a)
print("Sum: ", a.sum())
print("Min: ", a.min())
print("Max: ", a.max())
print()

### Using the axis=n to apply certain operations for a specific axis
b = np.arange(12).reshape(3, 4)
print(b)
print("Sum of each column: ", b.sum(axis=0))     # sum of each column
print("Min of each row: ", b.min(axis=1))     # min of each row
print("Cumulative Sum of each row: \n", b.cumsum(axis=1))  # cumulative sum along each row
print()

## Universal Functions

print("Universal Functions")
B = np.arange(3)
print(B)
print("Exponent: ", np.exp(B))
print("Square Root: ", np.sqrt(B))
C = np.array([2., -1., 4.])
print("Add: ", np.add(B, C))
print()

# Shape Manipulations

## Changing the shape of an array
a = np.floor(10 * rg.random((3, 4)))
print("Array: \n", a)
print("Shape: ", a.shape)
print()

### The shape of an array can be changed with various commands without modifying the original array
print("Flattened Array: \n", a.ravel())  # returns the array, flattened
print("Reshaped Array: \n", a.reshape(6, 2))  # returns the array with a modified shape
print("Transposed Array: \n", a.T)  # returns the array, transposed
print("Transposed Shape: ", a.T.shape)
print("Original Shape: ", a.shape)
