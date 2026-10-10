# Question 1: Array from a list and its attributes

## Aim

Create a NumPy array from the list [3, 6, 9, 12, 15] and print its shape, ndim, size and dtype.

## Code

```python
import numpy as np

arr = np.array([3, 6, 9, 12, 15])
print("Array :", arr)
print("Shape :", arr.shape)
print("ndim  :", arr.ndim)
print("Size  :", arr.size)
print("dtype :", arr.dtype)
```

## Output

```
Array : [ 3  6  9 12 15]
Shape : (5,)
ndim  : 1
Size  : 5
dtype : int64
```

## Explanation

`np.array()` converts the Python list into an ndarray. The attributes describe it:
- `shape` is a tuple of dimension lengths. `(5,)` means one axis with 5 elements.
- `ndim` is the number of axes (1 here).
- `size` is the total number of elements (5).
- `dtype` is the element type. Python integers become `int64` on most 64-bit systems (it can be `int32` on Windows with older NumPy versions).