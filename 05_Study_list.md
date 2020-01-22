# 리스트

### 리스트의 생성 및 조작법

##### 1. 리스트의 기본 연산

- 리스트 덧셈

  - ```python
    list1 = [10, 20, 30]
    list2 = [40, 50]
    
    list3 = list1 + list2
    list3 = [10, 20, 30, 40, 50]
    ```

- 리스트 곱셈

  - ```python
    data_list = [10, 20, 30, 40]
    data_list * 3
    [10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40]
    ```



##### 2. 리스트 항목 추가

- 리스트 추가

  - ```python
    data_list = [10, 20, 30, 40]
    
    data_list.insert(2, 20)
    data_list = [10, 20, 20, 30, 40]
    
    data_list.extned([50, 60]) # 반환 값 : None
    data_list.append([70, 80])
    data_list = [10, 20, 20, 30, 40, 50, 60, [70, 80]]
    ```



##### 3. 리스트 항목 변경

- 리스트 변경

  - ```python
    data_list = [10, 20, 30, 40]
    
    data_list[2] = 29
    data_list = [10, 20, 29, 40]
    
    data_list[1:3] = [12, 15]
    data_list = [10, 12, 15, 40]
    
    data_list[1:3] = [12, 15, 20]
    data_list = [10, 12, 15, 20, 40]
    
    data_list[2:3] = [31, 25]
    data_list = [10, 12, 31, 25, 20, 40]
    ```



##### 4. 리스트 항목 제거

- 리스트 제거

  - ```python
    data_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    
    del data_list[2]
    data_list = [10, 20, 40, 50, 60, 70, 80, 90, 100]
    
    del data_list[3:5]
    data_list = [10, 20, 40, 70, 80, 90, 100]
    
    data_list.pop(5) # 인덱스 5에 해당하는 항목 제거
    data_list = [10, 20, 30, 70, 80, 100]
    
    data_list.remove(100)
    data_list = [10, 20, 30, 70, 80]
    
    data_list.clear() # del data_list[:]
    data_list = []
    ```



##### 5. 리스트 항목 확인

- **in**

  - ```python
    data_list = [10, 20, 30, 50, 50, 50, 60, 70, 80]
    
    50 in data_list => True # not in 은 해당 항목이 없는지 검사
    50 not in data_list => False
data_list.count(50) => 3
    ```
    



##### 6. 리스트와 for문

- 리스트와 for문

  - ```python
    data_list = list(range(0, 11, 2))
    
    for item in data_list: # 리스트 항목을 반복해서 변수 item에 저장
    	print("{0}".format(item), end="")
    
    print()
    
    for idx, item in enumerate(data_list): # enumerate() 함수를 쓰면 index, item 리턴
        print("data_list[{0}] => {1}".format(idx, item))
    ```



- 리스트 내포

  - `list = [x for x in 순회객체]` 

  - ```python
    data_list1 = [1, 2, 3, 4, 5]
    
    print("data_list1 : {0} {1}".format(type(data_list1), data_list1))
    
    data_list2 = []
    for item in data_list1:
    	data_list2.append(item)
    	print("data_list2: {0} {1}".format(type(data_list2), data_list2)
    
    data_list3 = [item for item in data_list1]
              print("data_list3: {0} {1}".format(type(data_list3), data_list3))
              
    data_list4 = [x*y for x in data_list1 if x % 2 == 1 
                       for y in data_list1 if y % 2 == 0]
              
    ```

  - 



