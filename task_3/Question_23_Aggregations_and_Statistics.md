# Question 23: Aggregations and statistics

## Aim

Create a 3x4 array with `rng.random`. Print its overall sum, mean, min, max, std and prod, then the column sums, the row maxima, and the index of the overall maximum.

## Code

```python
import numpy as np

rng = np.random.default_rng(0)
m = rng.random((3, 4))
print("Array:\n", m)

print("Sum :", m.sum())
print("Mean:", m.mean())
print("Min :", m.min())
print("Max :", m.max())
print("Std :", m.std())
print("Prod:", m.prod())

print("Column sums :", m.sum(axis=0))
print("Row maxima  :", m.max(axis=1))
print("Index of overall max (flat):", m.argmax())
row, col = np.unravel_index(m.argmax(), m.shape)
print("Index of overall max (row, col):", (int(row), int(col)))
```

## Output

```
Array:
 [[0.63696169 0.26978671 0.04097352 0.01652764]
  [0.81327024 0.91275558 0.60663578 0.72949656]
  [0.54362499 0.93507242 0.81585355 0.0027385 ]]
Sum : 6.323697183324092
Mean: 0.5269747652770077
Min : 0.002738500170148095
Max : 0.9350724237877682
Std : 0.33890076332071295
Prod: 4.3416839031917845e-08
Column sums : [1.99385692 2.11761471 1.46346285 0.7487627 ]
Row maxima  : [0.63696169 0.91275558 0.93507242]
Index of overall max (flat): 9
Index of overall max (row, col): (2, 1)
```

## Explanation

Without an `axis` argument, aggregation functions reduce the whole array to one number. With `axis=0` they collapse the rows and give one result per column (column sums). With `axis=1` they collapse the columns and give one result per row (row maxima). `argmax()` returns the position of the maximum in the flattened array, and `np.unravel_index` converts that into (row, column) form. The product is a very small number because it multiplies twelve values that are all less than 1. A seed is used to keep the output reproducible.