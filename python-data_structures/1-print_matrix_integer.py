def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i,k in enumerate(row):
            print("{:d}".format(k), end=" " if i<len(row)-1 else "")
        print()