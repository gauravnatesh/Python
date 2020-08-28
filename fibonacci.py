n1=0
n2=1
l=int(input("Enter the number of terms: "))
if l==1:
    print(n1)
elif l==2:
    print(n1,", ",n2)
else:
    print(n1,',',n2, end = ", ")
    for i in range(3,l+1):
        n=n1+n2
        n1=n2
        n2=n
        print(n, end = ", ")
        i+=1
