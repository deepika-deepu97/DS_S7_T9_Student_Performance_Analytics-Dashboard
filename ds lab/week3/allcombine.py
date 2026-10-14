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

# Manhattan distance
Manhattan_distance = distance.cityblock(pointA, pointB)
print("Manhattan distance:", Manhattan_distance)

# Similarity
similarity_Manhattan= 1 / (1 +Manhattan_distance )
print("Manhattan similarity:", similarity_Manhattan)

# Manhattan distance
minkowski_distance_p1 = distance.minkowski(pointA, pointB,p=1)
print("minkowski_distance(p=1)", minkowski_distance_p1)


# Similarity
similarity_minkowski= 1 / (1 +minkowski_distance_p1)
print("minkowski similarity:", similarity_minkowski)

# Manhattan distance
minkowski_distance_p2 = distance.minkowski(pointA, pointB,p=2)
print("minkowski_distance(p=2)", minkowski_distance_p2)


# Similarity
similarity_minkowski= 1 / (1 +minkowski_distance_p2)
print("minkowski similarity:", similarity_minkowski)

# Manhattan distance
minkowski_distance_p3 = distance.minkowski(pointA, pointB,p=3)
print("minkowski_distance(p=3)", minkowski_distance_p3)


# Similarity
similarity_minkowski= 1 / (1 +minkowski_distance_p3)
print("minkowski similarity:", similarity_minkowski)