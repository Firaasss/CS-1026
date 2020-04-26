##Program for a company that rents out vehicles
##FIRAS ABOUSHAMALAH
##250920750
#

#variables to be used in the program pertaining to customer + vehicle rented out
name = (input("What is your name? "))    #customer's name
code = (input("Please type in your classification code ('B', 'D', or 'W' ): ").upper())    #Classification code: 'B' for budget, 'D' daily, 'W' weekly

#Code Error - must be either d, b or w (non-capital will be changed to capital)
if code == 'd'.upper() or code == 'b'.upper() or code == 'w'.upper():
    pass    #do nothing and continue program
else:
    print("")
    print("Sorry {}! That code is not available. Please enter either 'B', 'D', or 'W'".format(name))
    exit()

daysRented = int(input("How many days was the vehicle rented for? "))    #int of days rented
startOdometer = int(input("What was the odometer reading at the start of the rental period? (eg. 13594) "))
endOdometer = int(input("What was the odometer reading at the end of the rental period? "))

KM_DRIVEN = endOdometer - startOdometer    #total kilometers driven during rental period

#Code 'B' (budget)
B_BASE_CHARGE = 20.00    #base charge is always $20.00 for each day
B_KM_CHARGE = 0.30    #Kilometers driven charge is always $0.30 for each KM driven
B_SUM = ((B_BASE_CHARGE * daysRented) + (B_KM_CHARGE * KM_DRIVEN))
#Compute total cost for Option B

if code == "B":
    print("")
    print("You drove {}km during your rental period. \nThe total is ${}.".format(KM_DRIVEN, "%0.2f" % B_SUM))    #shows the total with 2 decimal places after the.


#Code 'D' (daily)
D_BASE_CHARGE = 50.00    #base charge is $50.00 for each day
dKmCharge = 0.30    #0.30 cents base charge
dSumNoCharge = (D_BASE_CHARGE * daysRented)    #This is the charge if the KM are under/equal to 100
dSumCharge = (D_BASE_CHARGE * daysRented) + ((dKmCharge * KM_DRIVEN) - (dKmCharge * 100*daysRented))    #charge for every km over 100 after first 100km per day limit
AVG_KM = round(KM_DRIVEN / daysRented)    #finds out the average KM driven per day

if code == "D":
    if AVG_KM <= 100:  #If avg KM driven are less or equal to 100 KM, no additional charge over base charge.
        print("")
        print("You drove an average of {}km per day for {} days (total {}km) - there is no additional KM charge. \nThe total is ${}.".format(AVG_KM, daysRented, KM_DRIVEN, "%0.2f" % dSumNoCharge))
    else:  #if Km is over 100, print:
        print("")
        print("You drove an average of {}km per day for {} days (total {}km) - there is an additional charge of ${}. \nThe total is ${}.".format(AVG_KM, daysRented, KM_DRIVEN, "%0.2f" % dSumCharge, "%0.2f" % dSumCharge))

#Code 'W' (weekly)
W_BASE_CHARGE = 200.00

import math     #retrieve the math ceiling method to roudn up to next integer
NUM_WEEKS = math.ceil(daysRented / 7)    #will use daysRented to create weeks from 1.1 to 2 and 2.2 to 3, etc.
AVG_KM_WEEK = round(KM_DRIVEN / NUM_WEEKS)    #Average number of kilometers driven by week - total km driven divided by # weeks
W_KM_CHARGE = 50.00 * NUM_WEEKS    #this is the charge if the avg km driven per week is less/equal to 1000.
kmOverLimit = AVG_KM_WEEK - 2000    #this calculates how many km exceed the 2000 per week limit
W_KM_CHARGE_2 = (100.00 * NUM_WEEKS) + (0.30 * kmOverLimit)*NUM_WEEKS   #the charge for going over 2000 per week average


W_SUM_BASE = W_BASE_CHARGE * NUM_WEEKS    #this is the charge if the average km per week was less than/equal to 1000
W_FULL_CHARGE = W_SUM_BASE + W_KM_CHARGE    #this is charged if the average km per week exceeds 1000 and but not 2000
W_FULL_CHARGE_2 = W_SUM_BASE + W_KM_CHARGE_2

if code == "W":  #if the user chooses code W, the following will be printed:
    if AVG_KM_WEEK <= 1000:
        print("")
        print("You drove an average of {}km per week for {} weeks (total {}km) - there is no additional KM charge! \nThe total is ${}".format(AVG_KM_WEEK, NUM_WEEKS, KM_DRIVEN, "%0.2f" % W_SUM_BASE))
    elif (AVG_KM_WEEK <= 2000) and (AVG_KM_WEEK > 1000):  #if the KM driven per week exceed 1000 but are less/equal to 2000, print the following:
        print("")
        print("You drove an average of {}km per week for {} weeks (total {}km) - there is an additional charge of ${}. \nThe total is ${}.".format(AVG_KM_WEEK, NUM_WEEKS, KM_DRIVEN, "%0.2f" % W_KM_CHARGE, "%0.2f" % W_FULL_CHARGE))
    elif AVG_KM_WEEK > 2000:   #if KM exceed 2000, charge main fee of $200/week, with additional $100/week + $0.30/km driven over the 2000km limit average.
        print("")
        print("You drove an average of {}km per week (total {}km). The limit is 2000km. You went {}km over, leaving an additional charge of ${} \nThe total is ${}.".format(AVG_KM_WEEK, KM_DRIVEN, kmOverLimit, "%0.2f" % W_KM_CHARGE_2, "%0.2f" % W_FULL_CHARGE_2))
