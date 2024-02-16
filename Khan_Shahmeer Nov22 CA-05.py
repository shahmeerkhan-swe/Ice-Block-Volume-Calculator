#Khan_Shahmeer Nov22 CA-05


def odds():
    user_prompt = input("Do you want to run the function odds? (Y/N): ")
    user_prompt = user_prompt.upper()

    while user_prompt == 'Y':
        iterations = int(input("Enter the number of iterations: "))

        for x in range(iterations):
            print("\nThis is run", x + 1)
            num = int(input("Enter a positive odd number between 1 to 13: "))
            isOdd = 1

            if num % 2 == 0:  # Modulus operation to validate 'num' as an odd number
                num = int(input("This number is even, please enter an odd number: "))
                isOdd = 0

            while isOdd == 1:
                if 1 <= num <= 13:
                    print(num, "is odd and prime")
                    isOdd = 0
                else:
                    print(num, "is odd but invalid")
                    isOdd = 0  # Loop that checks if num is in range and prints the appropriate response

        user_prompt = input("\nRun the program again? (Y/N): ")
        user_prompt = user_prompt.upper()

        if user_prompt == "N":
            return


def cryo_Input():
    freeboard = int(input("\nPlease enter the freeboard: "))
    length = int(input("Please enter the length: "))
    breadth = int(input("Please enter the breadth: "))

    return freeboard, length, breadth


def cryo_Process(freeboard, length, breadth):
    ice_thickness = freeboard + (freeboard * 8) # Free board is 1/9th of the total ice thickness
    floe_volume = ice_thickness * (length * breadth)

    return floe_volume


def cryo_Out(floe_volume):
    print("The volume for the ice floe is:", floe_volume)
    return 0


def main():

    odds()
    freeboard, length, breadth = cryo_Input()
    proc = cryo_Process(freeboard, length, breadth)
    print()
    cryo_Out(proc)


main()
