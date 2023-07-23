import torch

def multiply_tensors(a, b):
    c=a*b # tensor1과 tensor2의 크기가 일치하지 않아서 오류 발생
    return c

tensor1=torch.tensor([2, 4, 6])
tensor2=torch.tensor([1, 3]) 

result=multiply_tensors(tensor1, tensor2)
print(result)