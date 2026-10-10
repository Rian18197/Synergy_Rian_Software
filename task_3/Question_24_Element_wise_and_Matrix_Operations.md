# Question 24: Element-wise and matrix operations

## Aim

Given `A = [[1,2],[3,4]]` and `B = [[5,6],[7,8]]`, print the element-wise product, the matrix product with `np.matmul`, and the determinant of A with `np.linalg.det`.

## Code

```python
import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("Element-wise product:\n", A * B)
print("Matrix product (matmul):\n", np.matmul(A, B))
print("Determinant of A:", np.linalg.det(A))
```

## Output

```
Element-wise product:
 [[ 5 12]
  [21 32]]
Matrix product (matmul):
 [[19 22]
  [43 50]]
Determinant of A: -2.0000000000000004
```

## Explanation

`A * B` multiplies matching elements. `np.matmul(A, B)` (also written `A @ B`) is true matrix multiplication, where each entry is the dot product of a row of A with a column of B. For example, the top-left entry is 1x5 + 2x7 = 19, which matches the expected `[[19 22] [43 50]]`. `np.linalg.det(A)` computes 1x4 - 2x3 = -2. It is a floating-point calculation, so the printed value may show tiny rounding differences (such as -2.0000000000000004).