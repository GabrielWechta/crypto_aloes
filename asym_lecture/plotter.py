from matplotlib import pyplot as plt


def create_scatter_plot(x, y):
    plt.scatter(x, y)
    plt.show()

def create_bar_plot(x, y):
    plt.bar(x, y)
    plt.show()

def create_2_color_bar_plot(x, y1, y2):
    plt.bar(x, y1, color='cyan', alpha=0.5)
    plt.bar(x, y2, color='orange', alpha=0.5)
    plt.show()