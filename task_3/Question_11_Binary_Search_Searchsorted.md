# Question 11: Binary search with searchsorted

## Aim

Given the sorted array `s = np.array([2, 5, 8, 11, 14])`, find where 9 would be inserted, then do the same for `[1, 12, 5]` in one call.

## Code

```python
import numpy as np

s = np.array([2, 5, 8, 11, 14])
print("Insert position of 9        :", np.searchsorted(s, 9))
print("Insert positions of [1,12,5]:", np.searchsorted(s, [1, 12, 5]))
```

## Output

```
Insert position of 9        : 3
Insert positions of [1,12,5]: [0 4 1]
```

## Explanation

`np.searchsorted(sorted_array, values)` uses binary search to return the index where each value can be inserted while keeping the array sorted. 9 lies between 8 and 11, so it goes at index 3. For `[1, 12, 5]`, 1 goes at index 0, 12 at index 4 (between 11 and 14), and 5 at index 1 (before the existing 5, since the default side is `'left'`). The array must already be sorted.