# Question 22: Broadcasting rules and errors

## Aim

Try the additions (4,3)+(3,), (4,3)+(4,), (4,3)+(4,1) and (2,3,4)+(3,1) using `np.ones` arrays, and print either the result shape or the error message.

## Code

```python
import numpy as np

cases = [((4, 3), (3,)),
         ((4, 3), (4,)),
         ((4, 3), (4, 1)),
         ((2, 3, 4), (3, 1))]

for s1, s2 in cases:
    try:
        result = np.ones(s1) + np.ones(s2)
        print(f"{s1} + {s2} -> OK, result shape {result.shape}")
    except ValueError as e:
        print(f"{s1} + {s2} -> ERROR: {e}")
```

## Output

```
(4, 3) + (3,) -> OK, result shape (4, 3)
(4, 3) + (4,) -> ERROR: operands could not be broadcast together with shapes (4,3) (4,) 
(4, 3) + (4, 1) -> OK, result shape (4, 3)
(2, 3, 4) + (3, 1) -> OK, result shape (2, 3, 4)
```

## Explanation

NumPy compares shapes from the rightmost axis. Two dimensions are compatible if they are equal or one of them is 1. Missing leading dimensions are treated as 1.
- (4,3)+(3,): works, since the trailing 3 matches and the result is (4,3).
- (4,3)+(4,): fails, because the trailing dimensions 3 and 4 differ and neither is 1.
- (4,3)+(4,1): works, since the 1 stretches to 3 and the result is (4,3).
- (2,3,4)+(3,1): works, since (3,1) acts like (1,3,1), giving (2,3,4).
The `try/except` block catches the `ValueError` and prints its message instead of crashing.