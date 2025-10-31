import numpy as np
import matplotlib.pyplot as plt

def main():
    x = np.arange(0, 2 * np.pi,  0.0062831853)
    y = np.sin(x)
    plt.plot(x, y)