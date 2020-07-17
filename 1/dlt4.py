import numpy as np

# linspace(), zeros(), ones(), and numpy data types

lsp = np.linspace(5, 15, 19)
print(lsp)

lsp2 = np.linspace(5, 15, 9, retstep=True)
print(lsp2)

# zeros()

zero1 = np.zeros(5)
print(zero1)

zero2 = np.zeros((5, 4))
print(zero2)

zero3 = np.zeros((5, 4, 4))
print(zero3)

# ones
ones = np.ones(7)
print(ones)
