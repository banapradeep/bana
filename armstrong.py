a=int(raw_input())
r=list(map(int,str(a)))
b=list(map(lambda x:x**3,r))
c=sum(b)
if(c==a):
    print("yes")
else:
    print("no")
