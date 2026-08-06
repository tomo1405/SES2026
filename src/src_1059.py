import itertools
import seaborn as sns
import matplotlib.pyplot as plt
# Constants
SHAPES = [
    "Circle",
    "Square",
    "Triangle",
    "Rectangle",
    "Pentagon",
    "Hexagon",
    "Heptagon",
    "Octagon",
    "Nonagon",
    "Decagon",
]
COLORS = [
    "Red",
    "Blue",
    "Green",
    "Yellow",
    "Black",
    "White",
    "Purple",
    "Orange",
    "Pink",
    "Brown",
]
def task_func(num_pairs=10):
    max_pairs = len(SHAPES) * len(COLORS)
    num_pairs = min(num_pairs, max_pairs)
    
    pairs = [f"{s}:{c}" for s, c in itertools.product(SHAPES, COLORS)][:num_pairs]
    
    # Drawing the countplot
    ax = sns.countplot(x=pairs, hue=pairs, palette="Set3", legend=False)
    plt.xticks(rotation=90)
    
    return ax