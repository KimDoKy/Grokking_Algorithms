# chap4. 퀵 정렬

## 분할 정복
문제를 분할 정복 전략으로 풀기 위한 단계
1. 가장 간단한 경우로 기본 단계를 찾음
2. 주어진 문제를 작게 줄여서 기본 단계가 되도록 만듬

#### 유클리드 알고르즘
[유클리드 호제법](https://ko.wikipedia.org/wiki/%EC%9C%A0%ED%81%B4%EB%A6%AC%EB%93%9C_%ED%98%B8%EC%A0%9C%EB%B2%95)

#### 함수형 프로그래밍
재귀는 함수형 프로그래밍의 방법이다. 하스켈과 같은 함수형 프로그래밍 언어는 반복문이 없다. 무조건 재귀를 사용해야만 한다. 재귀를 잘 이해하고 있다면 함수형 언어를 익히기 쉽다.

## 퀵 정렬
퀵 정렬은 정렬 알고리즘임. 선택 정렬보다 훨씬 빠르고 자주 사용됨.

#### 귀납적 증명
귀납적 증명은 제대로 동작하는지 증명하는 방법 중 하나.  
기본 단계와 귀납 단계라는 두 단계가 필요.
기본 단계에서 알고리즘이 가장 기본적인 경우, 즉 배열의 크기가 0이나 1인 경우에 대해 알고리즘이 동작한다면 크기가 2, 3인 배열에서도 동작하고, 이렇게 모든 크기의 배열에 대해 퀵 정렬이 동작한다는 증명.

## 빅오 표기법 복습
### 병합 정렬과 퀵 정렬 비교
빅오 표기법에서는 상수는 무시되지만, 퀵 정렬과 병합 정렬은 예외.  
퀵 정렬이 병합 정렬보다 더 작은 상수를 가진다. 그래서 실행 시간이 O(n log n)으로 동일하다면 퀵 정렬이 더 빠르다. 그리고 퀵 정렬을 사용할 때 최악의 경우보다는 일반적인 경우가 훨씬 더 많기 때문에 현실에서는 퀵 정렬이 더 빠르다.

### 평균적인 경우와 최악의 경우 비교
기준 원소에 따라 달라짐.  
기준 원소를 전체 배열에서 무작위로 선택한다면 평균적으로 퀵 정렬은 O(n log n) 실행 시간을 가짐.  
가장 빠른 정렬 방법 중 하나이고, 분할 정복의 좋은 예.

---

- 분할 정복은 문제를 더 작은 조각으로 나누어 품. 만약 리스트에 분할 정복을 적용하면 기본 단계는 원소가 없는 빈 배열이거나 하나의 원소만 가진 배열이 된다.
- 퀵 정렬을 구현하려면 기준 원소를 무작위로 선택한다. 퀵 정렬의 평균적인 실행 시간은 O(n log n).
- 빅오 표기법에서 가끔씩 상수가 중요할 때가 있음. 퀵 정렬이 병합 정렬보다 빠른 이유이기도 함
- 단순 탐색과 이진 탐색을 비교할 때는 상수항이 전혀 문제가 되지 않음. 리스트가 길어지면 O(log n)이 O(n)보다 훨씬 빨라지기 때문
