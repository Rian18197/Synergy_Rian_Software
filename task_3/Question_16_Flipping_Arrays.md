# Question 16: Flipping arrays

## Aim

Given a 3x4 array of the numbers 1 to 12, print `np.flip` with no axis, with `axis=0` and with `axis=1`.

## Code

```python
import numpy as np

m = np.arange(1, 13).reshape(3, 4)
print("Original:\n", m)
print("flip (no axis):\n", np.flip(m))
print("flip axis=0 (rows reversed):\n", np.flip(m, axis=0))
print("flip axis=1 (columns reversed):\n", np.flip(m, axis=1))
```

## Output

```
Original:
 [[ 1  2  3  4]
  [ 5  6  7  8]
  [ 9 10 11 12]]
flip (no axis):
 [[12 11 10  9]
  [ 8  7  6  5]
  [ 4  3  2  1]]
flip axis=0 (rows reversed):
 [[ 9 10 11 12]
  [ 5  6  7  8]
  [ 1  2  3  4]]
flip axis=1 (columns reversed):
 [[ 4  3  2  1]
  [ 8  7  6  5]
  [12 11 10  9]]
```

## Explanation

`np.flip` reverses the order of elements along the given axis. With `axis=0`, the rows are reversed (the last row comes first). With `axis=1`, the columns within each row are reversed. With no axis, every axis is flipped, which gives the same result as flipping both axes, so the array is turned upside down and left to right (a 180 degree rotation).