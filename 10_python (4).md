# 파이썬(4) 0123

- 저장 / 조건 / 반복

  > 프로그래밍 초보단계

  

- 함수

  > Complexity (복잡도)  >> 해결방법 >> Abstraction (추상화, **요약**)
  >
  > Problem > `Function()`  > Solution
  >
  > 내부원리를 모르더라도,, 뭐를 입력하면 뭐가 나오는 지.. 사용법을 아는게 중요
  >
  > 절차 추상화 ( procedure ) , 조건 반복을 추상화..?
  >
  > 절차를 포장하는 개념
  >
  > **궁극적 목적** : 절차들을 모듈화(Module : 부분화)
  >
  > divide & conquer
  >
  > 레고처럼 블럭화해서 부분화해서 조립하는 것...

  

- 객체 ( OOP )

  > Abstraction (**요약, 추상화**)
  >
  > 조건 반복으로 만들어낸 함수들을 저장시킨 것.. 
  >
  > 객체는 저장의 추상화





## 함수

> 만드는 시점 ( 정의 )
>
> 활용되는 시점 ( 쓰는 시점 )



- Parameter (매개변수)

  - ```python
    def func(x):    # x 가 파라미터(매개변수)
    	return x + 2
    ```

  - `x` 는 매개변수

  - `함수의 정의` 부분에서 볼 수 있다.



- Argument (인자, 전달인자)

  - ```python
    func(2)    # 2 가 아규먼트(인자)
    ```

  - `2` 는 인자

  - `함수를 호출` 하는 부분에서 볼 수 있다.



- 직사각형 둘레 함수 정의

```python
def rectangle(width, height):
    area = width * height    # 넓이
    perimeter = 2 * (width + height)    # 둘레
    # 리턴이 여러개인것 처럼 보이지만 사실상 튜플자료형 1개가 나오는 것
    # (area, perimeter)
    # return 조심
    return area, perimeter

area, perimeter = rectangle(20, 30)
print(area)
print(perimeter)
```



- 좋은 함수란?
  - 원본은 파괴하지 않으면서 리턴값이 있는 코드
  - ex) `sorted()` 

- 실수하기 쉬운 함수

> .sort()  :  리턴값이 없다.
>
> sorted()  : 리턴값이 있다.



<u>DRY ( Don't Repeat Yourself ) : 반복되는 코드 짜지마라....</u>



```python
# 원기둥의 부피를 구하는 함수를 작성하세요.
# 밑면의 넓이 * 높이

def cylinder(r, h):
    '''
    cylinder() 함수는 원기둥의 부피를 구해주는 함수입니다.
    인자로는 반지름과 높이를 받게 되는데,
    cylinder(반지름, 높이) 형태로 활용되게 됩니다.
    
    cylinder(r, h)
    r : 반지름
    h : 높이
    '''
    return 3.14 * r**2 * h

print(cylinder(5, 2))
print(cylinder(2, 5))

# cylinder 함수의 주석을 보고 싶을때 ( 사용법 )
print(cylinder.__doc__)
```





### 이름공간(namespace)

___

![image-20200124131605196](./img/image-20200124131605196.png)











































