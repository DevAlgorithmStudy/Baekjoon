#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from pathlib import Path
from collections import defaultdict

# 1) 경로 설정 (레포지토리 루트로 이동)
ROOT = Path(__file__).parent.parent.parent
SOLVED_MD = ROOT / "problems" / "solved.md"
BY_TIER_DIR = ROOT / "problems" / "by-tier"
BY_ALGO_DIR = ROOT / "problems" / "by-algorithm"

# 2) 매핑 정의
TIER_FILES = {
    "Bronze": BY_TIER_DIR / "bronze.md",
    "Silver": BY_TIER_DIR / "silver.md",
    "Gold": BY_TIER_DIR / "gold.md",
    # Platinum 등 추가 시 여기에 파일 경로를 넣을 것
}

# 알고리즘 이름(KEY)과 파일 경로(MD)를 매핑
ALGO_FILES = {
    "DP": BY_ALGO_DIR / "dp.md",
    "그리디": BY_ALGO_DIR / "greedy.md",
    "Greedy": BY_ALGO_DIR / "greedy.md",
    "그래프": BY_ALGO_DIR / "bfs-dfs.md",
    "BFS": BY_ALGO_DIR / "bfs-dfs.md",
    "DFS": BY_ALGO_DIR / "bfs-dfs.md",
    "백트래킹": BY_ALGO_DIR / "backtracking.md",
    "Backtracking": BY_ALGO_DIR / "backtracking.md",
    "구현": BY_ALGO_DIR / "implementation.md",
    # 필요에 따라 추가하고 싶을 때 여기에 키: 값 형태로 더 추가
}

# 3) solved.md 의 테이블 파싱
def parse_solved_entries():
    """
    problems/solved.md의 '## 📑 해결한 전체 문제 목록' 이하 테이블을 파싱하여
    리스트 of dict 형태로 반환.
    각 dict의 키: week, name, number, tier, algo, solver, bum, hano, jin
    """
    if not SOLVED_MD.exists():
        print(f"Error: {SOLVED_MD} 파일을 찾을 수 없습니다.")
        return []

    text = SOLVED_MD.read_text(encoding="utf-8").splitlines()
    in_table = False
    headers = []
    entries = []

    for line in text:
        # '주차' 로 시작하는 헤더 라인 찾기
        if line.strip().startswith("| 주차") and "jin" in line:
            in_table = True
            headers = [h.strip() for h in line.strip().strip("|").split("|")]
            continue
        # 헤더 바로 다음 구분선(---) 무시
        if in_table and re.match(r"^\|\s*-+", line):
            continue
        if in_table:
            if line.strip().startswith("|"):
                cols = [c.strip() for c in line.strip().strip("|").split("|")]
                if len(cols) < len(headers):
                    continue  # 비어 있거나 형식 불일치 시 무시
                data = dict(zip(headers, cols))
                entries.append({
                    "week": data.get("주차", ""),
                    "name": data.get("문제명", ""),
                    "number": data.get("번호", ""),
                    "tier": data.get("난이도", ""),
                    "algo": data.get("알고리즘", ""),
                    "solver": data.get("선정자", ""),
                    "bum": data.get("bum", ""),
                    "hano": data.get("hano", ""),
                    "jin": data.get("jin", ""),
                })
                continue
            else:
                # 표가 끝나면 중단
                break

    return entries


def extract_plain_name(markdown_link: str) -> str:
    """
    "[문제명](url)" 형태의 문자열에서 '문제명'만 추출.
    markdown_link가 순수 텍스트라면 그대로 반환.
    """
    match = re.match(r"\[(.*?)\]", markdown_link)
    return match.group(1) if match else markdown_link


# 4) by-tier 파일 내 '## 📚 해결한 문제들' 구간 갱신
def update_tier_file(tier_name, entries):
    """
    tier_name 예: 'Bronze', 'Silver', 'Gold'
    해당 티어에 속하는 entries만 골라서,
    problems/by-tier/{tier}.md 파일 내 '## 📚 해결한 문제들' 섹션 테이블을 덮어쓴다.
    """
    target_path = TIER_FILES[tier_name]
    if not target_path.exists():
        print(f"⚠️ {tier_name} 파일이 존재하지 않아 건너뜁니다: {target_path}")
        return

    # 해당 티어에 속한 문제 필터
    tier_key = tier_name  # 'Bronze', 'Silver', 'Gold'
    filtered = [
        e for e in entries
        if e["tier"].split()[0] == tier_key
    ]

    # 기존 파일 읽기 (모두)
    lines = target_path.read_text(encoding="utf-8").splitlines()

    # '## 📚 해결한 문제들' 시작 인덱스 찾기
    start_idx = next(
        (i for i, l in enumerate(lines) if l.strip().startswith("## 📚 해결한 문제들")),
        None
    )
    if start_idx is None:
        print(f"⚠️ {tier_name} 파일에 '## 📚 해결한 문제들' 섹션이 없어 건너뜁니다.")
        return

    # 테이블을 덮어쓸 새로운 라인 생성
    new_table = []
    new_table.append("| 문제명 | 번호 | 주차 | bum | hano | jin | 알고리즘 |")
    new_table.append("|--------|------|------|-----|------|-----|------|")
    for e in filtered:
        name_text = extract_plain_name(e["name"])
        link = f"[{name_text}](https://www.acmicpc.net/problem/{e['number']})"
        bum_cell = e["bum"] if e["bum"] else "-"
        hano_cell = e["hano"] if e["hano"] else "-"
        jin_cell = e["jin"] if e["jin"] else "-"
        algo_cell = e["algo"]
        row = f"| {link} | {e['number']} | {e['week']} | {bum_cell} | {hano_cell} | {jin_cell} | {algo_cell} |"
        new_table.append(row)

    # 기존 내용에서 테이블 부분 제거 (start_idx부터 테이블 마지막까지)
    end_idx = start_idx + 1
    for i in range(start_idx + 1, len(lines)):
        if lines[i].strip().startswith("## "):
            break
        end_idx += 1

    lines_before = lines[: start_idx + 1]
    lines_after = lines[end_idx:]

    updated = lines_before + [""] + new_table + [""] + lines_after
    target_path.write_text("\n".join(updated), encoding="utf-8")
    print(f"✅ {tier_name} 테이블 업데이트 완료.")


