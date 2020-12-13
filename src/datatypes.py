import sys

print("=====Complex number=====")
num = 3+5j
print("The num", num, " is complex number?", isinstance(num, complex))
print(num.real, num.imag)

print("=====System float info=====")
print(sys.float_info)
print(sys.float_info.dig)

print("=====Tuples=====")
sample_tuple = ('Python 3',) * 3
print(sample_tuple)

print("=====Set=====")
another_set = set([1, 2, 3, "ab"])
print(another_set)
