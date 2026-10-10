# Question 10: Boolean masks on a 2-D array

## Aim

Given a marks matrix, print the marks that are 60 or above, then count how many students scored 40 or more in each subject (column).

## Code

```python
import numpy as np

marks = np.array([[45, 80, 67],
                  [90, 55, 72],
                  [38, 60, 85]])

print("Marks >= 60:", marks[marks >= 60])
print("Students with >= 40 per subject:", (marks >= 40).sum(axis=0))
```

## Output

```
Marks >= 60: [80 67 90 72 60 85]
Students with >= 40 per subject: [2 3 3]
```

## Explanation

Masking a 2-D array with `marks[marks >= 60]` returns a flattened 1-D array of the matching values. To count, `(marks >= 40)` gives a Boolean matrix. `True` counts as 1 and `False` as 0, so `.sum(axis=0)` adds down each column and counts the passing students per subject. The result `[2 3 3]` means 2 students passed subject 1 (one scored 38) and 3 passed each of the other two.