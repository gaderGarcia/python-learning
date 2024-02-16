import time

startTime = time.time()

n = int(input("What is the N value to sum?"))
sum =0


"""
This one is BigO(n)
because the number of operations executed are
based on the times that it needs to execute the for
The for loop the input is N numbers of executions
due to that is BigO(n)
"""
for value in range(1,n+1):
    sum = value + sum

print(f"The sum from 1 to {n} is:{sum}")
endTime = time.time()
print(f"Time execution {endTime-startTime}")

student_list = ["Edgar","Lizette","Ximena","Jonathan"]
"""
Since this exeuction is only one operation
to fetch the element 0 and nothing else
this is a BigO(1). Even if there are two access, it wil remains as
BigO(1)
"""
print(student_list[0])#BigO(1)
print(student_list[1])#BigO(1)
#The above we don't use BigO(1 + 1) we simply say BigO(1),
# because the access is direct