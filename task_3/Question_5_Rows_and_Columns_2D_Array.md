# Question 5: Rows and columns of a 2-D array

## Aim

Create `a = np.arange(1, 36).reshape(5, 7)` and print the 3rd row, the 4th column, the last row and the last column.

## Code

```python
import numpy as np

a = np.arange(1, 36).reshape(5, 7)
print("Array:\n", a)
print("3rd row    :", a[2])
print("4th column :", a[:, 3])
print("Last row   :", a[-1])
print("Last column:", a[:, -1])
```

## Output

```
Array:
 [[ 1  2  3  4  5  6  7]
  [ 8  9 10 11 12 13 14]
  [15 16 17 18 19 20 21]
  [22 23 24 25 26 27 28]
  [29 30 31 32 33 34 35]]
3rd row    : [15 16 17 18 19 20 21]
4th column : [ 4 11 18 25 32]
Last row   : [29 30 31 32 33 34 35]
Last column: [ 7 14 21 28 35]
```

## Explanation

`reshape(5, 7)` arranges the 35 numbers into 5 rows and 7 columns. Indexing is zero-based, so the 3rd row is `a[2]` and the 4th column is `a[:, 3]`. The colon means "all rows". Negative indices count from the end, so `a[-1]` is the last row and `a[:, -1]` is the last column.