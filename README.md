# **🍕Yammm**


### 한 줄 소개✅

&nbsp;&nbsp;&nbsp;&nbsp;`오직 당신만을 위한 영양사, Yammm을 만나보세요!`


### 프로젝트 소개

- 서구화된 식단, 배달 서비스의 발전으로 맛있는 음식을 접하기는 쉽지만, 맛있고 **건강한** 음식을 접하기는 어려워지고 있습니다.🥲 

    따라서 **🍕yammm**은 **사용자의 기존 식단을 분석**하여 부족한 점을 찾아낸 후 상황에 맞는 **음식을 추천**하고, 이를 통해 더 나은 내일을 만들 수 있도록 도와줍니다.



### 프로젝트 목표🚩

- 유저가 먹은 음식 사진을 업로드하면 이미지 처리 딥러닝 모델을 통해 **어떤 성분과 영양소가 들어가 있는지 분석**하여 유저에게 알려줍니다.

- 부족한 영양소를 채울 수 있는 **식단을 제안**하여 식습관 개선을 통한 **건강 관리**를 할 수 있는 서비스를 제공합니다.

---

### 팀 구성원의 이름과 역할

| <center>이름</center> | <center>역할</center> | <center>담당</center> |
|:----:|:----:|:----|
| 🐯 **서민정** | 팀장, AI |AI 모델 설계, 모델 함수화|
| 🦊 **이상은** | AI |AI 모델 설계, 모델 테스트 후 성능 향상|
| 🐳 **박진호** | Frontend |와이어프레임 제작, 로그인, 게시판, 오늘 먹은 음식, 캘린더 페이지 제작|
| 🥸 **오정진** | Frontend |와이어프레임 제작, 메인 기능, 오늘 먹은 음식, 인트로 페이지 제작|
| 🦈 **최성호** | Backend |메인 기능, DB 설계, API 설계, 서버 배포|
| 🐴 **홍의** | Backend |서브 기능, DB 설계, API 설계|


---
### 프로젝트 주요 기능🧩

- 식단에서 **부족한 영양소**가 어떤 것인지 알려줍니다. → 해당 정보를 바탕으로 다음 식사 **메뉴 추천**
- 유저가 업로드한 음식 **사진의 정보**를 나타냅니다.
- 유저가 **선택한 날짜별 단위**로 먹은 음식 정보를 알려줍니다.


### 프로젝트 세부 기능🏁

- **회원가입**과 **로그인**이 가능합니다.
- **아이디**와 **비밀번호**를 찾을 수 있습니다.
- 날짜별로 유저가 먹은 음식 정보 표시하는 **식단 일지**를 작성할 수 있습니다.
- 유저들이 사진과 함께 짧은 메모를 남길 수 있는 **커뮤니티** 기능을 지원합니다.

##### 추가 기능🏴
- 커뮤니티에 업로드된 타인의 게시물에 **반응**을 남길 수 있습니다.
- 오늘 먹었던 요리의 **레시피**에 대한 정보를 유튜브로 제공합니다.


---

### 프로젝트 와이어프레임🕸️

https://www.figma.com/file/GeoBbvBydetHv1MXmX731a?embed_host=notion&kind=&node-id=37%3A82&viewer=1

---

### 데이터셋💾

[음식 이미지 및 영양정보 텍스트](https://aihub.or.kr/aidata/30747) : **AI Hub**

---

### 기술 스택✨

- **AI**   
1. <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white"> 

2. <img src="https://img.shields.io/badge/Pytorch-EE4C2C?style=for-the-badge&logo=Pytorch&logoColor=white"> 딥러닝 구현 -> YOLOV3 : 여러 개의 이미지 동시에 빠르게 처리 가능


- **Frontend**  
1. <img src="https://img.shields.io/badge/React-33FFF2?style=for-the-badge&logo=React&logoColor=white"> 
2. <img src="https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=Next.js&logoColor=white"> 
3. <img src="https://img.shields.io/badge/Redux-D333DE?style=for-the-badge&logo=Redux&logoColor=white"> 
4. <img src="https://img.shields.io/badge/Tailwind CSS-31C491?style=for-the-badge&logo=Tailwind CSS&logoColor=white">

- **Backend**   
1. <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=Django&logoColor=white"> -> Django REST framework 사용 : Restful API 개발에 용이
2. <img src="https://img.shields.io/badge/Uwsgi-C5EDB0?style=for-the-badge&logo=Uwsgi&logoColor=white">  
3. <img src="https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=Nginx&logoColor=white">  
4. <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=SQLite&logoColor=white"> : mysql과 유사한 데이터베이스 관리 시스템으로, 간편하고 가볍다는 장점이 있음


---

### 프로젝트 구조도
![image](uploads/709d3964cda1abdd6ab5b4ef27c8c538/image.png)

---

### 서비스 구조도
![image](uploads/03036aaa810e7318ba09adb726406d85/image.png)


---
