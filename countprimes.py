a=int(input())
b=int(input())
z=0
while True:
    a=a+1
    if a%2==0:
        d=0
    elif a>=b:
        break
    else:
        z+=1
print(z)
