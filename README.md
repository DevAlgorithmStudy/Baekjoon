# 📘 Algorithm Study

알고리즘 문제 해결 능력을 향상시키기 위한 스터디입니다.  
각자의 언어(Java / Kotlin / Swift)로 문제를 풀이하고, 블로그 또는 개인 GitHub 레포에 정리한 후 이 저장소에 링크를 기록합니다.

📌 **본 스터디는 [백준 온라인 저지](https://www.acmicpc.net/) 문제를 기반으로 진행됩니다.**

📌 진행한 스터디 전체 문제 목록은 [`problems/solved.md`](./problems/solved.md)에서 확인할 수 있습니다.


## 🎯 스터디 목표

- 다양한 알고리즘 문제를 유형별로 학습
- 각자의 언어 특성에 맞는 풀이 연습
- 서로의 풀이 방식 공유 및 토론을 통한 사고 확장
- 꾸준한 기록 습관 형성


## 🧑‍💻 참여 멤버

| 이름 | 언어 | 블로그 / GitHub |
|------|------|------------------|
| [bum](https://github.com/ByeongbumSeo) | Java | [블로그](https://byeongbumseo.github.io/) |
| [jin](https://github.com/dhjin1125) | Kotlin | [GitHub](https://github.com/dhjin1125) |
| [hano](https://github.com/Glsme) | Swift | [GitHub](https://github.com/Glsme) |

> 개인별 자세한 소개는 [`members/`](./members/) 디렉토리에서 확인 가능합니다.


## ⏱️ 진행 방식

1. **주 1회** 문제 선정 및 풀이
2. 개인 블로그 or GitHub에 풀이 및 설명 업로드
3. `members/` 경로의 각자 주차별 파일(`week-xx.md`)에 링크 정리
4. `problems/` 경로에서 알고리즘 분류 및 티어 분류 정리


## 🗂️ 디렉토리 구조

```
Baekjoon/
├── README.md                  # 스터디 개요
├── docs/
│   └── study-rules.md         # 스터디 진행 규칙
├── members/
│   ├── member1/
│   │   ├── profile.md         # 멤버 소개 및 블로그/깃허브 링크
│   │   └── weekly/            # 주차별 학습 기록
│   │       ├── week-01.md
│   │       └── …
│   └── …
├── problems/
│   ├── solved.md              # 해결한 전체 문제 목록
│   ├── by-tier/               # 티어별 분류
│   │   ├── bronze.md
│   │   ├── silver.md
│   │   └── gold.md
│   └── by-algorithm/          # 알고리즘 유형별 분류
│       ├── dp.md
│       ├── greedy.md
│       ├── bfs-dfs.md
│       ├── backtracking.md
│       └── …
├── template/
│   └── weekly-template.md     # 주차별 개인 학습 기록 마크다운 템플릿
```


## 📄 스터디 규칙

스터디 참여와 운영 방식에 대한 세부 규칙은 👉 [`docs/study-rules.md`](./docs/study-rules.md) 문서를 참고해주세요.

- 주차별 문제 수, 선정 방식
- PR 작성 형식
- 커밋 및 디렉토리 구조 가이드
- 벌칙 및 보상 조건 등

스터디 운영에 필요한 모든 규칙이 정리되어 있습니다.


## 📝 solved.md 작성 가이드

`problems/solved.md` 파일은 스터디 전체 문제 목록을 정리하는 메인 테이블입니다.  
이 테이블은 GitHub Actions에 의해 자동 분류되어 `by-tier/`, `by-algorithm/` 디렉토리에 반영되므로, 반드시 **작성 규칙](./docs/solved-guideline.md)**을 준수해야 합니다.

- 각 문제는 문제명, 번호, 난이도(Tier), 알고리즘 유형, 선정자, 개인별 풀이 링크를 포함해야 하며
- Tier는 `Gold I`, `Silver II` 등과 같이 정확한 대소문자와 공백으로 표기되어야 하고
- 알고리즘은 `DP`, `BFS`, `백트래킹`, `구현` 등 사전에 정의된 키워드로만 작성해야 합니다.

자세한 규칙은 👉 [`docs/solved-guideline.md`](./docs/solved-guideline.md)에서 확인할 수 있습니다.
