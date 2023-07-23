import torch

square_matrix=torch.tensor([[9, 13, 5, 2],
                            [1, 11, 7, 6],
                            [3, 7, 4, 1],
                            [6, 0, 7, 10]])

print("Rotate clockwise 90 degrees: ")
print(torch.rot90(square_matrix, 3, [0, 1])) # 반시계 방향으로 270도 회전 = 시계 방향으로 90도 회전
print()

print("Rotate clockwise 180 degrees: ")
print(torch.rot90(square_matrix, 2, [0, 1])) # 반시계 방향으로 180도 회전 = 시계 방향으로 180도 회전
print()

print("Rotate clockwise 270 degrees: ")
print(torch.rot90(square_matrix, 1, [0, 1])) # 반시계 방향으로 90도 회전 = 시계 방향으로 270도 회전
print()

print("Flip it upside down relative to the vertical axis: ") # 세로 축을 기준으로 반대로 뒤집기
print(torch.flip(square_matrix, [1])) 
print()

print("Flip it upside down relative to the horizontal axis: ") # 가로 축을 기준으로 반대로 뒤집기
print(torch.flip(square_matrix, [0]))
print()

