# Question 13: flatten vs ravel

## Aim

Given `x = np.array([[1,2,3],[4,5,6]])`, create `f = x.flatten()` and `r = x.ravel()`. Set `f[0] = 100` and `r[1] = 200`, then print `x`.

## Code

```python
import numpy as np

x = np.array([[1, 2, 3], [4, 5, 6]])
f = x.flatten()
r = x.ravel()

f[0] = 100
r[1] = 200

print("x after changes:\n", x)
print("f:", f)
print("r:", r)
```

## Output

```
x after changes:
 [[  1 200   3]
  [  4   5   6]]
f: [100   2   3   4   5   6]
r: [  1 200   3   4   5   6]
```

## Explanation

`flatten()` always returns a copy, so `f[0] = 100` does not affect `x`. `ravel()` returns a view when possible (as here, since `x` is contiguous in memory), so `r[1] = 200` modifies `x[0, 1]`. The printed `x` shows 200 in place of 2, but its first element is still 1.