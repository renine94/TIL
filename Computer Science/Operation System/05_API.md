# API

> - API 정의
>
> 쉽게  이야기 하면 `API는 서버에서 약속된 정보를 내려주는 것` 을 의미합니다.
>
> **API는 보통 서버 개발자가 (API를 요청하는) 클라이언트를 위해 개발하게 됩니다.**



![API서버](https://www.grabbing.me/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fce356783-40c1-4120-a9d2-f9bb024f6379%2FUntitled.png?table=block&id=be9b4b3d-f14b-4aee-b389-ccfc04f3c860&width=1780&cache=v2)



클래스101 서비스이 앱 마이페이지를 예로 들면,

마이페이지를 들어가면 유저마다 다른 정보를 얻을 수 있습니다. 이는 서버에서 각 유저마다 다른 정보를 내려주고 있다는 걸 의미하죠.

이 때 유저의 개인 정보를 서버에게 요청하기 위해서는 **어디에, 무엇을 요청할지 알아야 합니다.**

그래서 앱은 유저 정보를 제공해주는 API를 이용해야 합니다. 마찬가지로 결제한 클래스의 정보를 얻기 위해선 클래스 정보를 제공해주는 API를 이용해야겠죠? 이 API들은 회사의 서버 개발자가 서버에 개발해놓은 것들이겠구요.



#### API 예시

![API](https://www.grabbing.me/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F641e3651-b4c8-40e1-8a9f-4ab32c48452b%2FUntitled.png?table=block&id=21455e24-30ef-4462-859e-01bf0517f789&width=1440&cache=v2)

<!-- 카카오 로그인 API 예시 -->

보통 웹에서 로그인을 할 때 '카카오 로그인' 기능을 많이 넣습니다. 그러면 클라이언트(개발자)들은 카카오 서버 개발자가 개발한 서버 API를 이용하게 됩니다.

**이 때 카카오 로그인 API 문서를 보면 어디(url) 에 무엇을(Parameter)을 보내면 무슨 응답(Response)을 줄지가 전부 약속되어 있는 것을 확인할 수 있습니다.**

