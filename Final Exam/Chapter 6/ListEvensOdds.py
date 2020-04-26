listEvens = [22, 25, 24, 29, 31, 34, 99, 74, 76]
listOdds = [9, 8, 16, 25, 55, 12, 5, 3, 4, 8]
def swapLists(values):
    for i in values:
        if i % 2 == 0:
            listEvens.append(i)
        else:
            listOdds.append(i)
    print("Evens: ", listEvens)
    print("Odds: ", listOdds)

print(swapLists(int(50)))
