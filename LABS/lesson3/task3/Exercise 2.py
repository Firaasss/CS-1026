month = input("What month of the year is it? ")

if (month == "January") or (month == "December") or (month == "February"):
    print("In {}, it is Winter. Go snowboarding".format(month))
elif (month == "March") or (month == "April") or (month == "May"):
    print("In {}, it is Spring. How about you go hiking?".format(month))
elif (month == "June") or (month == "July") or (month == "August"):
    print("In {}, it is Summer. Go Swim.".format(month))
elif (month == "September") or (month == "October") or (month == "November"):
    print("In {}, it is Autumn. Maybe go for a bike ride or something".format(month))
else:
    print("That's not a proper month. Or use a capital letter.")
