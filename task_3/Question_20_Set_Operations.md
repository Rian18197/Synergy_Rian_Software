# Question 20: Set operations

## Aim

Given `a = [1,2,3,4,5]` and `b = [4,5,6,7]`, compute the union, intersection, difference (a minus b) and symmetric difference.

## Code

```python
import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array([4, 5, 6, 7])

print("Union               :", np.union1d(a, b))
print("Intersection        :", np.intersect1d(a, b))
print("Difference (a - b)  :", np.setdiff1d(a, b))
print("Symmetric difference:", np.setxor1d(a, b))
```

## Output

```
Union               : [1 2 3 4 5 6 7]
Intersection        : [4 5]
Difference (a - b)  : [1 2 3]
Symmetric difference: [1 2 3 6 7]
```

## Explanation

NumPy provides set routines that return sorted, unique results: `union1d` (all values in either array), `intersect1d` (values in both), `setdiff1d(a, b)` (values in `a` but not in `b`), and `setxor1d` (values in exactly one of the arrays). The results match the expected outputs: [1..7], [4 5], [1 2 3] and [1 2 3 6 7].