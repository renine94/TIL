# Command 명령어

- 커맨드 명령어 별명줘서 짧게 만들기

![image-20200326134841430](img/image-20200326134841430.png)

1. `vi .bashrc` 로 `.bashrc` 파일 만들기 및 접근 (`~` 위치에서 접근해야 함.)
2. `i` , 즉 insert mode 의 약자를 쳐서 편집 모드 진입
3. `alias jn="jupyter notebook"`
4. `esc` 3번 정도 연타해 편집 모드를 벗어난 후 `:wq` 를 쳐서 저장하고 vi 탈출.
5. 설정이 바뀌었음을 터미널에 알려주는 명령어인 `source ~/.bashrc` 를 쳐서 업데이트.
6. 나와서 `ls -a` 쳐보면 `.bashrc` 파일이 생겨 있는 걸 알 수 있음. 
7. `cat .bash_history` 를 치면 내가 이전에 어떤 명령어를 쳤었는지 리스트를 볼 수 있음. 사실 그냥 `history` 라고만 쳐도 비슷한 결과를 받아볼 수 있음.





