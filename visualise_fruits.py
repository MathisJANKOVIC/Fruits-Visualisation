from matplotlib import pyplot
import numpy
import math

def plot(fruits):
    colors = ["#FF5733", "#33FF57", "#5733FF", "#FF33E6", "#33E6FF"]

    num_cols = math.ceil(math.sqrt(len(fruits)))
    num_rows = math.ceil(len(fruits) / num_cols)

    fig, axs = pyplot.subplots(num_rows, num_cols , figsize=(10, 8))
    if isinstance(axs, pyplot.Axes):
        axs = numpy.array([axs])

    axs = axs.flatten()

    # Find the maximum nutrition value across all fruits
    max_value = max(max(fruit["nutritions"].values()) for fruit in fruits)

    for i, fruit in enumerate(fruits):
        ax = axs[i]
        nutrition_values: dict = fruit["nutritions"]
        keys = list(nutrition_values.keys())
        values = list(nutrition_values.values())
        bars = ax.bar(keys, values, color=colors)
        ax.legend(bars, keys)

        ax.set_title(fruit["name"])

        # Set the same y-axis limits for all subplots
        ax.set_ylim([0, max_value])

    pyplot.tight_layout()
    pyplot.show()
