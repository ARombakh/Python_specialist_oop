from bar import *

bar1 = Bar(3, 7)
bar2 = Bar(3, 7)
print(bar1.__add__(bar2))

print(bar1 != bar2)

n = 5
# exp = input('exp=')
# print(eval(exp))

print(bar1.__repr__())

bar3 = eval(bar1.__repr__())

print("bar3 == bar1:")
print(bar3 == bar1)

print("bar3 is bar1:")
print(bar3 is bar1)

for item in bar1: print(item)