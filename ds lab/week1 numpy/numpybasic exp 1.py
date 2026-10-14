import numpy as np
arr=np.array([13,4,5,16,7,8])
print(arr)
#print(np.sort(arr))
print(arr[-2])
p=np.array([[1,2,3],[4,5,6]])
print(p)
# to print a
print(arr.ndim)
print(p.ndim)
#initializing array with zeros
k=np.zeros([5])
print(k)
l=np.zeros([3,4])
print(l)
#array indexing
print(arr[1])
print(p[1,1])

#negative indexing
print(arr[-1])
print(p[0,-1])

#slicing
print(arr[1:3])


#reshaping 2d array
print(arr.shape) #prints size of array
#print(p[0,2:4])
print(arr.reshape(2,3)) # reshapes 1d array into 2d array

#accessing elements using for loop
for x in arr:
    print(x)

for a in p:
    print(a)

n1=np.array([1,2,3,4])
n2=np.array([5,6,7,8])
n3=np.concatenate((n1,n2))
sp=np.array_split(n3,4)
print(sp[0])
#x=np.array_split(p,)

#sorting
print(np.sort(arr))
#searching

#arthemetic operation

print(np.sum([n1,n2]))
print(np.sum([n1,n2],axis=1))
print(np.sum([n1,n2],axis=0))
print(np.subtract(n1,n2))
print(np.multiply(n1,n2))
print(np.divide(n1,n2))

