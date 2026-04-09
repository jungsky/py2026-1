i, k, dan =0, 0, ""

for i in range (2, 10, 1):
    dan = dan + ("#   %2d단   #" % i)

print(dan)

for i in range (1, 10, 1):
    dan = ""
    for k in range(2, 10, 1):
        dan = dan + str("%2d X %2d = %2d" % (k, i, k*i))
    print(dan)