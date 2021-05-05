#This code is about a financial decision for the user between Investment or Bond
#Then calculations are made If the user invested or get a bond
#It tells the user how much money he would receive after the period if he invested of tells the user how much money he will pay after the bond period monthly

import math     #Imports the math functions.

print ("Choose either 'Investment' or 'Bond' from the menu below") # Asks the user to choose between bond or investment. 

space= ("\n")       # Saves a line spacing as a variable called space
print (space)       # Prints the line spacing.

print("Investment   - to calculate the amount of interest you'll earn on interest") # Prints a short explanation of what investment is
print("Bond         - to calculate the amount you'll have to pay on a home lone")   # Prints a short explanation of what a bond is

print (space)       # Prints the line spacing

choice= input("")   # Saves the users input as a variable called choice
print (space)       # Prints the line spacing


if choice == "Investment" or choice == "ÏNVESTMENT" or choice == "investment":  # Starts an if statement if the users input was Investment or INVESTMENT or investment

    print ("How much money would you like to deposit: ")# Asks the user how much money he wants to deposit
    money = float(input("R"))               # Saves the users input as a float variable called money
    print (space)                           # Prints the line spacing

    print ("What is the interest rate? (Only the number is needed not '%' to)") # Asks the user at what interest rate the user invests
    rate = float(input(""))                 # Saves the users input as a float variable called rate
    print (space)                           # Prints the line spacing
    
    print ("For how many years would you like to invest the money? (Only the number is needed) ")   # Asks the period time the user wants to invest their money
    years = float(input(""))                # Saves the users input as a float variable called years
    print (space)                           # Prints the line spacing
    
    print ("Do you prefer Simple or Compound interest ")# Asks the user if they prefer simple or compound interest
    interest = input("")                    # Saves users input as a variable called interest
    interest== "Simple"                     # If the variable interest is equal to simple
    amount = money*(1+rate*years)           # Calculates money multiplied by 1+rate multiplied by year and saves the answer as variable called amount  
    print ("R"+str(amount))                 # Prints variable called amount as a string
    print (space)                           # Prints the line spacing
    
    interest == "Compound"                  # If the variable interest is equal to compound                          
    amount = money*math.pow((1+rate),years) # Calculates money multiplied by math.pow of 1+rate and year
    print ("R"+str(amount))                 # Prints variable called amount as a string                 



elif choice== "Bond" or choice== "bond" or choice== "BOND": # Starts a elif statement if the users input  was bond

    print("What is the value of the house?")# Asks the user the value of the house they want to get a bond on
    money = float(input(""))                # Saves the users input as a float variable called money
    print (space)                           # Prints the line spacing
    
    print ("What is the interest rate? (Only the number is needed not '%' to)") # Asks the user what interest rate the bond should be
    rate = float(input(""))                 # Saves the users input as a float variable called rate
    print (space)                           # Prints the line spacing
    
    print ("In how many months are you planning to repay the loan? ")   # Asks the user in how many months he wants to pay the bond
    months = float(input(""))               # Saves the users input as a float variable called months
    years = months/12                       # divides months by 12 and saves it as a variable called years
    repayment = (years*money)/(1-math.pow((1-years),-months)) #Calculates year multiplied by money and that divided by a math.pow 1-years and -months and saves it as a variable called repayment
    repayment_monthly = repayment/months    # Calculates repayment divided by months and saves it as a variable called repayment_monthly to calculate the monthly payment
    print (space)                           # Prints the line spacing

    print ("R"+str(repayment_monthly)+" per month") # Prints the variable repatment_monthly's value this is what the user will pay per month
