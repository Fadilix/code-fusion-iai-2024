str_grid = """7 53 183 439 863
497 383 563 79 973
287 63 343 169 583
627 343 773 959 943
767 473 103 699 303"""

grid = [[int(num) for num in row.split(" ")] for row in str_grid.split("\n")]

import numpy as np

matrix = np.array(grid)

print(matrix)

max = matrix.max()
print(max)

print(np.where(matrix==max))

# product = 1
# for r in range(len(grid)):
#     for c in range(len(grid)):
#         if r != c:
