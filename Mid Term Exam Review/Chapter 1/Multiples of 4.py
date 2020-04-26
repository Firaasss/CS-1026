#Write a program that prints to the screen all multiples of 4 between 5 and 50 (inclusive)

count = 5
while count <= 50:
    count = count + 1
    if count % 4 == 0:
        print(count)
