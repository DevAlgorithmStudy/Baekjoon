
# solved.md 작성 가이드라인

`problems/solved.md` 파일은 GitHub Actions 자동 분류 스크립트가 읽어들여야 하는 형식으로 작성해야 합니다.  
아래 내용을 참고하여 **난이도(tier)**와 **알고리즘 이름**을 정확하게 기재해 주세요.

---

## 1. 파일 구조

```markdown
# 스터디 전체 문제 현황

## 📊 통계
- **총 스터디 횟수**: X회
- **총 해결 문제 수**: X개
- **난이도별 분포**: Bronze X, Silver X, Gold X, Platinum X

## 📑 해결한 전체 문제 목록

| 주차 | 문제명 | 번호 | 난이도    | 알고리즘   | 선정자 | bum        | hano       | jin        |
|------|--------|------|----------|-----------|--------|------------|------------|------------|
| 1    | [예시문제](https://www.acmicpc.net/problem/1234) | 1234 | Silver II | DP        | 멤버1 | https://… | https://… | https://… |
| 2    | [숨바꼭질](https://www.acmicpc.net/problem/1697) | 1697 | Silver I  | BFS       | 멤버2 | https://… | https://… | https://… |
| …    | …      | …    | …        | …         | …      | …          | …          | …          |
```

- 반드시 위와 같은 형태로 헤더와 표를 구성해야 합니다.
- **컬럼 순서**는 절대 변경하지 말아 주세요:  
  `주차 | 문제명 | 번호 | 난이도 | 알고리즘 | 선정자 | bum | hano | jin`

---

## 2. 난이도(Tier) 명칭 규칙

1. **첫 단어로 Tier**를 표기합니다.  
   예: `"Bronze V"`, `"Silver II"`, `"Gold I"`, `"Platinum IV"`  
2. **허용되는 Tier 이름** (첫 단어만 검사)  
   - `Bronze`  
   - `Silver`  
   - `Gold`  
   - (추가하려면 스크립트 `TIER_FILES`에 매핑을 추가해야 합니다)  
3. **세부 등급**(II, IV 등)은 공백(스페이스)으로 구분된 두 번째 토큰에 작성.  
   예:  
   - `Silver II`  
   - `Gold IV`  
   - `Bronze III`  
4. 만약 `Tier` 키워드를 정확히 쓰지 않으면 자동 분류가 되지 않습니다.  
   - 잘못된 예: `silverII`, `GoldIV`, `GOLD I` → 스크립트에서 인식 실패  
   - 올바른 예: `Silver II`, `Gold I`

---

## 3. 알고리즘 이름 규칙

자동 분류 스크립트가 인식하는 알고리즘 이름은 다음과 같습니다.  
### 3.1. 허용되는 키워드 (한글/영문 혼용 가능)
| 분류 키워드      | 매핑 파일 (`by-algorithm/`)         |
|------------------|--------------------------------------|
| `DP`             | `dp.md`                              |
| `그리디`         | `greedy.md`                          |
| `Greedy`         | `greedy.md`                          |
| `그래프`         | `bfs-dfs.md`                         |
| `BFS`            | `bfs-dfs.md`                         |
| `DFS`            | `bfs-dfs.md`                         |
| `백트래킹`       | `backtracking.md`                    |
| `Backtracking`   | `backtracking.md`                    |
| `구현`           | `implementation.md`                  |

- 표의 **왼쪽 키워드**(예: `BFS`, `백트래킹`)를 반드시 동일하게 입력해야 자동 분류가 가능합니다.
- 만약 여기에 없는 알고리즘명을 쓰려면, 스크립트 내부 `ALGO_FILES` 딕셔너리에 해당 키와 파일 경로를 추가해야 합니다.
- 키워드와 표기의 **대소문자**는 반드시 일치해야 합니다.  
  - 예: `DP`는 인식되지만 `dp`는 인식되지 않습니다.  
  - 예: `Backtracking`은 인식되지만 `backtracking`은 인식되지 않습니다.

---

## 4. 작성 예시

### 4.1. 올바른 예시

```markdown
| 주차 | 문제명 | 번호 | 난이도     | 알고리즘    | 선정자 | bum                              | hano                             | jin                              |
|------|--------|------|-----------|------------|--------|----------------------------------|----------------------------------|----------------------------------|
| 3    | [N-Queen](https://www.acmicpc.net/problem/9663)   | 9663 | Gold I    | 백트래킹    | 멤버3 | https://github.com/…/9663_bum    | https://github.com/…/9663_hano   | https://github.com/…/9663_jin    |
| 4    | [숨바꼭질](https://www.acmicpc.net/problem/1697)   | 1697 | Silver I  | BFS        | 멤버2 | https://github.com/…/1697_bum    | https://github.com/…/1697_hano   | https://github.com/…/1697_jin    |
| 5    | [동전 1](https://www.acmicpc.net/problem/2293)     | 2293 | Gold V    | DP         | 멤버1 | https://github.com/…/2293_bum    | https://github.com/…/2293_hano   | https://github.com/…/2293_jin    |
```

- `Gold I`, `Silver I`, `Gold V`처럼 **첫 단어** (`Gold` / `Silver`)가 스크립트에서 인식 가능한 Tier 이름이 되어야 합니다.
- `백트래킹`, `BFS`, `DP` 같이 **알고리즘 키워드**도 스크립트에 등록된 키와 정확히 일치해야 합니다.

### 4.2. 잘못된 예시

```markdown
| 주차 | 문제명 | 번호 | 난이도 | 알고리즘 | 선정자 | bum | hano | jin |
|------|--------|------|-------|---------|--------|-----|------|-----|
| 1    | [문제A](...)      | 1000 | SilverII  | dfs       | 멤버1 | …   | …    | …   |
| 2    | [문제B](...)      | 2000 | silver I  | 그리디     | 멤버2 | …   | …    | …   |
| 3    | [문제C](…)       | 3000 | GoldIV    | Backtracking | 멤버3 | …   | …    | …   |
```

- `SilverII` → **띄어쓰기 미삽입**, 스크립트에서 `Silver`만 인식 → 분류 실패  
- `silver I` → 소문자(`silver`) → 인식 실패  
- `GoldIV` → 띄어쓰기 미삽입 → 인식 실패  
- `dfs` → 소문자 키워드 → 인식 실패  
- `Backtracking`은 올바른 알고리즘 키지만 위 예시와 같이 다른 오타가 섞이면 문제가 있을 수 있습니다.

---

## 5. 요약

1. **난이도(Tier)**:  
   - 반드시 `Bronze`, `Silver`, `Gold` 등 스크립트에서 인식 가능한 첫 단어 + 공백 + 세부 등급(예: `II`, `V`) 형태로 작성  
2. **알고리즘**:  
   - 스크립트에 등록된 키워드(`DP`, `그리디`, `BFS`, `백트래킹`, `구현` 등) 중 하나를 정확히 작성  
3. **컬럼 순서**:  
   - `주차` → `문제명` → `번호` → `난이도` → `알고리즘` → `선정자` → `bum` → `hano` → `jin` 순서 고정  
4. **오타 및 띄어쓰기**  
   - 모든 키워드는 대소문자·공백·정확한 스펠링을 준수해야 하며,  
   - 잘못 작성된 경우 자동 분류가 누락될 수 있습니다.

위 가이드라인을 준수하여 `problems/solved.md`를 작성하면, GitHub Actions 자동화가 정상적으로 **by-tier/** 및 **by-algorithm/** 분류 파일을 갱신합니다.
