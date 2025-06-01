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

* 반드시 위와 같은 형태로 헤더와 표를 구성해야 합니다.
* **컬럼 순서**는 절대 변경하지 말아 주세요:
  `주차 | 문제명 | 번호 | 난이도 | 알고리즘 | 선정자 | bum | hano | jin`

---

## 2. 난이도(Tier) 명칭 규칙

1. **첫 단어로 Tier**를 표기합니다.
   예: `"Bronze V"`, `"Silver II"`, `"Gold I"`, `"Platinum IV"`
2. **허용되는 Tier 이름** (첫 단어만 검사)

   * `Bronze`
   * `Silver`
   * `Gold`
   * (추가하려면 스크립트 `TIER_FILES`에 매핑을 추가해야 합니다)
3. **세부 등급**(II, IV 등)은 공백(스페이스)으로 구분된 두 번째 토큰에 작성.
   예:

   * `Silver II`
   * `Gold IV`
   * `Bronze III`
4. 만약 `Tier` 키워드를 정확히 쓰지 않으면 자동 분류가 되지 않습니다.

   * 잘못된 예: `silverII`, `GoldIV`, `GOLD I` → 스크립트에서 인식 실패
   * 올바른 예: `Silver II`, `Gold I`

---

## 3. 알고리즘 이름 규칙

자동 분류 스크립트는 **대소문자 구분 없이** 모든 알고리즘 키를 소문자로 변환한 뒤 매핑합니다.
아래 표에 나열된 키워드를 사용하거나, 해당 표에 없는 경우 스크립트 `ALGO_FILES`에 키와 파일 경로를 추가해야 합니다.

### 3.1. 허용되는 키워드 (소문자/한글 혼용 가능)

| 분류 키워드 (소문자 기준) | 매핑 파일 (`by-algorithm/`) |
| --------------- | ----------------------- |
| `dp`            | `dp.md`                 |
| `그리디`           | `greedy.md`             |
| `greedy`        | `greedy.md`             |
| `그래프`           | `bfs-dfs.md`            |
| `bfs`           | `bfs-dfs.md`            |
| `dfs`           | `bfs-dfs.md`            |
| `백트래킹`          | `backtracking.md`       |
| `backtracking`  | `backtracking.md`       |
| `구현`            | `implementation.md`     |

* `solved.md`에 입력할 때는 대소문자 구분 없이, 위 표에서 소문자 또는 한글로 쓰면 자동 분류가 가능합니다.
  예:

  * `DP`, `dp`, `Dp` 모두 **소문자화**하여 `dp`로 인식 → `dp.md`로 분류
  * `BackTracking`, `백트래킹`, `backtracking` → 소문자화된 `backtracking` → `backtracking.md`로 분류
* 만약 표에 없는 알고리즘명을 쓰려면, 스크립트 내부 `ALGO_FILES` 딕셔너리에 해당 키(소문자 형태)와 파일 경로를 추가해야 합니다.

---

## 4. 작성 예시

### 4.1. 올바른 예시

```markdown
| 주차 | 문제명 | 번호 | 난이도     | 알고리즘   | 선정자 | bum                              | hano                             | jin                              |
|------|--------|------|-----------|------------|--------|----------------------------------|----------------------------------|----------------------------------|
| 3    | [N-Queen](https://www.acmicpc.net/problem/9663)   | 9663 | Gold I    | 백트래킹    | 멤버3 | https://github.com/…/9663_bum    | https://github.com/…/9663_hano   | https://github.com/…/9663_jin    |
| 4    | [숨바꼭질](https://www.acmicpc.net/problem/1697)   | 1697 | Silver I  | BFS        | 멤버2 | https://github.com/…/1697_bum    | https://github.com/…/1697_hano   | https://github.com/…/1697_jin    |
| 5    | [동전 1](https://www.acmicpc.net/problem/2293)     | 2293 | Gold V    | DP         | 멤버1 | https://github.com/…/2293_bum    | https://github.com/…/2293_hano   | https://github.com/…/2293_jin    |
```

* 알고리즘 칸에 예를 들어 `DP`, `dp`, 또는 `Dp`를 입력해도 모두 `dp.md`로 분류됩니다.
* `백트래킹`이나 `Backtracking`을 입력해도 모두 `backtracking.md`로 분류됩니다.

### 4.2. 잘못된 예시

```markdown
| 주차 | 문제명 | 번호 | 난이도 | 알고리즘 | 선정자 | bum | hano | jin |
|------|--------|------|-------|---------|--------|-----|------|-----|
| 1    | [문제A](...)      | 1000 | SilverII | dfs       | 멤버1 | …   | …    | …   |
| 2    | [문제B](...)      | 2000 | silver I  | 그리디     | 멤버2 | …   | …    | …   |
| 3    | [문제C](…)       | 3000 | GoldIV    | Backtracking | 멤버3 | …   | …    | …   |
```

* `SilverII` → 띄어쓰기 미삽입 → 인식 실패
* `silver I` → 소문자로 시작 → 대소문자 구분 없이 `.lower()` 처리하더라도 `silver`는 맞으나 `I`가 정상 인식되려면 공백 필요 (→ `Silver I`)
* `GoldIV` → 띄어쓰기 미삽입 → 인식 실패
* `Backtracking`은 키워드 목록에 있지만, 위 예시에서는 맞으나 다른 오타가 섞여 있으면 인식 실패 가능

---

## 5. 요약

1. **난이도(Tier)**:

   * 반드시 `Bronze`, `Silver`, `Gold` 등 스크립트에서 인식 가능한 첫 단어 + 공백 + 세부 등급(예: `II`, `V`) 형태로 작성
2. **알고리즘**:

   * 키워드는 **대소문자 구분 없이 모두 소문자화**되어 인식합니다.
   * 예를 들어 `dp`, `DP`, `Dp` 모두 정상 인식 → `dp.md`
   * 한글 키워드(`그리디`, `백트래킹`, `구현`)도 그대로 사용
   * 스크립트에 등록되지 않은 알고리즘은 `ALGO_FILES`에 소문자 키로 추가 필요
3. **컬럼 순서**:

   * `주차` → `문제명` → `번호` → `난이도` → `알고리즘` → `선정자` → `bum` → `hano` → `jin` 순서 고정
4. **오타 및 띄어쓰기**

   * `SilverII`, `GoldIV`처럼 붙여 쓰면 인식 실패
   * 알고리즘 키는 모두 소문자 혹은 한글로 작성하거나, 대소문자를 혼용해도 `.lower()` 처리가 되므로 정상 인식됨

위 가이드라인을 준수하여 `problems/solved.md`를 작성하면, GitHub Actions 자동화가 정상적으로 **by-tier/** 및 **by-algorithm/** 분류 파일을 갱신합니다.
