# 그리디 (Greedy)

## 📖 개념
그리디 알고리즘은 현재 상황에서 가장 좋아 보이는 선택을 하는 방식으로 최적의 해답을 찾아가는 알고리즘입니다.

## 🔑 핵심 포인트
- **탐욕적 선택 속성**: 부분 문제에 대한 최적해가 전체 문제의 최적해를 이룸
- **정렬 기반 접근**이 많음
- 항상 **전역 최적해**를 보장하지는 않음 → 문제 조건에 따라 유효성 확인 필수

## 📚 해결한 문제들

| 문제명 | 번호 | 난이도 | 주차 | bum | hano | jin |
|--------|------|--------|------|-----|------|-----|
| [멀티탭 스케줄링](https://www.acmicpc.net/problem/1700) | 1700 | Silver II | 2 | [풀이](https://github.com/D/1700) | [풀이](https://github.com/D/1700) | [풀이](https://github.com/D/1700) |
| [감소하는 수](https://www.acmicpc.net/problem/1038) | 1038 | Silver V | 5 | [풀이](https://github.com/I/1038) | [풀이](https://github.com/I/1038) | [풀이](https://github.com/I/1038) |
| [나무 자르기](https://www.acmicpc.net/problem/2805) | 2805 | Gold III | 5 | [풀이](https://github.com/J/2805) | [풀이](https://github.com/J/2805) | [풀이](https://github.com/J/2805) |

## 📝 학습 노트
### 주요 패턴
1. **정렬 후 선택**: 기준을 정한 뒤 정렬하고 앞에서부터 선택
2. **탐욕적 조건 증명** 필요: 항상 최적의 해를 보장하는가?
3. **Counter-example 분석**: Greedy가 실패하는 경우도 연습

### 언어별 특징
- **Java**: `Comparator` 커스터마이징을 자주 사용
- **Kotlin**: `sortedBy`, `maxBy` 등 유용한 정렬 함수 풍부
- **Swift**: `sorted { $0 < $1 }` 문법 활용