def multiply(num1,*args):
    for num in args:
        num1=num1*num
    return num1
print(multiply(1,2,3,4,5,6))