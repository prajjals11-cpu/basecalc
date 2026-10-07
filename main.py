#############################################################BASIC CALCULATOR######################################################################

#Turns the calculator on and off
on = True 

#Operation Functions
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

#Calculator Running State
while on == True:
    print("                                                                                        7")
    print("========================================================================================") #Basic Interface
    print("                      Welcome to the Base(ic) Calculator!!                              ")
    print("========================================================================================")
    print("                 By: ps_CPU (GitHub https://github.com/prajjals11-cpu                   ")
    print("                                                                                        ")
    print("                                                                                        ")
    print("                                                                                        ")
    print("Mode Selection:")
    print("------------------")
    print("[1] Addition")
    print("[2] Subtraction")
    print("[3] Multiplication")
    print("[4] Division")
    print("[5] Exponents")
    print("[6] Roots")
    print("[7] Shutdown")

#Operation Input
    print("Please select one of the options above")
    mode_selection = int(input("Operation? "))

#First Input
    num_1 = float(input("Enter your first number : "))
    print("-------------------------------------------")

#Second Input
    num_2 = float(input("Enter your second number: "))
    print("-------------------------------------------")

#Mode Descision
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
    elif mode_selection == 5:
        print(exponent())
        print("-------------------------------------------------------------------------------------")
    elif mode_selection == 6:
        print(root())
        print("-------------------------------------------------------------------------------------")
    elif mode_selection == 7:
        on = 0








