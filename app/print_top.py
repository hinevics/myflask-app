import matplotlib.pyplot as plt
import random

X = [random.random() for i in range(50)]
Y = [i**2 for i in X]

def top_plot():    
    fig, ax = plt.subplots( nrows=1, ncols=1 )  # create figure & 1 axis
    ax.plot(X, Y)
    fig.savefig(r'\static\images')   # save the figure to file
    plt.close(fig)  

top_plot()