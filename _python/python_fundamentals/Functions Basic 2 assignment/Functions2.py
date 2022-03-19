#1.Countdown
def countdown(x):
    arr=[]
    for x in range (x,-1,-1):
        arr.append(x)
    print(arr)
f=countdown(5)

#2.Print and Return
def printandreturn(i,j):
    print(i)
    return j
f=printandreturn(1,2)
print(f)

#3.First Plus Length
def firstlen(list):
    sum=list[0]+len(list)
    print(sum)
    return sum
list=[1,2,3,4,5]
f=firstlen(list)

#4.Values Greater than Second
def greaterthan(list):
    maxlist=[]
    if(len(list)<2):
        return False
    max=list[1]
    for x in range(0,len(list)):
        if(list[x]>max):
            maxlist.append(list[x])
    return maxlist
s=greaterthan([1,2,3,4,5,2])
print(s)

#5.This Length, That Value
def lengthvalue(s,v):
    list=[]
    for x in range(0,s):
        list.append(v)
    return list
z=lengthvalue(3,9)
print(z)

