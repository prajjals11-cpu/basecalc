# Basic Calculator 
#Turns the calculator on and off
on = True 

while on == True:
    print("----------------------------------------------------------------------------------------")
    print("Welcome to the Base(ic) Calculator!!"                                                    )
    print("By: ps_CPU (GitHub https://github.com/prajjals11-cpu"                                    )
    print(IN PROGRESS                                                                               )
    print("----------------------------------------------------------------------------------------")
    num_1 = float(input("Enter your first number : "))
    print("----------------------------------------------------------------------------------------")
    num_2 = float(input("Enter your second number: "))
    print("----------------------------------------------------------------------------------------")
    mode_selection = int(input("Operation? "))
    print("----------------------------------------------------------------------------------------")
    print("Mode Selection:")
    print("------------------")
    print("[1] Addition")
    print("[2] Subtraction")
    print("[3] Multiplication")
    print("[4] Division")
    print("[5] Exponents")
    print("[6] Roots")
    print("[7] Shutdown")
    if mode_selection == 1:
            print(sum())
            print("-------------------------------------------------------------------------------------")
        elif mode_selection == 2:
            print(difference())
            print("-------------------------------------------------------------------------------------")
        elif mode_selection == 3:
            print(product())
            print("-------------------------------------------------------------------------------------")
        elif mode_selection == 4:
            print(quotient())
            print("-------------------------------------------------------------------------------------")

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








