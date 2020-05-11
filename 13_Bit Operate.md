# 비트 연산자

![bitwise_operator](https://image.slidesharecdn.com/15-bitwiseoperators-130815152621-phpapp02/95/15-bitwise-operators-3-638.jpg?cb=1376580623)

```python
[1, 3, 5, 7]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
 x  o  x  o  x  o  x  o  x  x
 0  1  0  1  0  1  0  1  0  0   => 2진수로 표현가능
```



```
arr = [3, 6, 7, 1, 5, 4]
```



**비트연산자 예시**

![9A04CBE9-8EEC-4CE1-BBC0-56B53A6F3271](img/9A04CBE9-8EEC-4CE1-BBC0-56B53A6F3271.png)





#### 파이썬으로 부분집합 만드는방법 ( 비트오퍼레이션 이용 )

```python
arr = [3, 6, 7, 1, 5, 4]
n = len(arr)

for i in range(1<<n):
  for j in rnage(n):
    if i & (1<<j):
      arr[i]
  print()
print()
```



- 연습

```python
# 1 << 4   // 1    ===>   1 0 0 0 0

print( 10001 & ( 1 << 4 ) ) # => 10000

print( 2 & ( 1 << 1 ) ) # => 2


# 2진법 만들기 코드
def find(number):
    bina = ''
    for i in range(3, -1, -1):
        bina += '1' if number&(1<<i) else '0'
    return bina

print(find(4))
```

