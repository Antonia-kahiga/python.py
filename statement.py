#If statement
x=1
marks=77
grades=91.67
if x>0:
    print("The number is positive")
    print(7+10)

#If.. else statement
if marks>=60:
    print("You have passed")
else:
    print("You have failed")

#if..else if.. else statement
if grades<=29 and grades>=0:
    print("You have failed")
elif grades<=49 and grades>=30:
    print("You have passed ")
elif grades<=79 and grades>=50:
    print("You have credit")
elif grades<=100 and grades>=80:
    print("You have distinction")
else:
    print("Wrong input")

#self practice
cluster=int(input("Enter your cluster weight:"))
if cluster<=36 and cluster>34:
    print("You Qualify for 'Interior Design'")
elif cluster<=40 and cluster>=37:
    print("You qualify for 'Electical engineerin")
elif cluster<=42 and cluster>=41:
    print("You qualify for 'Civil Engineering'")
elif cluster<=45 and cluster>=43:
    print("You qualify for 'Architecture'")
else:
    print("You do not qualify for 'cluster 6'")

grade=float(input("Enter your grade :"))
if grade>=75:
    print("You scored an 'A' Congratulations")
elif grade>=65:
    print("You scored a 'B'")
elif grade>=50:
    print("You scored a 'C'")
elif grade>=30:
    print("You scored a 'D'")
elif grade>=10:
    print("You scored an 'E'")
else:
    print("Retake!")