# 파이썬(5) 0128

### regex (정규표현식)

___

> 잘해놓으면 나중에 아주 편함.....













### 다중조건 vs 중첩조건

```shell
# 다중조건... 서로 다른 그물망을 쓴다고 생각하면됨..
if 참치   #
if 방어   $
if       %

# 중첩조건(거른애를 다시 거르는 방법) : 조건이 망라적일때(exhaustive), 모든고기 낚아서 분류
if       #
elif     $
```



### 자료구조

___

> linked list
>
> stack
>
> queue



- list





### 사용 주의

| sorted()        | sort()         |
| --------------- | -------------- |
| reversed()      | reverse()      |
| 원본변경X , [:] | 원본변경O      |
| 리턴값이 있다.  | 리턴값이 없다. |





### 복사

___

- 복사가 되는게 아니라 같은 주소를 가지는 객체를 참조하고 있는것 ( **뮤터블 객체** )
  - `copy_list` 라는 변수가 같은 주소를 참조하고 있다. (별명을 붙인것)

![image-20200128132623065](img/image-20200128132623065.png)





- 진짜 복사하려면 어떻게 해야하나 ( **이뮤터블 객체** )
  - 값을 복사해서 새로운 값을 만들어내는것...

```python
original_list = [1,2,3]
copy_list = original_list[:]
copy_list[0] = 5

print(original_list)
print(copy_list)
```

![image-20200128133017415](img/image-20200128133017415.png)





##### 2차원 배열 복사 ( 깊은 복사 deep copy )

```python
a = [1, 2, [3, 4]]
b = a[:]

b[2][0] = 99
print(a)
print(b)

b[0] = 24
print(a)
print(b)
```

![image-20200128134302304](img/image-20200128134302304.png)



- `import copy`  ( deep copy 를 하게되면 메모리를 많이 잡아먹는다. )

```python
import copy

# copy.deepcopy(복사할대상)    # => deepcopy 결과물

a = [1, 2, [3, 4]]
b = copy.deepcopy(a)

b[2][0] = 99
print(a)
print(b)

b[0] = 24
print(a)
print(b)
```

![image-20200128134558409](img/image-20200128134558409.png)







### 자료구조 도식화

___

<center><img src="https://user-images.githubusercontent.com/18046097/61180439-44e60d80-a651-11e9-9adc-e60fa57c2165.png", alt="container"/></center>





## Comprehension

![image-20200128140438157](img/image-20200128140438157.png)

```python
[식 for 변수 in iterable]

list(식 for 변수 in iterable)
```



- 조건문 붙이기

```python
[식 for 변수 in iterable if 조건식]

[식 if 조건식 else 식 for 변수 in iterable]

# elif 는 다음과 같이 사용해야 합니다. (if else 열거)
[식 if 조건식 else 식 if 조건식 else 식 if ... else ... for 변수 in iterable]
```

