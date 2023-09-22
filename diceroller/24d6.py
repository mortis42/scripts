import random
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def roll_dice(num_rolls, num_sides):
    rolls = []
    for i in range(num_rolls):
        rolls.append(random.randint(1, num_sides))
    return rolls

def roll_and_combine(num_sets):
    results = []
    for i in range(num_sets):
        # Roll 24d6 and sort the rolls in descending order
        rolls = roll_dice(24, 6)
        rolls.sort(reverse=True)

        # Discard the 4 lowest and 2 highest rolls
        rolls = rolls[4:-2]

        # Combine dice in sets of three from lowest to highest
        sets = []
        for j in range(0, len(rolls), 3):
            sets.append(sorted(rolls[j:j+3]))

        # Sum each set of three dice
        sums = [sum(s) for s in sets]

        results.extend(sums)

    return results

# Generate the data using the roll_and_combine function
data = np.array(roll_and_combine(10000))

# Define the boundaries of the bins
bins = np.arange(3, 19) + 0.5

# Plot the histogram with density
sns.histplot(data, bins=bins, kde=True, stat='density', linewidth=0)

# Set the tick labels to the bin boundaries
plt.xticks(bins)

# Convert y-axis to percentage
plt.gca().yaxis.set_major_formatter(
    plt.FuncFormatter(lambda y, _: f'{y*100:.0%}'))

# Show the plot
plt.show()
