# Accept monthly salary from the user and deduct 10% insurance premium, 10% loan installment find out of remaining salary.

s=int(input("Enter Salary : "))

i=s*0.10
l=s*0.10
t=s-i-l

print("Salary after diduction : ",t)