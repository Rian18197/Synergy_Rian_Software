# Question 19: unique, counts and first index

## Aim

Given the array `a`, print the unique values, how many times each occurs, and the first index of each.

## Code

```python
import numpy as np

a = np.array([11, 11, 12, 13, 14, 15, 16, 17, 12, 13, 11, 14, 18, 19, 20])
values, first_idx, counts = np.unique(a, return_index=True, return_counts=True)

print("Unique values :", values)
print("Counts        :", counts)
print("First indices :", first_idx)
```

## Output

```
Unique values : [11 12 13 14 15 16 17 18 19 20]
Counts        : [3 2 2 2 1 1 1 1 1 1]
First indices : [ 0  2  3  4  5  6  7 12 13 14]
```

## Explanation

`np.unique` returns the sorted unique values. Setting `return_counts=True` also returns how many times each value appears (11 appears 3 times, 12, 13 and 14 appear twice, and the rest once, giving `[3 2 2 2 1 1 1 1 1 1]`). Setting `return_index=True` returns the index of the first occurrence of each value in the original array (for example 11 first appears at index 0 and 12 at index 2).