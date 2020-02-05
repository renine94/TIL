# 파이썬 (3) 0122

### (1) 딕셔너리 dict

1. dict 활용

   - ```python
     * dictionary에서 `for` 활용하는 4가지 방법
     
     ​```python
     # 0. dictionary (key 반복)
     for key in dict:
         print(key)
     
     
     # 1. key 반복
     for key in dict.keys():
         print(key)
         
         
     # 2. value 반복    
     for val in dict.values():
         print(val)
     
         
     # 3. key와 value 반복 ( 제일 많이 쓰인다. )
     for key, val in dict.items():
         print(key, val)
     
     ​```
     ```



### (2) 리스트

1. 리스트 내포

   - ```python
     iterable_object = [item_expression for item in iterable_list if item_condition]
     ```

     - ex) 구구단 3단을 출력하되 짝수가 아닌 것만 출력

       ```python
       gugu_three = [x * 3 for x in range(9) if x % 2 is not 0]
       # [3, 9, 15, 21]
       ```



<img src="C:\Users\multicampus\private_study\0120 ~ 0123 [3weeks]\리터러블, 시퀀스.jpg" style="zoom:80%;" />



### (3) recursion (재귀)

- divide & conquer. (분할 정복)







## 알고리즘

>  Input 을 어떻게 받아 Output 을 어떻게 출력할지부터 생각하라