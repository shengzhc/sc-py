def fib_func(xterms):
    x1 = 0
    x2 = 1
    count = 0
    if xterms <= 0:
        print("Please provide a +ve integer")
    elif xterms == 1:
        print("Fibonacci seq upto", xterms, ":")
        print(x1)
    elif xterms == 2:
        print("Fibonacci seq upto", xterms, ":")
        print(x2)
    else:
        while(count < xterms):
            xth = x1+x2
            count += 1
            x1 = x2
            x2 = xth
            print("Before yield, count %d, xth: %d" % (count, xth))
            yield xth


fib = fib_func(5)
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
