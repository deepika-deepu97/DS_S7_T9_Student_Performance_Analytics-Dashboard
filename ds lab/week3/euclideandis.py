import numpy as np
from scipy.spatial import distance

pointA = np.array([2, 4, 6])
pointB = np.array([5, 1, 9])

# Euclidean distance
euclidean_distance = distance.euclidean(pointA, pointB)
print("Euclidean distance:", euclidean_distance)

# Similarity
similarity_euclidean = 1 / (1 + euclidean_distance)
print("Euclidean similarity:", similarity_euclidean)