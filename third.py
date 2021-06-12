a=int(input("Enter a number"))
i=1
s=0
while i<a:
    if a%i==0:
        s+=i
        print(i)
    i+=1
if s==a:
    print(a, "is a perfect number")
else:
    print(a, "is not a perfect number")