a=input("Enter any number")
odd=0
even=0
for i in a:
    if int(i)%2==0:
        even+=1
    else:
        odd+=1
print("Number of even digits",even)
print("Number odd digits",odd)