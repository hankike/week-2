import numpy as np


# update/add code below ...

# Exercise one: Nickels and pennies
def ways(n):
    return n // 5 + 1


ways(12)
ways(20)
ways(3)
ways(0)

# Exercise two: Scores
names = np.array(['Hannah', 'Astrid', 'Abdul', 'Mauve', 'Jung'])
scores = np.array([99, 71, 85, 62, 91])


def lowest_score(names, scores):
    lowest = np.argmin(scores)
    return names[lowest]


lowest_score(names, scores)


def sort_names(names, scores):
    order = np.argsort(scores)[::-1]
    return names[order], scores[order]


sort_names(names, scores)
