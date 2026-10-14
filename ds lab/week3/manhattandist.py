import numpy as np
from scipy.spatial import distance

pointA = np.array([9, 4, 6, 8])
pointB = np.array([8, 3, 9, 7])

# Manhattan distance
Manhattan_distance = distance.cityblock(pointA, pointB)
print("Manhattan distance:", Manhattan_distance)

# Similarity
similarity_Manhattan= 1 / (1 +Manhattan_distance )
print("Manhattan similarity:", similarity_Manhattan)