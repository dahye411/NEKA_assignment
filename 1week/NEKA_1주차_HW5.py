import torch

def create_matrix(rows, cols): 
    matrix=[]
    for i in range(rows):
        row=[]
        for j in range(cols):
            element=float(input("Please enter the elements in row {} and column {}: ".format(i+1, j+1)))
            row.append(element)
        matrix.append(row)
    return torch.tensor(matrix) 

rows=int(input("Please enter the number of rows in the matrix: "))
cols=int(input("Please enter the number of columns in the matrix: "))
print()

print("First matrix")
mat1=create_matrix(rows, cols)
print()

print("Second matrix")
mat2=create_matrix(rows, cols)
print()

print("addition result: ")
print(mat1+mat2)
print()

print("subtraction result: ")
print(mat1-mat2)
print()


print("multiplication result: ")
print(torch.matmul(mat1, mat2))




