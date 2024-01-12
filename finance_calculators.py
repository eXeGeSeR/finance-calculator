import math

# Ask the user about the type of calculation. Make it case insensitive!
type_calculation = input('''What type of calculation would you like?\n
                        1. Would you like an investment -to calculate the amount 
                        of the interest you will earn on your investment?\n
                        2. Would you like a home loan bond -to calculate the amount 
                        you'll have to pay on a home loan?\n
                        Enter either "investment" or "bond" from the menu above to proceed \n''').casefold()

# Creating an if-elif-else structure based on user's answer
# Investment -calculation of the total of money accumulated with the interest
if type_calculation == "investment": 
    # Initialize the total of money before any interest 
    total_amount = 0

    # Ask the user the amount of money available to invest, the interest rate, the number of years and the type of interest
    invested_money = int(input("What is the amount of money do you like to invest?\n"))
    interest_rate = float(input("What interest rate are you interested on? Please type only digits, no need for % symbol!\n"))
    years = int(input("How many years would you like to invest in?\n"))
    interest_type = str(input("What kind of interest rate do you prefer: simple or compound?\n")).casefold()

    # Create an if-elif-else structure basen on type of interest rate
    # Calculate the simple interest rate and print it out
    if interest_type == "simple":
        total_amount = invested_money * (1 + ((interest_rate/100) * years))
        print(f"The money earned are £{total_amount} for {years} years with an amount of £{invested_money} at a simple interest rate of {interest_rate}%.")
    
    # Calculate the compound interest rate and print it out 
    elif interest_type == "compound":
        total_amount = invested_money * math.pow((1 + (interest_rate/100)), years)
        print(f"The money earned are £{total_amount} for {years} years with an amount of £{invested_money} at a compound interest rate of {interest_rate}%.")
    
    else: 
        # Error message displays if the user doesn't type any of the interest rate
        print("Error: You didn't type either simple or compound interest rate.")

elif type_calculation == "bond":
    # Bond -calculation of the monthly house repayment
    # Initialize the repayment plan 
    repayment = 0
    # Ask the user to type the present value of the house, the interest rate and the number of the months
    house_price = int(input("What is the present value of the house?\n"))
    interest_rate = float(input("What is the interest rate? Please type only digits, no need for the % symbol!\n"))
    months = int(input("How many months would you like to make the repayment?\n"))

    # Calculate the monthly repayment of the house and print it out
    repayment = ((interest_rate/100/12) * house_price)/(1 - (1 + (interest_rate/100/12))**(-months))
    print(f"The monthly repayment of the house is £{repayment}.")

else: 
    # Print out an error message as result of not typing investment or bond
    print("Error: You didn't type either investment or bond. Try again!")
