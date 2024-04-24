import matplotlib.pyplot as plt

def plot_histogram(data, column):
    plt.hist(data[column])
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.title(f'Histogram of {column}')
    plt.show()
