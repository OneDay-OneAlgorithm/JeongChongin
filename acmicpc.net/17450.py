a,b=map(int,input().split())
c,d=map(int,input().split())
e,f=map(int,input().split())
a,b,c,d,e,f=a*10,b*10,c*10,d*10,e*10,f*10
s=b/(a-500 if a>=5000 else a)
n=d/(c-500 if c>=5000 else c)
u=f/(e-500 if e>=5000 else e)
if s==max(s,n,u):print("S")
elif n==max(s,n,u):print("N")
else:print("U")