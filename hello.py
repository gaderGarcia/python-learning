#This is a comment of our first code in python
name = input("What's your name? ")
#remove white space
#name = name.strip().title()
#The key in python is a function like in C where you can
#pass different elements to execute in this case
#print is a function which print the N elements passed in the function
print("Hello",name,sep='*')
print("Again ",end='')
print(name)
print("Concatenate String: "+name)
print('Using "Simple quotes and double"')
#Another way to print is using format the string
#This is happening using the letter f
print(f"With Format, {name}")

buffer=[0]*30
print("The buffer content: ",buffer)
for i in range(len(name)):
    
    inx=ord(name[i])-ord('a')
    buffer[inx]+=1
    print(inx,end=' ')

print(f"how many letters e we have {buffer[ord('e')-ord('a')]}")
s1=''

for c in name:
    s1=c+s1

print(s1)
