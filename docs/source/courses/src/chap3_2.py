x_str = input("value of x ? ")
x = float(x_str)

y = 1
for l in range(10):
    y = y*(3 - x*y*y)/2

print("y={}".format(y))



