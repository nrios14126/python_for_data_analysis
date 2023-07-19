
#### Chapter 4: NumPy Basics ######################################################################

# One of the key features of NumPy is its n-dimensional array, or ndarray, which is a fast, 
# flexible container for large datasets. Arrays enable you to perform math operations on whole 
# blocks of data using similar syntax to the equivalent operations between scalar elements.

### The NumPy ndarray #############################################################################

import numpy as np

# Generate some random data
data = np.random.randn(2, 3)
data

# Scalar multiplication
data * 10

# Element-wise addition
data + (data * 2)

# Note that ndarrays are of homogeneous data, that is, all of the elements must be of the same 
# type. Every array has a shape, a tuple indicating the size of each dimension, and a dtype, an
# object describing the data type of the array:
data.shape

data.dtype

## Creating Arrays ********************************************************************************

# The easiest way to create an array is to use the array() function, which accepts any 
# sequence-like object and produces an ndarray

data1 = [6, 7.5, 8, 0, 1]
arr1 = np.array(data1)
arr1

arr1.shape

arr1.dtype

# Nested sequences, like a list of lists, will be converted into a multi-dimensional array:
data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr2 = np.array(data2)
arr2

arr2.shape

arr2.ndim

# Unless specified, np.array() tries to infer a good data type for the array. The data type is 
# stored in a special dtype metadata object:
arr2.dtype

# In addition to np.array(), np.zeros() creates an array of all zeros while np.ones() creates an 
# array of all ones. There's also np.emtpy() which creates an array without any particular 
# initializations. You may pass a length or a shape (tuple) as an argument:
np.zeros(10)

np.zeros((3, 6))

np.empty((2, 3, 2))

# np.arange() is an array-valued version of the built-in Python range() function:
np.arange(15)

# You can also produce an array of the given shape and dtype with all values set to the indicated 
# fill value:
np.full((5, 5), 7)

# Create an nxn identity matrix:
np.identity(4)

## Data Types for ndarrays ************************************************************************

# The data type or dtype is a special object containing the metadata the ndarray needs to interpret 
# a chunk of memory as a particular type of data:
arr1 = np.array([1, 2, 3], dtype=np.float64)
arr2 = np.array([1, 2, 3], dtype=np.int32)

arr1.dtype

arr2.dtype

# You can explicitly convert or cast an array from one dtype to another:
arr = np.array([1, 2, 3, 4, 5])
arr.dtype

float_arr = arr.astype(np.float64)
float_arr.dtype

# If you cast floats to ints the decimal part will be truncated:
arr = np.array([1.2, 2.5, 3.7, 4.1])
arr.astype(np.int32)

# You can also use another array's dtype attribute:
int_array = np.arange(10)
calibers = np.array([.22, .270, .357, .380, .44, .50], dtype=np.float64)
int_array.astype(calibers.dtype)
int_array.dtype

## Arithmetic with Arrays *************************************************************************

# Vectorization enables you to express batch operations on data without using any for loops. Any 
# arithmetic operations between equal-size arrays applies the operations element-wise:
arr = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
arr

arr * arr

arr - arr

# Arithmetic operations with scalars propogate the scalar argument to each element in the array:
1 / arr

arr ** 0.5

# Comparisons between arrays of the same size yield boolean arrays:
arr2 = np.array([[0.0, 4.0, 1.0], [7.0, 2.0, 12.0]])
arr2

arr2 > arr

## Basic Indexing and Slicing *********************************************************************

# One-dimensional arrays are simple, they can be sliced similarly to lists:
arr = np.arange(10)
arr

arr[5]

arr[5:8]

arr[5:8] = 12
arr

# An important distinction from Python's built-in lists is that array slices are views on the 
# original array. This means that the data is not copied, and any modifications to the view will be 
# reflected in the source array:
arr_slice = arr[5:8]
arr_slice

# Now, when I change values in arr_slice, the mutations are reflected in the original array:
arr_slice[1] = 12345
arr

# If you want a copy of a slice of an ndarray instead of a view, you will need to copy the array:
arr[5:8].copy()

# In a two-dimensional array, the elements at each single index are one-dimensional arrays:
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr2d[2]

# Individual elements can be accessed recursively, or you can pass a comma-separated list of 
# indices:
arr2d[0][2]

arr2d[0, 2]

# NumPy uses axes to specify a dimension. Axis 0 refers to the rows, whereas axis 1 refers to the 
# columns for two-dimensional arrays.

# In multidimensional arrays, if you omit later indices, the returned object will be a lower 
# dimensional ndarray consisting of all the data along the higher dimensions:
arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
arr3d

# Similarly, arr3d[1, 0] gives you all of the values whose indices start with (1, 0), forming a 
# 1-dimensional array:
arr3d[1, 0]

# Like one-dimensional objects such as lists, ndarrays can be sliced with similar syntax:
arr[1:6]

# Two-dimensional arrays slice a bit differently, here it slices along axis 0, which selects a 
# range of elements along that axis.
arr2d

