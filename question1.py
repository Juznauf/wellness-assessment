total = 0

for num in range(1000):
    if num % 3 == 0 or num % 5 == 0:
        total+=num


print('sum of all the multiples of 3 or 5 below 1000 is {}'.format(total))