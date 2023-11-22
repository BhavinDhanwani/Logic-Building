# Calculate compound interest.

# a=p(1+r/n)nt

p=int(input("Enter P : "))
r=int(input("Enter R : "))
# n=int(input("Enter number of times interest applied per time period : "))
t=int(input("Enter T : "))

a=p*(1+(r/100))*t
ci=a-p

# print(a)
print("Compound Interest is : ",ci)