import matplotlib.pyplot as plt
import numpy as np


class BuildHistogram:
    def __init__(self, text, title) -> None:
        self.plot_histogram(text, title)

    def plot_histogram(self, text, title):
        data = [ord(char) for char in text]
        plt.hist(data, bins=np.arange(257), edgecolor='black')
        plt.title(title)
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        plt.xlim(0, 255)
        plt.show()
