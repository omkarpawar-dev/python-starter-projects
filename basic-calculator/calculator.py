while True:
    num1=int(input("Enter number 1:"))
    num2=int(input("Enter number 2: "))
    op=input("Type X to Exit or Enter the operation you want to perform: ")

    if op.lower()=="x":
        break
    elif op=="+":
        print("The sum is: ", num1+num2)
    elif op=="-":
        print("The difference is: ", num1-num2)
    elif op=="*":
        print("The product is: ",num1*num2)
    elif op=="/":
        if num2==0:
            print("Error: Division by Zero is not allowed")
        else:
            print("The quotient is: ",num1/num2)
    elif op=="%":
        if num2==0:
            print("Error: Division by Zero is not allowed")
        else:
             print("The remainder is ",num1%num2)
