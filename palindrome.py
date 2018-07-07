a=int(raw_input())
sum1=0
n=a
 
while a!=0:
	rem=a%10
	sum1=sum1*10+rem
	a=a/10
if sum1==n:
	print n, "is palindrome"
else:
	print n, "is not palindrome"
