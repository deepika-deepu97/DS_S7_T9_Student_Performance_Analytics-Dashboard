import numpy as np
from scipy.spatial import distance
pointA = np.array([2, 4, 6])
pointB = np.array([5, 1, 9])
'''
pointA = np.array([9, 4, 6, 8])
pointB = np.array([8, 3, 9, 7])
'''

# Manhattan distance
minkowski_distance_p3 = distance.minkowski(pointA, pointB,p=1)
print("minkowski_distance(p=3)", minkowski_distance_p3)


# Similarity
similarity_minkowski= 1 / (1 +minkowski_distance_p3)
print("minkowski similarity:", similarity_minkowski)