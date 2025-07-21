operator=input('enter a operation to perform(+ - * /):')
num1=float(input("enter first number:"))
num2=float(input("enter second number:"))
if operator=="+":
    result=num1+num2
    print(round(result,3))
elif operator=="-":
    result=num1-num2
    print(round(result,3))
elif operator=="*":
    result=num1*num2
    print(round(result,3))
else:
    result=num1/num2
    print(round(result,3))
   