import numpy as np

# ============/ section - 1 /=============
mylst = [-17,0,4, 5, 9]
my_array_from_list = np.array(mylst)
print(my_array_from_list)
mul = my_array_from_list * 10
# 10 will be mul with every single index of this array
print(mul)

# ===============/ section - 2 /==============

my_tuple = (14, -3.54, 5+7j)
par = np.array(my_tuple)
print(par)
mul2 = my_tuple * 10
print(mul2)