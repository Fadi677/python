#1.Biggie Size
def biggie(list):
    for i in range(0,len(list)):
        if(list[i]>0):
            list[i]="big"
    return(list)
f=biggie([-1,3,5,-5])
print(f)

#2.Count Positives
def countp(list):
    count=0
    for i in range(len(list)-1,-1,-1):
        if(list[i]>0):
            count=count+1
            list[len(list)-1]=count
    return(list)
f=countp([-1,3,5,-5,1])
print(f)

#3.Sum Total
def sumlist(list):
    sum=0
    for i in range(0,len(list)):
        sum=sum+list[i]
    return sum
f=sumlist([-1,3,5,-5,1])
print(f)

#4.Average
def avg(list):
    sum=0
    avg=0
    for i in range(0,len(list)):
        sum=sum+list[i]
    avg=sum/len(list)
    return avg
f=avg([1,2,3,4])
print(f)

#5.Length
def length(list):
    return len(list)
f=length([])
print(f)

#6.Minimum
def minimum(list):
    if len(list)>0:
        min=list[0]
        for i in range(0,len(list)):
            if list[i]<min:
                min=list[i]
    else:
        return False
    return min
f=minimum([2,3,6,8,30,-20])
print(f)

#7.Maximum
def maximum(list):
    if len(list)>0:
        max=list[0]
        for i in range(0,len(list)):
            if list[i]>max:
                max=list[i]
    else:
        return False
    return max
f=maximum([2,3,6,8,30,-20])
print(f)

#8.Ultimate Analysis
def ultimate(list):
    sum=0
    avg=0
    min=list[0]
    max=list[0]
    for i in range(0,len(list)):
        sum=sum+list[i]
        avg=sum/len(list)
        if list[i]<min:
            min=list[i]
        if list[i]>max:
            max=list[i]
    dictionary={'sumTotal':sum,'average':avg,'minimum':min,'maximum':max}
    return dictionary
f=ultimate([2,3,4,5,6,7,8])
print(f)

#9.Reverse List
def reverseme(list):
    i=0
    j=len(list)-1
    while(i<j):
        list[i],list[j]=list[j],list[i]
        i+=1
        j-=1
    return list
f=reverseme([37,2,1,-9])
print(f)