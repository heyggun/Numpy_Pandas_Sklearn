# -*- coding: utf-8 -*-
"""Pandas_DataFrame_Indexing.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zZ81tqmeI-wnOPbbHJC8wvWDNYErh7bM
"""

# 데이터프레임 고급 인덱싱
# 데이터프레임에서 특정한 데이터만 골라내는 것을 인덱싱(indexing)이라 함
# Pandas는 Numpy 행렬과 같이 쉼표를 사용한 (행 인덱스, 열 인덱스) 형식의 2차원 인덱싱을
# 지원하기 위해 다음과 같은 특별한 인덱서(indexer) 속성도 제공

# loc : 라벨값 기반의 2차원 인덱싱
# iloc : 순서를 나타내는 정수 기반의 2차원 인덱싱

# loc 인덱서

# df.loc[행 인덱싱 값]
# df.loc[행 인덱싱 값, 열 인덱싱 값]

# 여기서 행 인덱싱 값은 정수 또는 행 인덱스데이터,
# 열 인덱싱값은 라벨 문자열임
# 인덱스데이터
# 인덱스데이터 슬라이스
# 인덱스데이터 리스트
# 같은 행 인덱스를 가지는 불리언 시리즈(행 인덱싱인 경우)
# 또는 위의 값을 반환하는 함수

import pandas as pd
import numpy as np

df = pd.DataFrame(np.arange(10,22).reshape(3,4),
                  index = ["a", "b", "c"],
                  columns = ["A", "B", "C", "D"])
df

# 인덱싱값을 하나만 받는 경우
# 만약 loc 인덱서를 사용하면서 인덱스를 하나만 넣으면 행(row)을 선택함
# 인덱스데이터가 "a" 인 행을 고르면 해당하는 행이 시리즈로 출력
# 시리즈라서 상하로 길게 출력되기는 했지만 행을 가져오고 있음

df.loc["a"]

# 인덱스데이터의 슬라이스도 가능

df.loc["b":"c"]

# 위는 사실 loc를 쓰지 않는 경우와 같음
df["b":"c"]

# 인덱스데이터의 리스트도 됨
df.loc[["b","c"]]

# 이때는 loc를 쓰지 않으면 KeyError 발생
df[["b","c"]]

# 데이터베이스와 같은 인덱스를 가지는 불리언 시리즈도 행을 선택하는 인덱싱 값으로 씀
df.A > 15

df.loc[df.A > 15]

# 인덱스 대신 인덱스 값을 반환하는 함수 사용 가능
# 다음 함수는 A열의 값이 12보다 큰 행만 선택

def select_rows(df):
  return df.A>15

select_rows(df)

df.loc[select_rows(df)]

# loc 인덱서가 없는 경우에 사용했던 라벨 인덱싱이나 라벨 리스트 인덱싱은 불가능

# 원래 (행) 인덱스값이 정수인 경우에는 슬라이싱도 라벨 슬라이싱 방식을 따름
# 즉 슬라이스의 마지막 값이 포함됨

df2 = pd.DataFrame(np.arange(10, 26).reshape(4,4), columns=["A", "B", "C", "D"])
df2

df2.loc[1:2]

# 인덱싱값을 행과 열 모두 받는 경우
# 인덱싱값을 행과 열 모두 받으려면 df.loc[행 인덱스, 열 인덱스] 형태로 사용
# 행 인덱스 라벨값이 a, 열 인덱스 라벨값이 A인 위치의 값을 구함

df.loc["a", "A"]

# 인덱싱값으로 라벨 데이터의 슬라이싱 또는 리스트를 사용할 수 있음

df.loc["b":"A"]

df.loc["a", :]

df.loc[["a","b"],["B","D"]]

# 행 인덱스가 같은 불리언 시리즈나 이러한 불리언 시리즈를 반환하는 함수도 행의 인덱싱 값이 될 수 있음

df.loc[df.A > 10, ["C","D"]]

# iloc 인덱서

# iloc 인덱서는 loc 인덱서와 반대로 라벨이 아니라 순서를 나타내는 정수(integer) 인덱스만 받음

df.iloc[0,1]

df.iloc[:2, 2]

df.iloc[0, -2:]

df.iloc[2:3, 1:3]

df

# loc 인덱서와 마찬가지로 인덱스가 하나만 들어가면 행을 선택함

df.iloc[-1]

df.iloc[-1] = df.iloc[-1]*2
df