# 5) by-algorithm 파일 내 '## 📚 해결한 문제들' 구간 갱신
def update_algo_files(entries):
    """
    모든 알고리즘 파일을 한 번에 갱신.
    동일한 출력 파일을 가리키는 여러 알고리즘 키를 그룹화하여,
    파일당 한 번만 테이블을 덮어쓴다.
    """
    # 5-1) 파일별 키 목록 생성 (역매핑)
    file_to_keys = defaultdict(list)
    for key, path in ALGO_FILES.items():
        file_to_keys[path].append(key)

    # 5-2) 각 파일별로 필터링된 entries 생성 후 테이블 갱신
    for file_path, keys in file_to_keys.items():
        if not file_path.exists():
            print(f"⚠️ 파일이 존재하지 않아 건너뜁니다: {file_path}")
            continue

        # 키 목록에 해당하는 알고리즘을 가진 entry만 필터링
        filtered = [e for e in entries if e["algo"].strip() in keys]
        if not filtered:
            # 테이블 헤더만 유지하게 덮어쓰기
            lines = file_path.read_text(encoding="utf-8").splitlines()
            start_idx = next(
                (i for i, l in enumerate(lines) if l.strip().startswith("## 📚 해결한 문제들")),
                None
            )
            if start_idx is None:
                print(f"⚠️ {file_path.name} 파일에 '## 📚 해결한 문제들' 섹션이 없어 건너뜁니다.")
                continue

            # 새로운 테이블: 헤더만
            new_table = []
            header = lines[start_idx + 1]  # 기존 헤더 행
            divider = lines[start_idx + 2]  # 구분선
            new_table.extend([header, divider])

            # 기존 테이블 영역 제거
            end_idx = start_idx + 1
            for i in range(start_idx + 1, len(lines)):
                if lines[i].strip().startswith("## "):
                    break
                end_idx += 1

            lines_before = lines[: start_idx + 1]
            lines_after = lines[end_idx:]

            updated = lines_before + [""] + new_table + [""] + lines_after
            file_path.write_text("\n".join(updated), encoding="utf-8")
            print(f"✅ {file_path.name} (키만 존재하지 않음) 테이블 헤더만 작성 완료.")
            continue

        # 파일 내 '## 📚 해결한 문제들' 시작 인덱스 찾기
        lines = file_path.read_text(encoding="utf-8").splitlines()
        start_idx = next(
            (i for i, l in enumerate(lines) if l.strip().startswith("## 📚 해결한 문제들")),
            None
        )
        if start_idx is None:
            print(f"⚠️ {file_path.name} 파일에 '## 📚 해결한 문제들' 섹션이 없어 건너뜁니다.")
            continue

        # 새로운 테이블 생성
        new_table = []
        new_table.append("| 문제명 | 번호 | 난이도 | 주차 | bum | hano | jin |")
        new_table.append("|--------|------|--------|------|-----|------|-----|")
        for e in filtered:
            name_text = extract_plain_name(e["name"])
            link = f"[{name_text}](https://www.acmicpc.net/problem/{e['number']})"
            tier_cell = e["tier"]
            week_cell = e["week"]
            bum_cell = e["bum"] if e["bum"] else "-"
            hano_cell = e["hano"] if e["hano"] else "-"
            jin_cell = e["jin"] if e["jin"] else "-"
            row = f"| {link} | {e['number']} | {tier_cell} | {week_cell} | {bum_cell} | {hano_cell} | {jin_cell} |"
            new_table.append(row)

        # 기존 테이블 영역 제거 및 삽입
        end_idx = start_idx + 1
        for i in range(start_idx + 1, len(lines)):
            if lines[i].strip().startswith("## "):
                break
            end_idx += 1

        lines_before = lines[: start_idx + 1]
        lines_after = lines[end_idx:]

        updated = lines_before + [""] + new_table + [""] + lines_after
        file_path.write_text("\n".join(updated), encoding="utf-8")
        print(f"✅ {file_path.name} 테이블 업데이트 완료.")


def main():
    entries = parse_solved_entries()
    if not entries:
        print("Warning: 해결한 문제 목록을 파싱하지 못했습니다.")
        return

    # 1) by-tier 파일들 갱신
    for tier_name in TIER_FILES.keys():
        update_tier_file(tier_name, entries)

    # 2) by-algorithm 파일들 갱신
    update_algo_files(entries)

    print("✅ 모든 분류 파일 업데이트 완료.")


if __name__ == "__main__":
    main()