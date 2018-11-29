import matplotlib.pyplot as plt
import numpy as np


# 绘制简单的曲线
# plt.plot([1, 2, 3, 5], [4, 3, 8, 10])
# plt.show()

x = np.linspace(-np.pi, np.pi, 100)
plt.plot(x, np.sin(x))
plt.show()
