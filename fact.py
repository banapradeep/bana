a=int(raw_input())
fact=1
if(a<0):
	 print("fact is not exist")
elif(a==0):
	 print("fact of 0 is 1")
else:
             for i in range (1,a+1):
            	fact=fact*i
             print fact
