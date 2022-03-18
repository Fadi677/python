#Basic
for x in range(151):
    print(x)

#Multiples of Five
for x in range(5,1001,5):
    print(x)

#Counting, the Dojo Way
for x in range(1,100):
    if x%10==0:
        print("Coding Dojo")
    elif x%5==0:
        print("Coding")
    else: print(x)
#That Sucker's Huge
sum=0
for x in range (1,500000,2):
    sum+=x
print(sum)

    #another method-
sum=0
for x in range (1,500000):
    if x%2==0:
        continue
    elif x%2!=0:
        sum+=x
print(sum)

#Countdown by Fours
for x in range(2018,0,-4):
    print(x)

#Flexible Counter
lownum=2
highnum=9
mult=3
for x in range(lownum,highnum+1):
    if x%mult==0:
        print(x)