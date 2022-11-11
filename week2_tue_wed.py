
#1
# def calc_math_expression(num1, num2, operator):

num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter first number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid operator")




# def calc_math_expression_from_str(str_input):

name = input("Enter your full name: ")
y = name.split()
print(y)



#2
# def find_largest_and_smallest_numbers(num1, num2, num3):

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
def min_num(num1, num2, num3):
    if num1 <= num2 and num1 <= num3:
        return num1
    elif num2 <= num1 and num2 <= num3:
        return num2
    else:
        return num3
print((max_num(6, 2, 1)), min_num(6, 2, 1))




#3
#def quadratic_equation_solver(a, b, c): (Found this solution online, 99% understand)
import math

# function for finding roots
def equationroots(a, b, c):
    # calculating discriminant using formula
    dis = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(dis))

    # checking condition for discriminant
    if dis > 0:
        print(" real and different roots ")
        print((-b + sqrt_val) / (2 * a))
        print((-b - sqrt_val) / (2 * a))

    elif dis == 0:
        print(" real and same roots")
        print(-b / (2 * a))

    # when discriminant is less than 0
    else:
        print("two complex roots")
        print(- b / (2 * a), " + i", sqrt_val)
        print(- b / (2 * a), " - i", sqrt_val)

# a b c
a = 2
b = -9
c = -12.5

# If a is 0, then incorrect equation
if a == 0:
    print("Input correct quadratic equation")

else:
    equationroots(a, b, c)


#def quadratic_equation_solver(a, b, c):
import cmath
print("General Form: -ax**2+bx+c=0")
a = int(input("Enter a (a!=0): "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

d = (b**2)-(4*a*c)
ans1 = (-b-cmath.sqrt(d))/(2*a)
ans2 = (-b+cmath.sqrt(d))/(2*a)

if d>0:
    print("real and different roots")
elif d==0:
    print("real and same roots")
elif d<0:
    print("two complex roots")



#4
#def temp_checker(min_temp, temp_1, temp_2, temp_3)
list1 = [temp_1, temp_2, temp_3]
val = min_temp
if(min(list1)>val):
    print("False")
else:
    print("True")