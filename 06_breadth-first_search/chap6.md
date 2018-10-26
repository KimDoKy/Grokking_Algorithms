# chap6. 너비 우선 탐색(breadth-first_search)

## 그래프의 소개
#### 그래프란 무엇인가

## 너비 우선 탐색
#### 최단 경로 찾기
#### 큐

## 그래프의 구현

## 알고리즘의 구현
- 푸시는 삽입과 거의 같은 의미이고, 팝은 삭제와 거의 같은 의미

#### 실행 시간

---

- 너비 우선 탐색은 A에서 B로 가는 경로가 있는지 알려줌
- 만약 경로가 존재한다면 최단 경로를 찾아줌
- 만약 X까지의 최단 경로를 찾는 문제가 있다면 그 문제를 그래프로 모형화하고 너비 우선 탐색으로 문제를 품
- 방향 그래프는 화살표를 가지며, 화살표 방향으로 관계를 가짐(rama -> adit는 rama가 adit에게 돈을 빚지고 있다는 뜻)
- 무방향 그래프는 화살표가 없고, 둘 간의 상호 관계를 나타냄(ross-rachel 은 ross가 rachel과 서로 데이트했다는 뜻)
- 큐는 선입선출
- 스택은 후입선출
- 탐색 목록에 추가된 순서대로 사람을 확인해야 함. 그래서 탐색 목록은 큐가 되어야 함. 그렇지 않으면 최단 경로를 구할 수 없음
- 누군가를 확인한 다음 두번 다시 확인하지 않도록 해야 함. 안그러면 무한 반복이 됨