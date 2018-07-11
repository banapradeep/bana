#include<stdio.h>
int main()
{
    char s[100],d;
    int i,n,p;
    gets(s);
    p=strlen(s);
for(i=0;i<p;i=i+2)
{
    if(i<p-1)
    {
    if(i%2==0)
    {
        d=s[i];
        s[i]=s[i+1];
        s[i+1]=d;
    }
}
}
puts(s);
}
