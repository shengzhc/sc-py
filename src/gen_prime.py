def find_prime(limit):
    num = 1
    while num < limit:
        if num > 1:
            for x in range(2, num):
                if num % x == 0:
                    break
            else:
                yield num
        num += 1


for prime in find_prime(100):
    print(prime)
