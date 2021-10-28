from numpy.lib.utils import safe_eval
import matplotlib.pyplot as plt
import random

X = [random.random() for i in range(50)]
Y = [random.random() for i in range(50)]

def top_plot():    
    plt.plot(X, Y)
    plt.savefig(r'static/images/top.png')