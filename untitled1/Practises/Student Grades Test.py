target = 30000
balance = 10000
year = 0
rate = 10.0

while balance < target:
    year = year + 1
    print(year, balance)
    interest = (balance*rate)/100
    balance = balance + interest

#print results
print("Over {} years, you acquired ${} of interest. Your balance is now ${}.".format(year, "%0.2f" % interest, balance))




