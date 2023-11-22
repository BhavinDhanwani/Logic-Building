# Accept 2 number and swap with temp variable and without temp variable.

# with temp variable.

a=int(input("Enter 1st number : "))
b=int(input("Enter 2nd number : "))

c=a
a=b
b=c

print(a)
print(b)

# without temp variable.

a=int(input("Enter 1st number : "))
b=int(input("Enter 2nd number : "))

a,b=b,a

print(a)
print(b)