import os
import sys
import re
import argparse

DRAFTS_DIR = "slides-output/drafts"
DECK_HTML = "slides-output/deck.html"

def check_drafts():
    print("=== [檢查節點 4: 逐頁稿字數與出處驗證] ===")
    all_passed = True
    results = []

    for i in range(1, 11):
        filename = f"slide-{i:02d}.md"
        filepath = os.path.join(DRAFTS_DIR, filename)

        if not os.path.exists(filepath):
            print(f"❌ 缺失檔案: {filepath}")
            all_passed = False
            continue

        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        source_match = re.search(r'(來源出處[：:].*)', content, re.M)
        if not source_match:
            print(f"❌ {filename}: 缺少「來源出處：」欄位")
            all_passed = False
            continue

        source_line = source_match.group(1)
        lines = content.splitlines()
        body_lines = [l for l in lines if not l.startswith("#") and not l.startswith("來源出處") and not l.startswith(">")]
        body_text = " ".join(body_lines)

        zh_chars = re.findall(r'[\u4e00-\u9fff]', body_text)
        zh_count = len(zh_chars)

        limit_passed = zh_count <= 120

        paths_in_source = re.findall(r'(wiki/[^\s,)]+|raw/[^\s,)]+)', source_line)
        path_errors = []
        for p in paths_in_source:
            if p.endswith(".md"):
                clean_p = p.replace("/", os.sep)
            else:
                clean_p = p.replace("/", os.sep) + ".md"
            if not os.path.exists(clean_p):
                path_errors.append(clean_p)

        status_str = "✅ 通過" if (limit_passed and len(path_errors) == 0) else "❌ 未通過"
        if not limit_passed:
            all_passed = False
            status_str += f" (中文字數超標: {zh_count} > 120)"
        if path_errors:
            all_passed = False
            status_str += f" (不存在的路徑: {', '.join(path_errors)})"

        results.append({
            "file": filename,
            "zh_count": zh_count,
            "status": status_str
        })
        print(f"  {filename} | 中文字數: {zh_count:3d} / 120 | {status_str}")

    print("\n--- 檢查總結 ---")
    if all_passed:
        print("🎉 全部 10 頁逐頁稿均符合字數規格（<= 120 字）且出處檔案均真實存在！")
    else:
        print("⚠️ 存在未通過規格的頁面，請退回修訂！")

    return all_passed

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--stage", choices=["drafts", "deck"], default="drafts")
    args = parser.parse_args()

    if args.stage == "drafts":
        ok = check_drafts()
        sys.exit(0 if ok else 1)
    elif args.stage == "deck":
        if os.path.exists(DECK_HTML):
            print(f"✅ 簡報實體檔案已建立: {DECK_HTML} ({os.path.getsize(DECK_HTML)} bytes)")
            sys.exit(0)
        else:
            print(f"❌ 找不到簡報實體檔案: {DECK_HTML}")
            sys.exit(1)

if __name__ == "__main__":
    main()
