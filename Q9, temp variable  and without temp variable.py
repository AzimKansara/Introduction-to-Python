a= 5
b=10
#with Temp veriable:
temp=a
a=b
b=temp
print("a=",a)
print("b=",b)
#without Temp veriable:
c=5
d=10
c = c + d
d = c - d
c = c - d
print("c",c)
print("d",d)