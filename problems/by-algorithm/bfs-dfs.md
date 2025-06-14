# BFS / DFS (너비우선탐색 / 깊이우선탐색)

## 📖 개념
BFS와 DFS는 그래프 탐색 기법으로, 각각 큐와 스택을 기반으로 탐색 순서가 달라집니다.

## 🔑 핵심 포인트
- **BFS (Breadth-First Search)**: 가까운 노드부터 탐색 (큐)
- **DFS (Depth-First Search)**: 깊은 노드부터 탐색 (재귀 or 스택)
- **방문 체크 배열** 필수
- **미로 탐색**, **최단거리 문제**, **연결 요소 탐색**에 많이 사용됨

## 📚 해결한 문제들

| 문제명 | 번호 | 난이도 | 주차 | bum | hano | jin |
|--------|------|--------|------|-----|------|-----|
| [숨바꼭질](https://www.acmicpc.net/problem/1697) | 1697 | Silver I | 2 | [풀이](https://github.com/C/1697) | [풀이](https://github.com/C/1697) | [풀이](https://github.com/C/1697) |
| [줄세우기](https://www.acmicpc.net/problem/2252) | 2252 | Gold II | 4 | [풀이](https://github.com/G/2252) | [풀이](https://github.com/G/2252) | [풀이](https://github.com/G/2252) |

## 📝 학습 노트
### 주요 패턴
1. **BFS → 최단 거리**: 거리 배열 추가
2. **DFS → 조합 탐색**: 백트래킹과도 연계됨
3. **방문 처리 위치 주의**: 함수 호출 시 or 조건 만족 시 처리 여부

### 언어별 특징
- **Java**: `Queue`, `Stack`, `LinkedList` 자료구조 사용
- **Kotlin**: `mutableListOf`, `ArrayDeque`로 큐 처리
- **Swift**: `Array`, `Set`으로 구현 → 자료구조 최적화 필요