import numpy as np

a = np.arange(6).reshape(2, 3)
print(a)
# [[0 1 2]
#  [3 4 5]]

print(np.expand_dims(a, 0))
# [[[0 1 2]
#   [3 4 5]]]

print(np.expand_dims(a, 0).shape)
# (1, 2, 3)