# Question 17: Stacking and concatenating

## Aim

Given `a1 = [[1,1],[2,2]]` and `a2 = [[3,3],[4,4]]`, produce the `vstack` result, the `hstack` result, and `np.concatenate` along `axis=1`.

## Code

```python
import numpy as np

a1 = np.array([[1, 1], [2, 2]])
a2 = np.array([[3, 3], [4, 4]])

print("vstack:\n", np.vstack((a1, a2)))
print("hstack:\n", np.hstack((a1, a2)))
print("concatenate axis=1:\n", np.concatenate((a1, a2), axis=1))
```

## Output

```
vstack:
 [[1 1]
  [2 2]
  [3 3]
  [4 4]]
hstack:
 [[1 1 3 3]
  [2 2 4 4]]
concatenate axis=1:
 [[1 1 3 3]
  [2 2 4 4]]
```

## Explanation

`np.vstack` stacks arrays vertically (one below the other), giving shape (4, 2). `np.hstack` places them side by side, giving shape (2, 4). `np.concatenate(..., axis=1)` joins along columns, so it gives the same result as `hstack` for 2-D arrays. `concatenate` is the general function, and `vstack` / `hstack` are convenient shortcuts for axes 0 and 1.