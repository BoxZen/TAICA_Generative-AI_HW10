import os
import re
import glob

WIKI_DIR = "wiki"
RAW_DIR = "raw"

def check_wiki():
    print("=== 開始執行 Wiki 知識庫 Lint 健康檢查 ===")
    errors = []
    warnings = []

    # 1. Gather all markdown files in wiki/
    wiki_files = glob.glob(f"{WIKI_DIR}/**/*.md", recursive=True)
    wiki_files = [os.path.normpath(f) for f in wiki_files]
    print(f"掃描到 {len(wiki_files)} 份 Wiki Markdown 檔案。")

    # 2. Check broken links
    link_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
    all_referenced_files = set()

    for wf in wiki_files:
        with open(wf, "r", encoding="utf-8") as f:
            content = f.read()

        base_dir = os.path.dirname(wf)
        links = link_pattern.findall(content)
        for text, target in links:
            # ignore web links or mailto
            if target.startswith("http://") or target.startswith("https://") or target.startswith("mailto:"):
                continue
            # ignore anchors
            clean_target = target.split("#")[0]
            if not clean_target:
                continue
            # resolve relative path
            # if target starts with file:///
            if clean_target.startswith("file:///"):
                target_path = clean_target.replace("file:///", "").replace("/", os.sep)
            else:
                target_path = os.path.normpath(os.path.join(base_dir, clean_target))

            all_referenced_files.add(target_path)
            if not os.path.exists(target_path):
                errors.append(f"[斷鏈錯誤] 在 {wf} 中的連結指向不存在的檔案: {target} (解析路徑: {target_path})")

    # 3. Check orphan files (except index.md, log.md)
    # Check index.md mentions
    index_path = os.path.normpath(os.path.join(WIKI_DIR, "index.md"))
    with open(index_path, "r", encoding="utf-8") as f:
        index_content = f.read()

    for wf in wiki_files:
        if wf.endswith("index.md") or wf.endswith("log.md"):
            continue
        rel_from_wiki = os.path.relpath(wf, WIKI_DIR).replace("\\", "/")
        if rel_from_wiki not in index_content:
            warnings.append(f"[孤島警示] 檔案 {wf} (相對路徑: {rel_from_wiki}) 未被收錄於 wiki/index.md")

    # 4. Check citations in concepts and syntheses
    cite_pattern = re.compile(r'\[來源:\s*raw/[^\]]+\s*\|\s*原始連結\]\(https?://[^\)]+\)')
    for wf in wiki_files:
        if "concepts" in wf or "syntheses" in wf:
            with open(wf, "r", encoding="utf-8") as f:
                content = f.read()
            cites = cite_pattern.findall(content)
            if len(cites) == 0:
                errors.append(f"[出處缺失] {wf} 內未發現任何合規雙重出處標註 [來源: raw/... | 原始連結](URL)")
            else:
                print(f"  [出處驗證通過] {os.path.basename(wf)}: 包含 {len(cites)} 處雙重出處引用")

    print("\n--- 檢查結果 ---")
    if errors:
        print(f"發現 {len(errors)} 個嚴重錯誤:")
        for e in errors:
            print("  ❌", e)
    else:
        print("✅ 斷鏈檢查與出處格式檢查 100% 通過，無嚴重錯誤！")

    if warnings:
        print(f"發現 {len(warnings)} 個警示:")
        for w in warnings:
            print("  ⚠️", w)
    else:
        print("✅ 孤島檢查 100% 通過，所有頁面皆被 index.md 正常索引！")

    return len(errors) == 0

if __name__ == "__main__":
    check_wiki()
