# SIMPLE CALCULATOR

print("Select your choice:\n","1-ADD \n","2-SUBTRACT \n","3-DIVIDE \n","4-MULTIPLY \n","5-POWER \n","6-None \n")

while True:
    n=int(input("Enter your choice: "))
    if n in (1,2,3,4,5):
        n1=int(input("Enter the first number:"))
        n2=int(input("Enter the second number:"))

        if n==1:
            print(n1,"+",n2,"=",n1+n2)
        elif n==2:
            print(n1,"-",n2,"=",n1-n2)
        elif n==3:
            print(n1,"/",n2,"=",n1/n2)
        elif n==4:
            print(n1,"*",n2,"=",n1*n2)
        elif n==5:
            print(n1,"^",n2,"=",n1**n2)
            break
    else:
        print("THE END \nTHANKYOU")
        break
        
        