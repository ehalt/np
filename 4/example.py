import numpy as np
import matplotlib.pyplot as plt

t1 = np.arange(0.0, 2.0, 0.1)
t2 = np.arange(0.0, 2.0, 0.1)

# note: that plot returns a list of lines. The 'L1 = plot" usage
# extracts the first element of the list into l1 using tuple unpacking.
# so, l1 is a line2D instance, not a sequence of lines

l1 = plt.plot(t2, np.exp(-t2))
l2, l3 = plt.plot(t2, np.sin(2 * np.pi * t2), '--go', t1, np.log(1 + t1), '.')
l4, = plt.plot(t2, np.exp(-t2) * np.sin(2 * np.pi * t2), 'rs-.')

plt.legend((l2, l4), ('oscillatory', 'damped'), loc = 'upper right', shadow = True)
plt.xlabel('time')
plt.ylabel('volts')
plt.title('Damped oscillation')
plt.show()