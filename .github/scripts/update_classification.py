#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from pathlib import Path
from collections import defaultdict

# 1) 경로 설정 (레포지토리 루트)
ROOT = Path(__file__).parent.parent.parent
SOLVED_MD = ROOT / "problems" / "solved.md"
BY_TIER_DIR = ROOT / "problems" / "by-tier"
BY_ALGO_DIR = ROOT / "problems" / "by-algorithm"

# 2) 매핑 정의 (모두 소문자 key 기준)
TIER_FILES = {
    "bronze": BY_TIER_DIR / "bronze.md",
    "silver": BY_TIER_DIR / "silver.md",
    "gold":   BY_TIER_DIR / "gold.md",
    # platinum 등 추가 시 "platinum": BY_TIER_DIR/"platinum.md" 등으로 확장
}

# 알고리즘 이름(KEY, 소문자로 변환)과 파일 경로(MD)를 매핑
# (모두 소문자 키 → 대응 파일)
ALGO_FILES = {
    "dp":            BY_ALGO_DIR / "dp.md",
    "그리디":          BY_ALGO_DIR / "greedy.md",
    "greedy":        BY_ALGO_DIR / "greedy.md",
    "그래프":          BY_ALGO_DIR / "bfs-dfs.md",
    "bfs":           BY_ALGO_DIR / "bfs-dfs.md",
    "dfs":           BY_ALGO_DIR / "bfs-dfs.md",
    "백트래킹":        BY_ALGO_DIR / "backtracking.md",
    "backtracking":  BY_ALGO_DIR / "backtracking.md",
    "구현":           BY_ALGO_DIR / "implementation.md",
    # 필요 시 여기에 소문자 키:경로를 추가
}

# 3) solved.md의 표를 파싱
def parse_solved_entries():
    """
    '## 📑 해결한 전체 문제 목록' 표 아래 각 행을 추출하여
    리스트 of dict로 반환.
    각 dict: week, name, number, tier, algo, solver, bum, hano, jin
    """
    if not SOLVED_MD.exists():
        print(f"Error: {SOLVED_MD} 파일을 찾을 수 없습니다.")
        return []

    text = SOLVED_MD.read_text(encoding="utf-8").splitlines()
    in_table = False
    headers = []
    entries = []

    for line in text:
        # '주차' 로 시작하고 'jin' 컬럼이 있는 헤더 발견 시 표 진입
        if line.strip().startswith("| 주차") and "jin" in line:
            in_table = True
            headers = [h.strip() for h in line.strip().strip("|").split("|")]
            continue

        # 헤더 바로 다음 구분선 무시
        if in_table and re.match(r"^\|\s*-+", line):
            continue

        if in_table:
            # 데이터 행(‘| 숫자 | ... |’) 감지
            if line.strip().startswith("|"):
                cols = [c.strip() for c in line.strip().strip("|").split("|")]
                if len(cols) < len(headers):
                    continue  # 형식이 맞지 않으면 스킵
                data = dict(zip(headers, cols))
                entries.append({
                    "week":    data.get("주차", ""),
                    "name":    data.get("문제명", ""),
                    "number":  data.get("번호", ""),
                    "tier":    data.get("난이도", ""),
                    "algo":    data.get("알고리즘", ""),
                    "solver":  data.get("선정자", ""),
                    "bum":     data.get("bum", ""),
                    "hano":    data.get("hano", ""),
                    "jin":     data.get("jin", ""),
                })
                continue
            else:
                # 표가 끝나면 파싱 종료
                break

    return entries


def extract_plain_name(markdown_link: str) -> str:
    """
    "[문제명](url)" 형태에서 '문제명'만 추출.
    만약 순수 텍스트(링크 없는)면 그대로 반환.
    """
    match = re.match(r"\[(.*?)\]", markdown_link)
    return match.group(1) if match else markdown_link


