print("====List Comprehension====")
# for element in list, if true, return value of expression based
# upon the element in the list
listofCountries = ["India", "America", "England", "Germany", "Brazil",
                   "Vietnam"]
theList = [country[0] for country in listofCountries]
print(theList)
print([x+y for x in 'get' for y in 'set' if x != 't' and y != 'e'])
for index, value in enumerate(listofCountries):
    print(index, value)

print("====List Repetition====")
two_dim_list = [[0]*3] * 3
print(id(two_dim_list[0]), id(two_dim_list[1]), id(two_dim_list[2]))

print("====List Slicing====")
theList = [1, 2, 3, 4, 5, 6, 7, 8]
print(theList[4:-5])

print("====List Reverse====")
print(theList[::-1])
print(theList[0:4:-1])
