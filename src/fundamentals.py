import keyword
print("=======Keyword========")
print(keyword.kwlist)

print("======Identifier======")
print('_test is identifier?', '_test'.isidentifier())
print('1test is identifier?', '1test'.isidentifier())
print('test1 is identifier?', 'test1'.isidentifier())
print('test_1 is identifier?', 'test_1'.isidentifier())

print("======Variable=======")
vari = 10
print(vari, " is of type ", type(vari))
vari = "string"
print(vari, " is of type ", type(vari))
vari = {'a', 'b', 'c'}
print(vari, " is of type ", type(vari))
