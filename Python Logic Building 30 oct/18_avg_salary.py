# Accept 5 employees name and salary and count average and total salary.

total=0
for i in range(1,6):
    name=input("Enter Your name :- ")
    salary=int(input("Enter salary : "))
    total+=salary
average=total/5

print("Average salary is ",average)