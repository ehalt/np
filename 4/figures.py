import numpy as np
import matplotlib.pyplot as plt

my_first_figure = plt.figure("My first figure!")
subplot_1 = my_first_figure.add_subplot(2,3, 1)
subplot_6 = my_first_figure.add_subplot(2,3, 6)
plt.plot(np.random.rand(50).cumsum(), 'k--')
plt.show()

subplot_2 = my_first_figure.add_subplot(2, 3, 2)
plt.plot(np.random.rand(50),'go')
plt.show()


