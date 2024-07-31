import matplotlib.pyplot as plt

from data.data import air_quality

print(air_quality.head())

air_quality.plot()
plt.show()
