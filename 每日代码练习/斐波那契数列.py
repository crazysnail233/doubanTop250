def fb(i):
    list = [0,1]
    if i < 2:
        return  list[i]
    elif i >= 2:
        return (fb(i-2) + fb(i-1))

print(fb(10))