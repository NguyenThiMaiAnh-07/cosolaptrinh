x=float(input("x="))
y=float(input("y="))
if x+y: 
    print("Phep toan:+\n" + str(x)+ "+" + str(y) + "=",(x+y))
elif x-y:
    print("Phep toan:-\nx-y=",x-y)
elif  x*y:
    print("Phep toan:*\nx*y=",x*y)
elif x/y:
    print("Phep toan:/\nx/y=",x/y)
elif x/y and y==0:
    print("Khong hop le",y=0)
else:
    print("Khong hop le")
    

    
