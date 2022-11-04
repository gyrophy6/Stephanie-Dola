import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 100, 10)  # Создаем массив из ста точек на промежутке (-1; 1)
y = np.sin(x)*(x**(-2))
plt.plot(x,y)
plt.grid()
plt.show()

x = np.linspace(10,100,100)
y = np.exp(-x*np.sin(x))
plt.plot(x,y)
plt.minorticks_on()
plt.show()

x = np.linspace(10,100,1000)
y = np.exp(np.sin(x)*x)
plt.plot(x,y)
plt.minorticks_on()
plt.show()


