def factorial(a):
    if a == 0 or a ==1:
        return 1
    else:
        return a * factorial(a-1)


val=int(input("Enter a number:"))
if val<0:
    print("Sorry! factorial is not defined for negative numbers.")
else:
    result=factorial(val)
    print('The factorial of', val ,"is", result)