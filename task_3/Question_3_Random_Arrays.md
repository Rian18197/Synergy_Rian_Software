# Question 3: Random arrays

## Aim

Create a 3x3 array of random floats and a 2x5 array of random integers from 0 to 9 using a Generator, and a 4x4 array of integers from 1 to 100 using `np.random.randint`.

## Code

```python
import numpy as np

rng = np.random.default_rng(42)          # seeded so the output is reproducible
floats = rng.random((3, 3))              # floats in [0, 1)
ints = rng.integers(0, 10, size=(2, 5))  # 0 to 9 (upper bound is exclusive)

np.random.seed(42)
legacy = np.random.randint(1, 101, size=(4, 4))   # 1 to 100

print("Random floats (3x3):\n", floats)
print("Random ints 0-9 (2x5):\n", ints)
print("randint 1-100 (4x4):\n", legacy)
```

## Output

```
Random floats (3x3):
 [[0.77395605 0.43887844 0.85859792]
  [0.69736803 0.09417735 0.97562235]
  [0.7611397  0.78606431 0.12811363]]
Random ints 0-9 (2x5):
 [[8 4 5 3 1]
  [9 7 6 4 8]]
randint 1-100 (4x4):
 [[ 52  93  15  72]
  [ 61  21  83  87]
  [ 75  75  88 100]
  [ 24   3  22  53]]
```

## Explanation

- `np.random.default_rng()` creates the modern random Generator. `rng.random(shape)` gives floats in the range [0, 1).
- `rng.integers(low, high, size)` gives integers where `high` is exclusive, so `(0, 10)` yields 0 to 9.
- `np.random.randint(1, 101, ...)` is the older global-state API. The upper bound is also exclusive, so 101 is used to include 100.
- A seed (42) is used so the results are repeatable. Without a seed, the numbers change on every run.