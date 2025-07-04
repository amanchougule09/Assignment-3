import math

num=float(input("Enter a number: "))

if num>0:
    sqrt_val=math.sqrt(num)
else:
    sqrt_val="undefined (Square root only defined for >=0 in real numbers)"

if num>0:
    log_val=math.log(num)
else:
    log_val="undefined (log only defined for positive numbers)"

sin_val=math.sin(num)

print("Square root: ",sqrt_val)
print("Logarithm:",log_val)
print('Sine: ',sin_val)