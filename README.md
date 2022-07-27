# 딥러닝을 이용한 패션 스타일 분류

## 프로젝트 목표
* 사용자의 패션 이미지를 입력 받아 어떤 스타일인지 분류하여 알려주는 서비스

## 데이터
![111](https://user-images.githubusercontent.com/86766081/175889300-bf295912-107c-443c-99e8-e3c95ce11ed8.png)
* 무신사 홈페이지 → 스타일 → 코디숍 에서 약 23,000개의 이미지를 수집
    * https://www.musinsa.com/app/styles/lists
* 이미지별 스타일(캐주얼, 스트릿 등)을 라벨로 하여 저장

![222](https://user-images.githubusercontent.com/86766081/175889933-3436a6ad-0eee-46ef-9c25-a53d00c05452.png)

※ 총 12개의 스타일 종류 중 이미지 개수가 너무 적은 스타일을 제거 후 총 7개의 스타일로 분류  
(걸리시, 댄디, 로맨틱, 스트릿, 스포츠, 캐주얼, 포멀)

## 데이터 파이프라인
![pipe](https://user-images.githubusercontent.com/86766081/176106803-f7f6bc3b-54a6-449e-8972-af651dc0a5e4.png)


* Selenium을 이용한 동적 웹 크롤링으로 이미지를 로컬에 저장
* Tensorflow와 Pytorch를 이용하여 CNN, EfficientNetB0 모델링(진행중)
* Flask를 이용해 웹 제작 예정
