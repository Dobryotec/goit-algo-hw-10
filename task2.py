import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x ** 2

a = 0 
b = 2  


x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()


ax.plot(x, y, 'r', linewidth=2)

ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)


ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')


ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()

def monte_carlo_integration(func, a, b, num_samples):
    samples_x = np.random.uniform(a, b, num_samples)
    samples_y = func(samples_x)
    integral = (b - a) * np.mean(samples_y)
    return integral

num_samples = 100000
mc_integral = monte_carlo_integration(f, a, b, num_samples)
print("Інтеграл методом Монте-Карло: ", mc_integral)

result, error = spi.quad(f, a, b)
print("Інтеграл за допомогою функції quad: ", result)

difference = abs(mc_integral - result)
print(f"Різниця між результатами: {difference}")