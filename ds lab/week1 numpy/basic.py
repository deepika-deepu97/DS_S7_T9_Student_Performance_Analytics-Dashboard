print("hello")
a=10
print(a)
#string printing
b="chetna"
print(b)

d="python programming"
print(d)

#to declare variables
x,y,z="hello","hi","welcome"
print(x,y,z)
#using saperator
e=f=g="e f g samevariables"
print(e,f,g,sep=" , ")

#multi line comments
""""e=f=g="e f g samevariables"
print(e,f,g,sep=" , ")"""

#integer input
c=int(input())
if c>5:
    print("Yes")
else:
    print("No")

#to find datatype
h=1
i=2.3
j=True

print(type(h))
print(type(i))
print (type(j))

#type casting

k=int(1)
l=int(2.5)
m=float(3)
n=str(123)

print(k,l,m,n)

o=float(1)
p=float(2.8)
r=float("3")
s=float("4.2")

print(o,p,r,s)

#slicing strings 

name="Batta Chetna Chowdary"
print(name[0:5]) # last letter not included