#Project1-Variables and Control Structures

#Interest occurs in almost all financial
#Simple interest: the amount added on the initial invested amount (principal amount)
#Compound interest: is calculated on the current total known as accumulated amount

#Aim: Create a program that allows the user to access 2 different financial calculators:
# 1) An investment calculator
# 2) A home loan repayment calculator

import math

#User choice of which type of calculation they want
print("investment - to calculate the amount of interest you'll earn on your investment" +"\n"
      "bond       - to calculate the amount you'll have to pay on a home loan")

calculator_type = input("Enter either 'investment' or 'bond' from the menu above to proceed:").strip().lower()

#If branches for investment: add the amount of money,
#interest rate, number of years planned to invest
if calculator_type == "investment":
    amount = float(input("Enter the amount of money that you are depositing (£): "))
    years = int(input("Enter the number of years planned on investing: ") )
    rate = float(input("Enter the interest rate you are choosing in %: "))
  
    #Ask user if they want a simple or compund interest type investment
    interest = input("Enter either 'simple' or 'compound' for the interst type:").strip().lower()
    
    if interest == "simple":
        # A = P*(1+r*t)
        r = rate/100
        amount_returned= amount * (1+r*years)
        print(f"Your total expected amount from simple type is {amount_returned}")
    elif interest == "compound":
        # A = P*(1+r*t)
        r = rate/100
        amount_returned= amount * math.pow((1+r),years)
        print(f"Your total expected amount from compound type is {amount_returned}")

elif calculator_type == "bond":
        #Present value of the house
        house_value = float(input("Enter the present value of the house (£):"))
        #Interest rate
        interest_rate = float(input("Enter the interest rate in %: "))
        #number of moths they plan to take to repay the bond
        n_repay = int(input("Enter the number of months you plan to take to repay the bond: "))
        
        #calculate the monthly interest rate:
        monthly_int_rate = (interest_rate / 100) / 12

        #Amount a person will have to repaid on a home loan each month
        repayment = (monthly_int_rate * house_value) / (1-math.pow((1 + monthly_int_rate),(-n_repay)))
        print(f"The money you will have to repay each month is {repayment}")

else:
    print("Please enter a correct option.")       
