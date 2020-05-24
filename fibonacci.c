n = int(input("Enter number:"))
a=0
b=1
i=3
print(a)
print(b)
while i<=n:
    a += b
    a,b = b,a
    print(b)
    i+=1
