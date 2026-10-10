# Question 8: Boolean masks for filtering

## Aim

Given `arr = np.array([4, 15, 8, 23, 42, 16, 7, 30])`, print the values greater than 10, the even values, and the values from 10 to 30 inclusive.

## Code

```python
import numpy as np

arr = np.array([4, 15, 8, 23, 42, 16, 7, 30])
print("Greater than 10 :", arr[arr > 10])
print("Even values     :", arr[arr % 2 == 0])
print("Between 10 and 30:", arr[(arr >= 10) & (arr <= 30)])
```

## Output

```
Greater than 10 : [15 23 42 16 30]
Even values     : [ 4  8 42 16 30]
Between 10 and 30: [15 23 16 30]
```

## Explanation

A comparison such as `arr > 10` produces a Boolean array (the mask). Indexing with that mask keeps only the elements where it is `True`. For several conditions, combine masks with `&` (and) or `|` (or), and wrap each condition in parentheses because of operator precedence. Python's `and` / `or` do not work element-wise on arrays.