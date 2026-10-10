# Question 6: Strided slices and sub-blocks

## Aim

Using the same array, print every second element of the first row and the 2x3 block from rows 1 to 2 and columns 2 to 4.

## Code

```python
import numpy as np

a = np.arange(1, 36).reshape(5, 7)
print("Every 2nd element of row 0:", a[0, ::2])
print("Block rows 1-2, cols 2-4:\n", a[1:3, 2:5])
```

## Output

```
Every 2nd element of row 0: [1 3 5 7]
Block rows 1-2, cols 2-4:
 [[10 11 12]
  [17 18 19]]
```

## Explanation

The slice syntax is `start:stop:step`, and the stop value is exclusive. `a[0, ::2]` takes the whole first row with a step of 2. For the block, rows 1 to 2 and columns 2 to 4 (inclusive) become `1:3` and `2:5`, which gives a 2x3 sub-array. Basic slices return views of the original array, not copies.