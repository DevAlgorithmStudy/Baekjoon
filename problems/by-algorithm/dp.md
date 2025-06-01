# 동적계획법 (Dynamic Programming)

## 📖 개념
동적계획법은 복잡한 문제를 간단한 여러 개의 하위 문제로 나누어 해결하는 기법입니다.

## 🔑 핵심 포인트
- **최적 부분 구조**: 큰 문제의 최적해가 작은 문제들의 최적해로 구성
- **중복 부분 문제**: 동일한 하위 문제가 반복적으로 발생
- **메모이제이션**: 계산 결과를 저장하여 중복 계산 방지

## 📚 해결한 문제들

| 문제명 | 번호 | 난이도 | 주차 | bum | hano | jin |
|--------|------|--------|------|-----|------|-----|
| [[예시 Silver (DP)](https://www.acmicpc.net/problem/11053)](https://www.acmicpc.net/problem/11053) | 11053 | Silver II | 1 | [풀이](https://github.com/B/11053_bum) | [풀이](https://github.com/B/11053_hano) | [풀이](https://github.com/B/11053_jin) |
| [[예시 Gold (DP)](https://www.acmicpc.net/problem/2293)](https://www.acmicpc.net/problem/2293) | 2293 | Gold V | 2 | [풀이](https://github.com/E/2293_bum) | [풀이](https://github.com/E/2293_hano) | [풀이](https://github.com/E/2293_jin) |
| [[예시 잘못된 Tier](https://www.acmicpc.net/problem/9999)](https://www.acmicpc.net/problem/9999) | 9999 | silver I | 3 | [풀이](https://github.com/G/9999_bum) | [풀이](https://github.com/G/9999_hano) | [풀이](https://github.com/G/9999_jin) |
| [[문제B](https://www.acmicpc.net/problem/11053)](https://www.acmicpc.net/problem/11053) | 11053 | Silver II | 5 | [풀이](https://github.com/2) | [풀이](https://github.com/2) | [풀이](https://github.com/2) |
| [[문제D](https://www.acmicpc.net/problem/2293)](https://www.acmicpc.net/problem/2293) | 2293 | Gold V | 6 | [풀이](https://github.com/4) | [풀이](https://github.com/4) | [풀이](https://github.com/4) |
| [[문제2](...)](https://www.acmicpc.net/problem/9992) | 9992 | Gold III | 7 | [풀이](...) | [풀이](...) | [풀이](...) |

## 📝 학습 노트
### 주요 패턴
1. **1차원 배열**: dp[i] = i번째 상태의 최적해
2. **2차원 배열**: dp[i][j] = (i,j) 상태의 최적해
3. **배낭 문제**: 용량 제한이 있는 최적화 문제

### 언어별 특징
- **Java**: 배열 초기화와 메모리 관리 주의
- **Kotlin**: 간결한 문법으로 가독성 좋음
- **Swift**: 옵셔널 처리에 주의