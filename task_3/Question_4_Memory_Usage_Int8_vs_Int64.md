# Question 4: Memory usage of int8 vs int64

## Aim

Create the numbers 0 to 9 as `int8` and as `int64`, and compare their `nbytes`.

## Code

```python
import numpy as np

a8 = np.arange(10, dtype=np.int8)
a64 = np.arange(10, dtype=np.int64)

print("int8  array:", a8,  "-> nbytes =", a8.nbytes)
print("int64 array:", a64, "-> nbytes =", a64.nbytes)
```

## Output

```
int8  array: [0 1 2 3 4 5 6 7 8 9] -> nbytes = 10
int64 array: [0 1 2 3 4 5 6 7 8 9] -> nbytes = 80
```

## Explanation

`nbytes` equals `size * itemsize`. An `int8` uses 1 byte per element (10 x 1 = 10 bytes), while `int64` uses 8 bytes per element (10 x 8 = 80 bytes). Both arrays hold the same values, but the smaller dtype uses 8 times less memory. This matters for large datasets, as long as the values fit in the smaller range (int8 holds -128 to 127).