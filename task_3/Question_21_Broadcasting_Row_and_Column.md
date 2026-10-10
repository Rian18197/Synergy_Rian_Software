# Question 21: Broadcasting a row and a column

## Aim

Given `m = np.arange(1, 10).reshape(3, 3)`, add the row `[10, 20, 30]` to every row, then add the column `[[100], [200], [300]]` to every column.

## Code

```python
import numpy as np

m = np.arange(1, 10).reshape(3, 3)
row = np.array([10, 20, 30])
col = np.array([[100], [200], [300]])

print("m:\n", m)
print("m + row:\n", m + row)
print("m + col:\n", m + col)
```

## Output

```
m:
 [[1 2 3]
  [4 5 6]
  [7 8 9]]
m + row:
 [[11 22 33]
  [14 25 36]
  [17 28 39]]
m + col:
 [[101 102 103]
  [204 205 206]
  [307 308 309]]
```

## Explanation

Broadcasting lets arrays of different shapes work together without copying data. The row has shape (3,), which is treated as (1, 3) and stretched down the 3 rows of `m`. The column has shape (3, 1) and is stretched across the 3 columns, so each row of `m` gets its own constant (100, 200 or 300) added to all its elements.