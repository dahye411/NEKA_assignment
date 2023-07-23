import pandas as pd
import numpy as np

data={
    'Name': ['철수', '영희', '진희', '정혁'],
    'Age': [17, 23, 42, 29],
    'City': ['서울', '부산', '인천', '광주']
}

df=pd.DataFrame(data)

df['Salary']=[5000, 650, 2400] # data가 4개여야 하는데 3개여서 오류 발생