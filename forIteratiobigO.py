import time

startTime = time.time()

n = int(input("What is the N value to sum?"))
sum =0

for value in range(1,n+1):
    sum = value + sum

print(f"The sum from 1 to {n} is:{sum}")
endTime = time.time()
print(f"Time execution {endTime-startTime}")
