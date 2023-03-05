while True:
    n=int(input('n='))
    if n>=1 and n<=50:
        i=1
    while i<=n:
         print(i)
         i=i+1
2,n=int(input("Nhap so nguyen: (n>=1)"))
i=1
S=0
while i<=n:
     S=S+i
     i=i+1
print("Tong S=",S)
i=1
while i<=6:
     j=1
     while j<=i:
         print("*", end="")

         j=j+1
     print("\n")
     i=i+1