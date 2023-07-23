import numpy as np
import pandas as pd

data={
    'A': np.random.randint(1, 10, 5), # 1부터 9까지 랜덤한 정수 5개
    'B': np.random.randint(1, 10, 5)
}

df=pd.DataFrame(data)

df['C']=df['A']+df['B']
print(df)

df['D']=df.mean(axis=1) # df.mean(axis=0)은 열에 포함된 각 행 값들의 평균을 구함, df.mean(axis=1)은 행에 포함된 각 열 값들의 평균을 구함
                        # axis=0은 책을 위로 쌓는 것이라 생각(진행방향이 세로-열), axis=1은 책을 옆으로 쌓는 것이라 생각(진행방향이 가로-행)
print(df)