# Accept 5 expences from user and get the average expence.

total=0
for i in range(1,6):
    exp=int(input("Enter Expences : "))
    total+=exp
avg=total/5
print("Average Expences is ",avg)