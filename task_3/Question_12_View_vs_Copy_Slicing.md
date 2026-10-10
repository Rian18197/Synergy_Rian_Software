# Question 12: View vs copy with slicing

## Aim

Create `a = np.arange(1, 9)` and `b = a[2:6]`. Set `b[0] = 99` and print `a`. Repeat with `b = a[2:6].copy()`.

## Code

```python
import numpy as np

# Case 1: slice (a view)
a = np.arange(1, 9)
b = a[2:6]
b[0] = 99
print("With view :", a)

# Case 2: explicit copy
a = np.arange(1, 9)
b = a[2:6].copy()
b[0] = 99
print("With copy :", a)
```

## Output

```
With view : [ 1  2 99  4  5  6  7  8]
With copy : [1 2 3 4 5 6 7 8]
```

## Explanation

A basic slice such as `a[2:6]` returns a view that shares memory with the original array. Changing `b[0]` therefore also changes `a[2]` to 99. Calling `.copy()` allocates new memory, so modifying `b` leaves `a` unchanged. Use `.copy()` whenever you need to modify a slice without affecting the source.