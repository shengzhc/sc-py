alist = [4, 16, 64, 256]
print("=====List Comprehension=====")
print([var**(1/2) for var in alist])

print("====Generator Expression=====")
iter = (var**(1/2) for var in alist)
print(iter)
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))


class AP:
    def __init__(self, a1, d, size):
        self.ele = a1
        self.diff = d
        self.len = size
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count > self.len:
            raise StopIteration
        elif self.count == 0:
            self.count += 1
            return self.ele
        else:
            self.count += 1
            self.ele += self.diff
            return self.ele


print("======AP Class======")
for ele in AP(10, 2, 5):
    print(ele)


def ap_yield(a1, d, size):
    count = 0
    while count < size:
        yield a1
        count += 1
        a1 += d


print("=====AP Gen Expression=====")
for ele in AP(10, 2, 5):
    print(ele)
