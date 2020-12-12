print("[Warning-This is INVALID now]Interning: string with no space and less "
      "than 20 chars")
str1 = "learning python"
str2 = "learning python"
print("str1 's memory address is ", id(str1),
      ", and str2's memory address is ", id(str2))

print("======Interning: Integers ranging between -5 and +255=====")
int1 = 10
int2 = 10
print("int1 's memory address is ", id(int1),
      ", and int2's memory address is ", id(int2))
int1 = 11256
int2 = 11256
print("int1 's memory address is ", id(int1),
      ", and int2's memory address is ", id(int2))

print("=====Augmented Assignment Statement=====")
my_tuple = (10, 20, 30)
my_tuple += (40, 50)
print(my_tuple)
my_list = ('a', 'e', 'i')
my_list += ('o', 'u')
print(my_list)
