# Basic Calculator 
on = True 

while on == True:
    print("----------------------------------------------------------------------------------------")
    print("Welcome to the Base(ic) Calculator!!")
    print("By: ps_CPU (GitHub https://github.com/prajjals11-cpu")
    print(IN PROGRESS)
    print("----------------------------------------------------------------------------------------")
    num_1 = float(input("Enter your first number : "))
    print("----------------------------------------------------------------------------------------")
    num_2 = float(input("Enter your second number: "))
    print("----------------------------------------------------------------------------------------")
    mode_selection = int(input("Operation? "))
    print("----------------------------------------------------------------------------------------")

def sum():
    ans = num_1 + num_2
    return(ans)

def difference():
    ans = num_1 - num_2
    return(ans)

def product():
    ans = num_1 * num_2
    return(ans)

def quotient():
    ans = num_1 / num_2
    return(ans)

def exponent():
    ans = num_1 ** num_2
    return(ans)

def root():
    ans = num_1 ** (1/num_2)
    return(ans)

num_1 = float(input("Enter your first number : "))
num_2 = float(input("Enter your second number: "))
mode_selection = int(input("Operation? "))






