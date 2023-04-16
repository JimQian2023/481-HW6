# import matplotlib.pyplot as plt
# from sympy import plot_implicit, symbols, Eq, And

# x, y = symbols('x y')
# p1 = plot_implicit(Eq(x**2 + y**2, 5), backend='matplotlib')
# plt.show()

import matplotlib.pyplot as plt
from sympy import plot_implicit, symbols, Eq, And

from sympy import plot
from sympy.plotting.plot import Plot
from sympy import Symbol

x, y = symbols('x y')

p = Plot(x**2, title='Squared Plot', label='foo', legend=True, show=True)
p.show()