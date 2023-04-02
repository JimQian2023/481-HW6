import matplotlib.pyplot as plt
from sympy import plot_implicit, symbols, Eq, And

x, y = symbols('x y')
p1 = plot_implicit(Eq(x**2 + y**2, 5), backend='matplotlib')
plt.show()
