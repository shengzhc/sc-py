print("=====Argument Formatting=====")
print('{}'.format("Hello"))
print('{'+'{}'.format("Hello")+'}')

print("=====Padding=====")
print("right aligned with 10 spots: {}".format(format("Hello", "*>10s")))
print("left aligned with 10 spots: {}".format(format("Hello", "*<10s")))
print("center aligned with 20 spots: {}".format(format("Hello", "*^20s")))

print("=====Justify=====")
print('<--{0:*>30}-->'.format('Python Programming'))
print('<--{0:*<30}-->'.format('Python Programming'))
print('<--{0:*^30}-->'.format('Python Programming'))
