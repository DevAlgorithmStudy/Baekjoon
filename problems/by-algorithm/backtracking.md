# 백트래킹 (Backtracking)

## 📖 개념
백트래킹은 가능한 모든 경우를 탐색하되, 유망하지 않은 경우를 미리 가지치기하는 기법입니다.

## 🔑 핵심 포인트
- **DFS 기반**의 완전 탐색
- 조건을 만족하지 않으면 **백트랙 (되돌아가기)**
- **가지치기 (Pruning)** 기법 중요
- **N과 M 문제 시리즈**, **조합/순열 문제**에서 자주 등장

## 📚 해결한 문제들

| 문제명 | 번호 | 난이도 | 주차 | bum | hano | jin |
|--------|------|--------|------|-----|------|-----|
| [평균](https://www.acmicpc.net/problem/1546) | 1546 | Bronze V | 1 | [풀이](https://github.com/B/1546) | [풀이](https://github.com/B/1546) | [풀이](https://github.com/B/1546) |
| [N-Queen](https://www.acmicpc.net/problem/9663) | 9663 | Gold I | 3 | [풀이](https://github.com/F/9663) | [풀이](https://github.com/F/9663) | [풀이](https://github.com/F/9663) |

## 📝 학습 노트
### 주요 패턴
1. **함수 내 반복문** → 재귀적 탐색 구조
2. **조건 만족 안 하면 return** → 가지치기
3. **결과 배열 or StringBuilder 활용**

### 언어별 특징
- **Java**: 문자열 + 방문 체크 배열 조합 자주 사용
- **Kotlin**: `StringBuilder`, 람다 표현식으로 간결
- **Swift**: 재귀 구조에서 클로저와 value 타입 변수 주의