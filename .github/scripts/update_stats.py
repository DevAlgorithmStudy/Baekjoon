#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from pathlib import Path
from collections import Counter

# 1) 경로 설정
ROOT = Path(__file__).parent.parent.parent
SOLVED_MD = ROOT / "problems" / "solved.md"

# 2) 파싱을 위한 정규 표현식
TABLE_HEADER_PATTERN = re.compile(r"^\|\s*주차\s*\|\s*문제명\s*\|\s*번호\s*\|\s*난이도\s*\|\s*알고리즘\s*\|\s*선정자\s*\|\s*bum\s*\|\s*hano\s*\|\s*jin\s*\|")
TABLE_DIVIDER_PATTERN = re.compile(r"^\|\s*-+")
ROW_PATTERN = re.compile(r"^\|\s*(\d+)\s*\|")  # 주차 열이 숫자로 시작하는 행

# 3) 통계 영역 마커
START_MARKER = "<!-- ACTIONS-STATS:START -->"
END_MARKER   = "<!-- ACTIONS-STATS:END -->"

# 4) 허용 티어 키워드
TIER_KEYWORDS = ["Bronze", "Silver", "Gold", "Platinum"]

def parse_solved_rows():
    """
    solved.md에서 '## 📑 해결한 전체 문제 목록' 아래 표의 각 행을 파싱하여
    리스트 of dict를 반환: 각 dict에는 week, tier 항목이 담겨 있다.
    """
    lines = SOLVED_MD.read_text(encoding="utf-8").splitlines()
    in_table = False
    headers = []
    rows = []

    for line in lines:
        if in_table:
            # 표 구분선(두 번째 줄) 지나면 본격적 데이터 행
            if TABLE_DIVIDER_PATTERN.match(line):
                continue
            if ROW_PATTERN.match(line):
                cols = [c.strip() for c in line.strip().strip("|").split("|")]
                # 컬럼 순서: 주차, 문제명, 번호, 난이도, 알고리즘, 선정자, bum, hano, jin
                # 유효 행인지 확인
                if len(cols) >= 9:
                    week = cols[0]
                    tier = cols[3]
                    rows.append({"week": week, "tier": tier})
                continue
            else:
                # 표가 끝났을 때
                break
        else:
            # 표 헤더 시작 지점 찾기
            if TABLE_HEADER_PATTERN.match(line):
                in_table = True
                continue

    return rows

def compute_statistics(entries):
    """
    entries: parse_solved_rows() 반환값(week, tier 리스트)
    아래 통계를 계산하여 dict로 반환:
    - total_sessions: 고유 주차 수
    - total_problems: 행 개수
    - tier_counts: { 'Bronze': X, 'Silver': X, 'Gold': X, 'Platinum': X }
    """
    weeks = set()
    tier_counter = Counter()

    for e in entries:
        w = e["week"]
        weeks.add(w)

        # tier의 첫 단어(예: 'Silver II' -> 'Silver') 추출
        tier_full = e["tier"]
        tier_key = tier_full.split()[0]
        if tier_key in TIER_KEYWORDS:
            tier_counter[tier_key] += 1

    # Ensure all keys exist
    tier_counts = {k: tier_counter.get(k, 0) for k in TIER_KEYWORDS}

    return {
        "total_sessions": len(weeks),
        "total_problems": len(entries),
        "tier_counts": tier_counts
    }

def regenerate_stats_block():
    """
    solved.md의 기존 통계 영역을 새로운 값으로 교체한다.
    """
    content = SOLVED_MD.read_text(encoding="utf-8")
    entries = parse_solved_rows()
    stats = compute_statistics(entries)

    # 새 통계 텍스트 생성
    new_stats = [
        START_MARKER,
        f"- **총 스터디 횟수**: {stats['total_sessions']}회",
        f"- **총 해결 문제 수**: {stats['total_problems']}개",
        "- **난이도별 분포**: " + ", ".join(
            f"{tier} {stats['tier_counts'][tier]}" for tier in TIER_KEYWORDS
        ),
        "",
        END_MARKER
    ]
    new_stats_block = "\n".join(new_stats)

    # 기존 통계 블록 교체 (START_MARKER ~ END_MARKER 사이)
    pattern = re.compile(
        rf"{re.escape(START_MARKER)}[\s\S]*?{re.escape(END_MARKER)}",
        re.MULTILINE
    )
    updated_content = pattern.sub(new_stats_block, content)

    SOLVED_MD.write_text(updated_content, encoding="utf-8")
    print("✅ solved.md 통계 영역 업데이트 완료.")

if __name__ == "__main__":
    regenerate_stats_block()