# Question 9: Finding indices with nonzero and where

## Aim

Find the indices of values satisfying the condition using `np.nonzero`, then again using `np.where`. The expected result is `[1 3 4 5 7]`.

## Code

```python
import numpy as np

arr = np.array([4, 15, 8, 23, 42, 16, 7, 30])

# Expected output [1 3 4 5 7] includes index 1 (value 15), so the condition is >= 15
print("nonzero (>= 15):", np.nonzero(arr >= 15)[0])
print("where   (>= 15):", np.where(arr >= 15)[0])

# For comparison, a strict "> 15" leaves out the 15
print("where   (>  15):", np.where(arr > 15)[0])
```

## Output

```
nonzero (>= 15): [1 3 4 5 7]
where   (>= 15): [1 3 4 5 7]
where   (>  15): [3 4 5 7]
```

## Explanation

Both `np.nonzero(mask)` and `np.where(mask)` (with a single argument) return a tuple of index arrays, one per dimension. For a 1-D array we take `[0]`. They give identical results.

Note: the task says "greater than 15", but the expected output `[1 3 4 5 7]` includes index 1, whose value is exactly 15. So the expected output corresponds to `>= 15`. A strict `> 15` returns `[3 4 5 7]`. Both are shown above.