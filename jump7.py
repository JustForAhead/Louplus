n=0
while n<100:
    n+=1
    if n%7==0 or n%10==7 or n//10==7:
        continue
    print(n)
