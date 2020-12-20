import functools

alist = [lambda m:m**2, lambda m, n:m*n, lambda m:m**4]
print(alist[0](10), alist[1](10, 20), alist[2](2))

alist = ['learn', 'python', 'step', 'by', 'step']
print("=====Lambda=====")
print(list(map(lambda m: m.upper(), alist)))

print("=====Func=====")


def capitalize_list(s):
    return s.capitalize()


print(list(map(capitalize_list, alist)))


print("=====Reduce=====")


def my_func(m, n):
    return m+n


print(functools.reduce(my_func, [1, 2, 3, 4]))
print(functools.reduce(lambda m, n: m+n, [1, 2, 3, 4]))