# 4) by-tier 파일 갱신
def update_tier_file(tier_name_lower, entries):
    """
    tier_name_lower: "bronze", "silver", "gold" (모두 소문자)
    entries 중 해당 tier를 가진 것만 골라 problems/by-tier/{tier}.md 갱신
    """
    target_path = TIER_FILES[tier_name_lower]
    if not target_path.exists():
        print(f"⚠️ {tier_name_lower} 파일이 존재하지 않아 건너뜁니다: {target_path}")
        return

    # 'Bronze V' → split()[0].lower() == 'bronze'
    filtered = [
        e for e in entries
        if e["tier"].split()[0].lower() == tier_name_lower
    ]

    lines = target_path.read_text(encoding="utf-8").splitlines()

    # '## 📚 해결한 문제들' 섹션 인덱스
    start_idx = next(
        (i for i, l in enumerate(lines) if l.strip().startswith("## 📚 해결한 문제들")),
        None
    )
    if start_idx is None:
        print(f"⚠️ {tier_name_lower} 파일에 '## 📚 해결한 문제들' 섹션이 없어 건너뜁니다.")
        return

    # 새로운 테이블 생성
    new_table = []
    new_table.append("| 문제명 | 번호 | 주차 | bum | hano | jin | 알고리즘 |")
    new_table.append("|--------|------|------|-----|------|-----|------|")
    for e in filtered:
        plain_name = extract_plain_name(e["name"])
        link       = f"[{plain_name}](https://www.acmicpc.net/problem/{e['number']})"
        bum_cell   = e["bum"]  if e["bum"]  else "-"
        hano_cell  = e["hano"] if e["hano"] else "-"
        jin_cell   = e["jin"]  if e["jin"]  else "-"
        algo_cell  = e["algo"]
        row = f"| {link} | {e['number']} | {e['week']} | {bum_cell} | {hano_cell} | {jin_cell} | {algo_cell} |"
        new_table.append(row)

    # 기존 테이블 영역 제거
    end_idx = start_idx + 1
    for i in range(start_idx + 1, len(lines)):
        if lines[i].strip().startswith("## "):
            break
        end_idx += 1

    lines_before = lines[: start_idx + 1]
    lines_after  = lines[end_idx:]

    updated = lines_before + [""] + new_table + [""] + lines_after
    target_path.write_text("\n".join(updated), encoding="utf-8")
    print(f"✅ {tier_name_lower} 테이블 업데이트 완료.")


# 5) by-algorithm 파일 갱신 (케이스-인센시티브, 그룹화)
def update_algo_files(entries):
    """
    동일 파일(bfs-dfs.md 등)에 매핑된 여러 키(“bfs”, “dfs”, “그래프”)를
    한 번에 그룹화하여, 해당 파일을 단 한 번만 덮어씁니다.
    """

    # 5-1) “파일 → (연관된 알고리즘 키 목록)” 역매핑 생성
    file_to_keys = defaultdict(list)
    for key, path in ALGO_FILES.items():
        file_to_keys[path].append(key)

    # 5-2) 각 파일별로 필터링된 entries를 한 번만 처리
    for file_path, keys in file_to_keys.items():
        if not file_path.exists():
            print(f"⚠️ 파일이 존재하지 않아 건너뜁니다: {file_path}")
            continue

        # entries 중 e["algo"].lower()가 keys 리스트(소문자/한글 키)와 일치하는 것만 필터
        filtered = [
            e for e in entries
            if e["algo"].strip().lower() in [k.lower() for k in keys]
        ]

        # 파일 내용 읽기
        lines = file_path.read_text(encoding="utf-8").splitlines()

        # '## 📚 해결한 문제들' 섹션 인덱스
        start_idx = next(
            (i for i, l in enumerate(lines) if l.strip().startswith("## 📚 해결한 문제들")),
            None
        )
        if start_idx is None:
            print(f"⚠️ {file_path.name}에 '## 📚 해결한 문제들' 섹션이 없어 건너뜁니다.")
            continue

        # 새 테이블 생성
        new_table = []
        new_table.append("| 문제명 | 번호 | 난이도 | 주차 | bum | hano | jin |")
        new_table.append("|--------|------|--------|------|-----|------|-----|")
        for e in filtered:
            plain_name = extract_plain_name(e["name"])
            link       = f"[{plain_name}](https://www.acmicpc.net/problem/{e['number']})"
            tier_cell  = e["tier"]
            week_cell  = e["week"]
            bum_cell   = e["bum"]  if e["bum"]  else "-"
            hano_cell  = e["hano"] if e["hano"] else "-"
            jin_cell   = e["jin"]  if e["jin"]  else "-"
            row = f"| {link} | {e['number']} | {tier_cell} | {week_cell} | {bum_cell} | {hano_cell} | {jin_cell} |"
            new_table.append(row)

        # 기존 테이블 영역 제거 및 새 테이블 삽입
        end_idx = start_idx + 1
        for i in range(start_idx + 1, len(lines)):
            if lines[i].strip().startswith("## "):
                break
            end_idx += 1

        lines_before = lines[: start_idx + 1]
        lines_after  = lines[end_idx:]

        updated = lines_before + [""] + new_table + [""] + lines_after
        file_path.write_text("\n".join(updated), encoding="utf-8")
        print(f"✅ {file_path.name} 테이블 업데이트 완료.")


def main():
    entries = parse_solved_entries()
    if not entries:
        print("Warning: 해결한 문제 목록을 파싱하지 못했습니다.")
        return

    # 1) by-tier 파일들 갱신 (소문자로 key 접근)
    for tier_lower in TIER_FILES.keys():
        update_tier_file(tier_lower, entries)

    # 2) by-algorithm 파일들 갱신 (그룹화된 키)
    update_algo_files(entries)

    print("✅ 모든 분류 파일 업데이트 완료.")


if __name__ == "__main__":
    main()