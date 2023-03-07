x=float(input("x="))
y=float(input("y="))
ch=str(input("Phep toan:"))

if ch=="+": 
    print(str(x)+"+"+str(y)+"=",x+y)
elif ch=="-":
    print(str(x)+"-"+str(y)+"=",x-y)
elif  ch=="*":
    print(str(x)+"*"+str(y)+"=",x*y)
elif ch=="/":
    print(str(x)+"/"+str(y)+"=",x/y)
elif x/y and y==0:
    print("Khong hop le",y=0)
else:
    print("Khong hop le")
