# 프로젝트 Description

## 프로젝트 목표

- 트래블월렛의 트래블페이 충전 시 환전할 통화 입력-페이지 이동 과정을 자동화하여 반복 테스트를 용이하게 할 것.
- 단순한 click 액션 뿐만 아니라 실제 검색 결과에서 통화 충전 화면으로 이동하여 검색어가 포함되어 있는지 확인하는 과정도 추가하여 logging 할 것.

## 테스트 상세 과정

### 검색 수행

- 메인 화면 → 검색 화면으로 이동
- 검색창에 search_keyword 입력
- 검색 결과 중 search_keyword와 일치하는 element 클릭

### 충전 통화 이름 확인

- 통화 충전 화면에 search_keyword가 포함되어 있는지 확인
- 통화 충전 화면 → 검색 화면으로 이동
- 검색 화면 → 메인 화면으로 이동

## 테스트 환경

- 자동화 도구: Appium 2.5.0
- 작성 언어: Python
- 테스트 대상: iOS