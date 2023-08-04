def fact(num):
    if num == 0:
        return 1
    else:
        return num * fact(num-1)
x = eval(input("enter the number"))
print(fact(x))