arr2d[:2]

# Note that a colon by itself means to take the entire axis, so you can slice only higher 
# dimensional axes by doing so:
arr2d[:2, :]

arr2d[:, :1]

# You can pass multiple slices just like you can pass multiple indexes. When slicing like this, you 
# always obtain array views of the same number of dimensions:
arr2d[:2, 1:]

# By mixing integer indexes and slices, you get lower dimensional slices:
arr2d[:2, 2]

arr2d[1, :2]

## Boolean Indexing *******************************************************************************

# Let's consider an example where we have some data in an array and an array of names with 
# duplicates:
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
data = np.random.randn(7, 4)

names

data

# Now suppose each name corresponds to a row in the data array and we wanted to select all the rows 
# with corresponding name 'Bob'. Like arithmetic, comparisons with arrays are also vectorized:
names == 'Bob'

# This boolean array can be passed when indexing the array:
data[names == 'Bob']

# The boolean array must be of the same length as the array axis it's indexing. You can also mix 
# and match boolean arrays with slices or integers:
data[names == 'Bob', 2:]

data[names == 'Bob', 3:]

# To select everything but 'Bob' you can use either '!=' or negation with '~':
data[~(names == 'Bob')]

data[names != 'Bob']

# The '~' operator can be useful when you want to invert a general condition:
cond = names == 'Bob'
data[~cond]

# Selecting two of the three names to combine multiple boolean conditions can be done using '&' or 
# '|' operators:
mask = (names == 'Bob') | (names == 'Will')
mask

data[mask]

# The Python keywords 'and' and 'or' don't work with boolean arrays. Use '&' and '|'

# Note that selecting data from an array by boolean indexing always creates a copy of the data, 
# even if the returned array is unchanged.

# Setting values with boolean arrays works in a common-sense way. To set all of the negative values 
# in data to 0 we need only do:
data[data < 0] = 0
data

# Setting whole rows or columns using a one-dimensional boolean array:
data[names != 'Joe'] = 7
data

## Fancy Indexing *********************************************************************************

# Fancy indexing describes indexing using integer arrays:
arr = np.empty((8, 4))
for i in range(8):
    arr[i] = i
arr

# To select out a subset of the rows in a particular order, you can simply pass a list or ndarray 
# of integers specifying the desired order:
arr[[4, 3, 0, 6]]

# Using negative indices selects rows from the end:
arr[[-3, -5, -7]]

# Passing multiple index arrays selects a one-dimensional array of elements corresponding to each 
# tuple of indices:
arr = np.arange(32).reshape((8, 4))
arr

arr[[1, 5, 7, 2], [0, 3, 1, 2]]

# Regardless of how many dimensions the array has, the result of fancy indexing is always 
# one-dimensional. The behavior of fancy indexing in this case is a bit unintuitive, since we 
# expect is a rectangular region of the array.

# To retrieve a rectangular region formed by selecting a subset of the matrix's rows and columns:
arr[[1, 5, 7, 2]][:, [0, 3, 1, 2]]

# Note that fancy indexing (unlike slicing) always copies the data into a new array.

## Transposing Arrays and Swapping Axes ***********************************************************

# Transposing is a special form of reshaping that similarly returns a view on the underlying data 
# without copying anything.

arr = np.arange(15).reshape((3, 5))
arr

# Using the transpose attribute:
arr.T

# Using the transpose method:
arr.transpose()

# When computing the inner matrix product:
arr = np.random.randn(6, 3)
arr

np.dot(arr.T, arr)

# For higher dimensional arrays, transpose() will accept a tuple of axis numbers to permute the 
# axes:
arr = np.arange(16).reshape((2, 2, 4))
arr

# Here, the axes have been reordered with the second axis first, the first axis second, and the 
# last axis unchanged:
arr.transpose((1, 0, 2))

# Simple transposing with array.T is a special case of swapping axes. There is a method swapaxes() 
# that takes a pair of axis numbers and switches the indicated axes to rearrange the data:
arr

# This will return a view on the data wihtout making a copy:
arr.swapaxes(1, 2)

### Universal Functions ###########################################################################

# A universal function performs element-wise operations on data in ndarrays. You can think of them 
# as fast vectorized wrappers for simple functions that take one or mor scalar values and produce 
# one or more scalar results. 

arr = np.arange(10)
arr 

np.sqrt(arr)

np.exp(arr)

# These are referred to as 'unary' functions. Others, such as add() or maximum() take
# two arrays, so they are 'binary' functions:
x = np.random.randn(8)
y = np.random.randn(8)

# Compute element-wise maximum between x and y
np.maximum(x, y)

# While not common, a universal function can return multiple arrays. For example, modf() returns 
# the fractional and integral parts of a floating-point array:
arr = np.random.randn(7) * 5
arr

remainder, whole_part = np.modf(arr)

remainder

whole_part

# Unary functions accept an optional out argument that allows them to operate in-place on arrays:
arr

np.sqrt(x = arr)

np.sqrt(x = arr, out = arr)

arr
