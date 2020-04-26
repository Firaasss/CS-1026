def mySumOdds(low, hi):
    total = 0
    for i in range(low, hi+1, 1):
        if i % 2 ==1:
            total = total + i

    print("The difference between the numbers is", hi - low)
    return total

x = mySumOdds(50, 500)
print("The sum of the two is", x)

