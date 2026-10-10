# Question 7: Indexing a 3-D array

## Aim

Given `arr = np.arange(1, 13).reshape(2, 2, 3)`, print 6, then the first row of the second block, then the last element using negative indices.

## Code

```python
import numpy as np

arr = np.arange(1, 13).reshape(2, 2, 3)
print("Array:\n", arr)
print("Element 6          :", arr[0, 1, 2])
print("Second block, row 0:", arr[1, 0])
print("Last element       :", arr[-1, -1, -1])
```

## Output

```
Array:
 [[[ 1  2  3]
  [ 4  5  6]]

 [[ 7  8  9]
  [10 11 12]]]
Element 6          : 6
Second block, row 0: [7 8 9]
Last element       : 12
```

## Explanation

The array has shape (2, 2, 3), meaning 2 blocks, each with 2 rows and 3 columns. The index order is `[block, row, column]`. The value 6 is in block 0, row 1, column 2. `arr[1, 0]` selects block 1 and row 0, which is `[7 8 9]`. `arr[-1, -1, -1]` takes the last block, last row and last column, which is 12.