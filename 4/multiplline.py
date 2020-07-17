import numpy as np
import matplotlib.pyplot as plt

# ===========/ Section - 1 /============

data_set_size = 15
low_mu, low_sigma = 50, 4.3
low_data_set = low_mu + low_sigma * np.random.rand(data_set_size)
high_mu, high_sigma = 57, 5.2
high_data_set = high_mu + high_sigma * np.random.randn(data_set_size)

days = list(range(1, data_set_size + 1))
plt.plot(days,low_data_set,
         days, high_data_set)
plt.show()

# =========/ Section - 2 /==========

plt.plot(days, low_data_set,
         days, low_data_set, "vm",
         days, high_data_set,
         days, high_data_set, "^k")
plt.show()

# ============/section - 3 /===========

plt.plot(days, low_data_set,
         days, high_data_set)
plt.xlabel('Day')
plt.ylabel('Temperature: degrees Farenheit')
plt.title('Randomized temperature data')
plt.show()

# =============/ Section - 4 /============

plt.plot(
    days, high_data_set, "^k")
plt.xlabel('Day')
plt.ylabel('Temperature: degrees Farenheit')
plt.title('Randomized temperature data')
plt.show()