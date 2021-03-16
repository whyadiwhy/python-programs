in_put=input()
text=in_put.split()
#print (text)
N=int(text[0])
H=int(text[1])
x=int(text[2])
#print(N,H,x)
time=input()
T=time.split()
b=0
for i in (T):
    a=int(i)
    b=max(b,a)
#print(b,"",x,"",H)
if x+b>=H:
    print("Yes")
else:
    print("No")
