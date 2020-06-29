def load_first_matric():
    row1, col1 = map(int, input("Enter size of first matrix: ").split())
    print("Enter first matrix:")
    m1 = [[float(j) for j in input().split()] for i in range(row1)]
    return row1, col1, m1

def load_second_matric():
    row2, col2 = map(int, input("Enter size of second matrix: ").split())
    print("Enter second matrix:")
    m2 = [[float(j) for j in input().split()] for i in range(row2)]
    return  row2, col2, m2

def normal_load():
    row1, col1 = map(int, input("Enter size of matrix: ").split())
    print("Enter matrix:")
    m1 = [[float(j) for j in input().split()] for i in range(row1)]
    return row1, col1, m1

def transpose(row, col, amatrix, type):
    """
    row and col are int
    """
    new_m = [["" for j in range(col)] for i in range(row)]
    if type == "1":
        for i in range(row):
            for j in range(col):
                if i != j:
                    new_m[j][i] = amatrix[i][j]
                else:
                    new_m[i][j] = amatrix[i][j]
    elif type== "2":
        for i in range(col):
            for j in range(row):
                if i + j != row - 1:
                    new_m[row - 1 - j][col - 1 - i] = amatrix[i][j]
                else:
                    new_m[i][j] = amatrix[i][j]
    elif type == "3":
        for i in range(col):
            for j in range(row):
                new_m[i][col - 1 - j] = amatrix[i][j]
    else:
        for i in range(col):
            for j in range(row):
                new_m[row - 1 -i][j] = amatrix[i][j]
    print("The result is:")
    for i in new_m:
        print(*i)

def get_ma_len(matx):
    return len(matx) * len(matx[0])

def calc_det(b,col, i =0):
    if get_ma_len(b) == 1:
        return b[0][0]
    else:
        if get_ma_len(b) == 4:
            return b[0][0] * b[1][1] - b[0][1] * b[1][0]
        else:
            total = 0  # important
            for j in range(col):
                imp = b[i][j]
                new_b = []
                for ii in range(len(b)):
                    new_row = []
                    for jj in range(len(b[0])):
                        if ii != i and jj != j:
                            new_row.append(b[ii][jj])
                    if new_row:
                        new_b.append(new_row)
                ans = imp * (-1)**(i + j) * calc_det(new_b, len(new_b[0]))
                total += ans
            return total

def get_matrix(matrix, i, j):
    new_b = []
    for ii in range(len(matrix)):
        new_row = []
        for jj in range(len(matrix[0])):
            if ii != i and jj != j:
                new_row.append(matrix[ii][jj])
        if new_row:
            new_b.append(new_row)
    return new_b

def get_minor(matrix, i, j):
    new_matrix = get_matrix(matrix, i, j)
    return calc_det(new_matrix, len(new_matrix[0]))

def get_adj(tar_matx):
    row = len(tar_matx)
    col = len(tar_matx[0])
    ans = [["" for i in range(col)] for i in range(row)]
    for i in range(row):
        for j in range(col):
            minor = get_minor(tar_matx, i, j)
            ans[i][j] = (-1)**(i+j)*minor
    return ans

while True:
    choice = input("""
1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit
Your choice: """)
    if choice == "1":
        row1, col1, m1 = load_first_matric()
        row2, col2, m2 = load_second_matric()
        if row1 != row2 or col1 != col2:
            print("The operation cannot be performed.")
        else:
            result = [[" " for j in i] for i in m1]
            for i in range(row1):
                for j in range(col1):
                    result[i][j] = m1[i][j] + m2[i][j]
            print("The result is:")
            for i in result:
                print(*i)
    elif choice == "2":
        row1, col1, m1 = normal_load()
        num = float(input("Enter constant: "))
        new_m1 = [[num * j for j in i] for i in m1]
        print("The result is:")
        for i in new_m1:
            print(*i)
    elif choice == "3":
        row1, col1, m1 = load_first_matric()
        row2, col2, m2 = load_second_matric()
        if col1 != row2:
            print("The operation cannot be performed.")
        else:
            new_m2 = [[m2[i][j] for i in range(row2)] for j in range(col2)]
            result = [[0 for i in range(col2)] for j in range(row1)]
            for i in range(row1):
                for j in range(col2):
                    result[i][j] = sum([m1[i][f] * new_m2[j][f] for f in range(col1)])
            print("The result is:")
            for i in result:
                print(*i)
    elif choice == "4":
        type = input("""
1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line
Your choice: """)
        row1, col1, m1 = normal_load()
        transpose(row1, col1, m1, type)
    elif choice == "5":
        row1, col1, m1 = normal_load()
        print("The result is:")
        print(calc_det(m1, len(m1[0])))
    elif choice == "6":
        row1, col1, m1 = normal_load()
        det = calc_det(m1, len(m1[0]))
        if det == 0:
            print("This matrix doesn't have an inverse.")
        else:
            adj = get_adj(m1)
            new_m = [["" for j in range(col1)] for i in range(row1)]
            for i in range(row1):
                for j in range(col1):
                    if i != j:
                        new_m[j][i] = adj[i][j]
                    else:
                        new_m[i][j] = adj[i][j]
            d = 1/det
            t = [[d * j for j in i] for i in new_m]
            t = [[0 if ele ==0 else int(ele * 100)/100 for ele in i]for i in t]
            print("The result is:")
            for i in t:
                print(*i)
    elif choice == "0":
        break
    else:
        print("Invalid Input!")










