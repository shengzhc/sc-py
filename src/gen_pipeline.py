def find_prime():
    num = 1
    while num < 100:
        if num > 1:
            for x in range(2, num):
                if num % x == 0:
                    break
            else:
                print("find_prime:", num)
                yield num
        num += 1


def find_odd_prime(seq):
    for num in seq:
        if (num % 2) != 0:
            print("find_odd_prime:", num)
            yield num


a_pipeline = find_odd_prime(find_prime())
for _ in a_pipeline:
    pass
