a=int(input())

# no even/odd
if a%2==0:
    print("No is Even")
else:
    print("No is odd")

# biggest of three nos

b=int(input())
c=int(input())

if a>b and a>c:
    print("{no} is largest".format(no=a))
elif b>a and b>c:
    print("{0} is largest".format(b))
else:
    print("{no} is largest".format(no=c))