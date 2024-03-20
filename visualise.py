import matplotlib.pyplot as plt

# JSON data
data = [
    {
        "name": "Papaya",
        "nutritions": {
            "calories": 39,
            "fat": 0.3,
            "sugar": 4.4,
            "carbohydrates": 5.8,
            "protein": 0.5
        }
    },
    {
        "name": "Annona",
        "nutritions": {
            "calories": 92,
            "fat": 0.29,
            "sugar": 3.4,
            "carbohydrates": 19.1,
            "protein": 1.5
        }
    }, 
    {
        "name": "Lemon",
        "nutritions": {
            "calories": 29,
            "fat": 0.3,
            "sugar": 2.5,
            "carbohydrates": 9,
            "protein": 1.1
        }
    },
    {
        "name": "Banana",
        "nutritions": {
            "calories": 96,
            "fat": 0.2,
            "sugar": 17.2,
            "carbohydrates": 22,
            "protein": 1
        }
    }
]

# Plotting
def plotting(data):
    colors = ["#FF5733", "#33FF57", "#5733FF", "#FF33E6", "#33E6FF"]
    fig, axs = plt.subplots(2, 2 , figsize=(10, 8))
    axs = axs.flatten()

    # Find the maximum nutrition value across all fruits
    max_value = max(max(fruit["nutritions"].values()) for fruit in data)

    for i, fruit in enumerate(data):
        ax = axs[i]
        nutrition_values = fruit["nutritions"]
        keys = list(nutrition_values.keys())
        values = list(nutrition_values.values())
        bars = ax.bar(keys, values, color=colors)
        ax.legend(bars, keys)
        
        ax.set_title(fruit["name"])
        
        # Set the same y-axis limits for all subplots
        ax.set_ylim([0, max_value])

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    plotting(data)