# Question 2: zeros, ones and full

## Aim

Create a 3x2 array of zeros, a 2x4 array of ones with integer dtype, and a 2x3 array filled with 7 using `np.full`.

## Code

```python
import numpy as np

zeros = np.zeros((3, 2))
ones = np.ones((2, 4), dtype=int)
sevens = np.full((2, 3), 7)

print("Zeros (3x2):\n", zeros)
print("Ones (2x4, int):\n", ones)
print("Full of 7 (2x3):\n", sevens)
```

## Output

```
Zeros (3x2):
 [[0. 0.]
  [0. 0.]
  [0. 0.]]
Ones (2x4, int):
 [[1 1 1 1]
  [1 1 1 1]]
Full of 7 (2x3):
 [[7 7 7]
  [7 7 7]]
```

## Explanation

- `np.zeros(shape)` and `np.ones(shape)` take the shape as a tuple. By default they produce floats, which is why zeros prints as `0.`.
- Passing `dtype=int` to `np.ones` gives integer ones (`1` instead of `1.`).
- `np.full(shape, fill_value)` fills every cell with the given value. Its dtype is inferred from the fill value, so 7 gives an integer array.