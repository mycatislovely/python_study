import numpy as np
from matplotlib import pyplot as plt
from math import *

def draw_plot(function, left_boundary, right_boundary):

    plt.rcParams["figure.figsize"] = [2.50, 2.20]

    # set axis at zero position
    ax = plt.figure().add_subplot(1, 1, 1)
    ax.spines['left'].set_position(('data', 0.0))
    ax.spines['bottom'].set_position(('data', 0.0))
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    # add a grid
    plt.grid()

    x = np.linspace(left_boundary, right_boundary, num=100)
    plt.plot(x, function(x), color='red') 

    plt.tight_layout(pad=0.50)
    plt.show()
    
    
    
# draw_plot(lambda x: x ** 2 - 3 * x + 10, -10, 10)
# draw_plot(lambda x: x ** 2 + 3 * x - 10, -10, 10)
# draw_plot(lambda x: -(x ** 2) + 4 * x - 4, -10, 10)
# draw_plot(lambda x: -(x ** 3)- 4, -10, 10)
# draw_plot(lambda x: -(0.5 * x )- 4, -10, 10)
# draw_plot(lambda x: 2 ** x, -4, 3)
draw_plot(np.vectorize(lambda x: log(x, 2)), 0.2, 32)












