# Docker 설치

- Window

**Need Docker for Windows Only**



- Mac





## Docker 버전 확인

```shell
$ docker --version
$ docker version

# Client 와 Server 로 나뉘게 된다.
Client: Docker Engine - Community
 Version:           19.03.8
 API version:       1.40
 Go version:        go1.12.17
 Git commit:        afacb8b
 Built:             Wed Mar 11 01:23:10 2020
 OS/Arch:           windows/amd64
 Experimental:      false

Server: Docker Engine - Community
 Engine:
  Version:          19.03.8
  API version:      1.40 (minimum version 1.12)
  Go version:       go1.12.17
  Git commit:       afacb8b
  Built:            Wed Mar 11 01:29:16 2020
  OS/Arch:          linux/amd64
  Experimental:     false
 containerd:
  Version:          v1.2.13
  GitCommit:        7ad184331fa3e55e52b890ea95e65ba581ae3429
 runc:
  Version:          1.0.0-rc10
  GitCommit:        dc9208a3303feef5b3839f4323d9beb36df0a9dd
 docker-init:
  Version:          0.18.0
  GitCommit:        fec3683
```



- Client 는 Window
- Server는 Linux





- 도커 명령어 모음

```shell
$ docker --help
```





## Docker 실행시키기

```shell
$ docker run hello-world

# bash 실행결과
Unable to find image 'hello-world:latest' locally # 로컬에서 hello-world 못찾겠음
latest: Pulling from library/hello-world # 자기가 스스로 hello-world 다운받음
0e03bdcc26d7: Pulling fs layer
0e03bdcc26d7: Verifying Checksum
0e03bdcc26d7: Download complete
0e03bdcc26d7: Pull complete # 다운완료
Digest: sha256:49a1c8800c94df04e9658809b006fd8a686cab8028d33cfba2cc049724254202
Status: Downloaded newer image for hello-world:latest

# Hello-world 라는 Image 를 실행시킨 것임.
Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

# 처음 설치된 이 hello-world 는 Ubuntu 기반으로 설치가 되었음
To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

# 여기에 도커 Image 들을 공유하고 받을 수 있는 공간 hub.docker
Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/
```

- Pull
  - 이미지를 받는다고 생각하면 됨
- Digest
  - 서버와 클라이언트 상의 체크썸?
  - 편지를 보내는데 편지가 올바른 지 값이랑 일치하면 내용이 맞구나...?
- Status
  - latest
    - 태그 최신버전의 hello-world 를 받았음





### 가장 많이 쓰이게 될 명령어

- 도커 컨테이너 목록 출력

```shell
$ docker ps -a
```

![image-20200728010537876](C:\Users\kjaeg\AppData\Roaming\Typora\typora-user-images\image-20200728010537876.png)

**names**

- 이름을 안정해주면 랜덤으로 나온다.





### Docker Container 실행하기 (컨테이너 만들기)

```shell
$ docker container run <docker-image-name> <command>

# Image 가 없으면 Docker Hub 에서 자동으로 내려받게 됨..
$ docker container run ubuntu:latest /bin/echo 'hello world'

$ docker ps -a
$ docker container ps -a

$ docker system df

$ docker image ls
```

