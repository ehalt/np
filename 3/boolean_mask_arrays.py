import numpy as np

my_vector = np.array([-17, 4, 0, 2, 21, 37, 105])
print(my_vector)

zero_mod_7_mask = 0 == (my_vector % 7)
print(zero_mod_7_mask)

sub_array = my_vector[zero_mod_7_mask]
print(sub_array)

ind1 = sub_array[sub_array > 0]
print(ind1)


