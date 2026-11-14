import os
import re

CARDS_DIR = "slides-output/cards"
os.makedirs(CARDS_DIR, exist_ok=True)

TARGET_PAGES = [
    ("wiki/concepts/time-complexity.md", "card-time-complexity.md"),
    ("wiki/concepts/algorithm-timeout.md", "card-algorithm-timeout.md"),
    ("wiki/concepts/space-complexity.md", "card-space-complexity.md"),
    ("wiki/concepts/recursive-complexity.md", "card-recursive-complexity.md"),
    ("wiki/concepts/memory-management.md", "card-memory-management.md"),
    ("wiki/concepts/incremental-method.md", "card-incremental-method.md"),
    ("wiki/concepts/memoization.md", "card-memoization.md"),
    ("wiki/concepts/divide-and-conquer.md", "card-divide-and-conquer.md"),
    ("wiki/concepts/dynamic-programming.md", "card-dynamic-programming.md"),
    ("wiki/concepts/greedy-algorithm.md", "card-greedy-algorithm.md"),
    ("wiki/syntheses/dp-vs-greedy.md", "card-dp-vs-greedy.md"),
    ("wiki/syntheses/recursion-vs-iteration.md", "card-recursion-vs-iteration.md"),
]

def extract_card(wiki_path, card_name):
    with open(wiki_path, "r", encoding="utf-8") as f:
        content = f.read()

    lines = content.splitlines()
    title = lines[0].replace("#", "").strip()

    # extract definition, analogies, key properties, complexity data, and citations
    cite_pattern = re.compile(r'(\[來源:[^\]]+\|\s*原始連結\]\(https?://[^\)]+\))')
    cites = cite_pattern.findall(content)

    card_content = []
    card_content.append(f"# 證據卡：{title}")
    card_content.append(f"> **來源 Wiki 頁面**：`{wiki_path}`")
    card_content.append(f"> **權限隔離狀態**：純文字唯讀抽取，100% 知識邊界鎖定")
    card_content.append("")
    card_content.append("## 1. 關鍵定義與白話類比")

    # find section 1
    sec1 = re.search(r'## 1\..*?\n(.*?)(?=\n## 2|\Z)', content, re.S)
    if sec1:
        card_content.append(sec1.group(1).strip())
    card_content.append("")

    card_content.append("## 2. 核心運作步驟與關鍵性質")
    sec2 = re.search(r'## 2\..*?\n(.*?)(?=\n## 3|\Z)', content, re.S)
    if sec2:
        card_content.append(sec2.group(1).strip())
    card_content.append("")

    card_content.append("## 3. 重要數據與複雜度證據")
    sec3 = re.search(r'## 3\..*?\n(.*?)(?=\n## 4|\Z)', content, re.S)
    if sec3:
        card_content.append(sec3.group(1).strip())
    card_content.append("")

    card_content.append("## 4. 嚴格收錄之雙重出處清單")
    for i, c in enumerate(set(cites), 1):
        card_content.append(f"{i}. {c}")
    card_content.append("")

    out_path = os.path.join(CARDS_DIR, card_name)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(card_content) + "\n")
    print(f"成功產出證據卡: {out_path} (含 {len(cites)} 條出處標註)")

for wp, cn in TARGET_PAGES:
    extract_card(wp, cn)

print(f"\n全部 {len(TARGET_PAGES)} 張證據卡抽取完成！")
