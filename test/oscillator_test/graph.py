#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

x = np.load("out.npy")
plt.plot(x)
plt.show()
