# Question 15: Row and column vectors

## Aim

Given `a = np.array([1, 2, 3, 4, 5, 6])`, make a row vector (1, 6) and a column vector (6, 1), once with `np.newaxis` and once with `np.expand_dims`.

## Code

```python
import numpy as np

a = np.array([1, 2, 3, 4, 5, 6])

row_1 = a[np.newaxis, :]
col_1 = a[:, np.newaxis]
row_2 = np.expand_dims(a, axis=0)
col_2 = np.expand_dims(a, axis=1)

print("np.newaxis    -> row:", row_1.shape, " column:", col_1.shape)
print("expand_dims   -> row:", row_2.shape, " column:", col_2.shape)
print("Row vector:\n", row_1)
print("Column vector:\n", col_1)
```

## Output

```
np.newaxis    -> row: (1, 6)  column: (6, 1)
expand_dims   -> row: (1, 6)  column: (6, 1)
Row vector:
 [[1 2 3 4 5 6]]
Column vector:
 [[1]
  [2]
  [3]
  [4]
  [5]
  [6]]
```

## Explanation

Both approaches insert a new axis of length 1. With `np.newaxis` (an alias for `None`), placing it first in the index (`a[np.newaxis, :]`) gives a row vector of shape (1, 6), and placing it second (`a[:, np.newaxis]`) gives a column vector of shape (6, 1). `np.expand_dims(a, axis=0)` and `axis=1` do the same thing. These shapes are useful for broadcasting.