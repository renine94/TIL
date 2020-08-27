# -*- coding: utf-8 -*-
"""002_레모네이드 판매 예측.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FiiyR8XfwsnJauHriWQzz1gVmtkVxJrI
"""

# 라이브러리 사용
import pandas as pd
import tensorflow as tf

# 데이터 준비
데이터 = pd.read_csv('https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/lemonade.csv')
데이터.head()

# 독립변수, 종속변수
독립 = 데이터[['온도']]
종속 = 데이터[['판매량']]

print(독립.shape, 종속.shape)

# 모델을 만듭니다.
X = tf.keras.layers.Input(shape=[1]) # 독립변수 개수
Y = tf.keras.layers.Dense(1)(X) # 종속변수 개수
model = tf.keras.models.Model(X, Y)
model.compile(loss='mse')

# 모델을 학습합니다.
model.fit(독립, 종속, epochs=10000, verbose=0) # verbose = 0 을 주면 학습을 하는 동안 화면출력을 하지 않는다.
model.fit(독립, 종속, epochs=10) # 학습시킨후에 10번만 더 학습시켜서 결과를 확인한다.

# 모델을 이용합니다.
model.predict(독립)

# 모델을 이용한 예측
model.predict([[15]])

# 값만 예쁘게 정제해서 도출하기
int(round(model.predict([[15]])[0][0], 1))

