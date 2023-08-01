for i in range(10):
    for k in range (i+1, 10):
        if i<8:
            print(f"{i}{k:01d}".format(i,k), end=", ")
        else:
            print(f"{i}{k:01d}".format(i,k))
        