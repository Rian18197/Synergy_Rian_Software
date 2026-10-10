# Question 14: Reshaping

## Aim

Reshape `np.arange(1, 13)` into (3, 4), (2, 6), (2, 3, 2) and (4, -1), and print the shape of each.

## Code

```python
import numpy as np

base = np.arange(1, 13)
for shape in [(3, 4), (2, 6), (2, 3, 2), (4, -1)]:
    print(f"reshape{shape} ->", base.reshape(shape).shape)
```

## Output

```
reshape(3, 4) -> (3, 4)
reshape(2, 6) -> (2, 6)
reshape(2, 3, 2) -> (2, 3, 2)
reshape(4, -1) -> (4, 3)
```

## Explanation

`reshape` changes the shape without changing the data, as long as the total number of elements stays the same (12 here: 3x4, 2x6 and 2x3x2 all equal 12). A `-1` tells NumPy to work out that dimension automatically. For `(4, -1)`, it computes 12 / 4 = 3, so the result is (4, 3).