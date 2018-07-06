a=int(raw_input())
print (a)
if(a%4==0 and a%400==0 and a%100!=0):
   print('a is leap year')
else:
   print('a is not leap year')
