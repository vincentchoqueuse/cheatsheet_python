# initialization
coefs = [1, -0.2, 0.4]

# algorithm
x = float(input("value of x ? "))
p_x = coefs[0]*(x**2) + coefs[1]*x + coefs[2]

# display outputs
print("p({})={}".format(x, p_x))