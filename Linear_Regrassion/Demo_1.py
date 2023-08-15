import numpy as np 
import matplotlib.pyplot as plt

data_x = np.linspace(1.0, 10.0, 100)[:, np.newaxis]
data_y = np.sin(data_x) + 0.1 * np.power(data_x, 2) + 0.5 * np.random.rand(100, 1)
data_x / np.max(data_x)



