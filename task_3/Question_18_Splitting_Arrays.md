# Question 18: Splitting arrays

## Aim

Given `x = np.arange(1, 25).reshape(2, 12)`, split it into 3 equal parts, split it after the 3rd and 4th columns, and split `np.arange(1, 7)` into 4 parts with `np.array_split`.

## Code

```python
import numpy as np

x = np.arange(1, 25).reshape(2, 12)

print("Split into 3 equal parts (axis=1):")
for part in np.split(x, 3, axis=1):
    print(part, "\n")

print("Split after the 3rd and 4th columns:")
for part in np.split(x, [3, 4], axis=1):
    print(part, "\n")

print("array_split of arange(1,7) into 4 parts:")
print(np.array_split(np.arange(1, 7), 4))
```

## Output

```
Split into 3 equal parts (axis=1):
[[ 1  2  3  4]
 [13 14 15 16]] 

[[ 5  6  7  8]
 [17 18 19 20]] 

[[ 9 10 11 12]
 [21 22 23 24]] 

Split after the 3rd and 4th columns:
[[ 1  2  3]
 [13 14 15]] 

[[ 4]
 [16]] 

[[ 5  6  7  8  9 10 11 12]
 [17 18 19 20 21 22 23 24]] 

array_split of arange(1,7) into 4 parts:
[array([1, 2]), array([3, 4]), array([5]), array([6])]
```

## Explanation

The array has 2 rows and 12 columns, so equal splitting into 3 parts is done along the columns (`axis=1`), giving three 2x4 blocks. `np.split(x, [3, 4], axis=1)` cuts at column indices 3 and 4, producing columns 0-2, column 3, and columns 4-11 (widths 3, 1 and 8). `np.split` raises an error if the parts cannot be equal, but `np.array_split` allows uneven parts. Splitting 6 elements into 4 gives sizes 2, 2, 1, 1, with the earlier parts getting the extra elements.