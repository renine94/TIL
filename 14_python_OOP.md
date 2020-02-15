# OOP ( 객체지향 프로그래밍 )

> 코드 관리가 쉬워짐
>
> ex) Duck.run()  => 오리야 달려! 사람이 읽기 쉽게끔 `주어+동사` 형태로 만들었다.
>
> 코드 => 함수 => 객체지향프로그래밍



- 클래스(Class)
  - 객체를 표현하는 문법
  - 속성과 행위 ( 자동차, 색상 )
- 인스턴스(instance) == `객체` 
  - 클래스의 인스턴스/객체 ( 실제로 메모리상에 할당된 것 )
  - 객체는 자신 고유의 속성(Attribute)을 가지며 클래스에서 정의한 행위를 수행할수 있다.
- 속성(attribuet)
  - 클래스/인스턴스가 가지고 있는 속성(값)
- 메서드(Method)
  - 클래스/인스턴스가 할 수 있는 행위(**함수**)



```python
class Person:
    name = 'ssafy' # class attribute ( 클래스 속성 )
    
    # 생성자 정의
    def __init__(self, name='samsung'):
        self.name = name # instance attribute ( 객체 속성 )
        

john = Person('John')
Jaegu = Person('Jaegu')
ssafy = Person()

print(john.name)
print(Jaegu.name)
print(ssafy.name)

Person.name
```











