from random import randint

counter = 0
flag = True

while flag:
    nb_1 = randint(0, 100)
    nb_2 = randint(0, 100)
    result = nb_1 + nb_2

    x_str = input("{} + {} = ".format(nb_1, nb_2))
    x = float(x_str)
    if x == result:
        counter += 1 
    else:
        flag = False

print("Number of correct operations: {}".format(counter))