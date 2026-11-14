import urllib.request
import ssl
import re
import html
import os
import sys

DATE = "2026-11-14"

SOURCES = [
    {
        "id": "01",
        "slug": "01-time-complexity.md",
        "orig_url": "https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E6%97%B6%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6.md",
        "fetch_url": "https://raw.githubusercontent.com/youngyangyang04/leetcode-master/master/problems/%E5%89%8D%E5%BA%8F/%E6%97%B6%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6.md",
        "title": "关于时间复杂度，你不知道的都在这里！",
        "type": "markdown"
    },
    {
        "id": "02",
        "slug": "02-algorithm-timeout.md",
        "orig_url": "https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E7%AE%97%E6%B3%95%E8%B6%85%E6%97%B6.md",
        "fetch_url": "https://raw.githubusercontent.com/youngyangyang04/leetcode-master/master/problems/%E5%89%8D%E5%BA%8F/%E7%AE%97%E6%B3%95%E8%B6%85%E6%97%B6.md",
        "title": "On的算法居然超时了，此时的n究竟是多大？",
        "type": "markdown"
    },
    {
        "id": "03",
        "slug": "03-recursive-time-complexity.md",
        "orig_url": "https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E9%80%92%E5%BD%92%E7%AE%97%E6%B3%95%E7%9A%84%E6%97%B6%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6.md",
        "fetch_url": "https://raw.githubusercontent.com/youngyangyang04/leetcode-master/master/problems/%E5%89%8D%E5%BA%8F/%E9%80%92%E5%BD%92%E7%AE%97%E6%B3%95%E7%9A%84%E6%97%B6%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6.md",
        "title": "通过一道面试题目，讲一讲递归算法的时间复杂度！",
        "type": "markdown"
    },
    {
        "id": "04",
        "slug": "04-space-complexity.md",
        "orig_url": "https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E7%A9%BA%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6.md",
        "fetch_url": "https://raw.githubusercontent.com/youngyangyang04/leetcode-master/master/problems/%E5%89%8D%E5%BA%8F/%E7%A9%BA%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6.md",
        "title": "空间复杂度分析",
        "type": "markdown"
    },
    {
        "id": "05",
        "slug": "05-recursive-complexity-analysis.md",
        "orig_url": "https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E9%80%92%E5%BD%92%E7%AE%97%E6%B3%95%E7%9A%84%E6%97%B6%E9%97%B4%E4%B8%8E%E7%A9%BA%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6%E5%88%86%E6%9E%90.md",
        "fetch_url": "https://raw.githubusercontent.com/youngyangyang04/leetcode-master/master/problems/%E5%89%8D%E5%BA%8F/%E9%80%92%E5%BD%92%E7%AE%97%E6%B3%95%E7%9A%84%E6%97%B6%E9%97%B4%E4%B8%8E%E7%A9%BA%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6%E5%88%86%E6%9E%90.md",
        "title": "递归算法的时间与空间复杂度分析！",
        "type": "markdown"
    },
    {
        "id": "06",
        "slug": "06-memory-consumption.md",
        "orig_url": "https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%89%8D%E5%BA%8F/%E5%86%85%E5%AD%98%E6%B6%88%E8%80%97.md",
        "fetch_url": "https://raw.githubusercontent.com/youngyangyang04/leetcode-master/master/problems/%E5%89%8D%E5%BA%8F/%E5%86%85%E5%AD%98%E6%B6%88%E8%80%97.md",
        "title": "刷了这么多题，你了解自己代码的内存消耗么？",
        "type": "markdown"
    },
    {
        "id": "07",
        "slug": "07-algorithm-design.md",
        "orig_url": "https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html",
        "fetch_url": "https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html",
        "title": "algorithm design - 演算法筆記",
        "type": "html"
    }
]

def clean_markdown_carl(text):
    # Remove trailing QR code block and separators
    # Notice: Carl uses <div align="center"><img src='https://file1.kamacoder.com/i/algo/01二维码.jpg' width=450> </img></div>
    text = re.sub(r'-{3,}\s*<div align=[\'"]?center[\'"]?>\s*<img[^>]*二维码[^>]*>(\s*</img>)?\s*</div>', '', text, flags=re.I | re.S)
    text = re.sub(r'<div align=[\'"]?center[\'"]?>\s*<img[^>]*二维码[^>]*>(\s*</img>)?\s*</div>', '', text, flags=re.I | re.S)
    text = re.sub(r'-{5,}\s*$', '', text)
    return text.strip()

def parse_ntnu_html(raw_html):
    lines = []
    lines.append("# algorithm design - 演算法筆記")
    lines.append("")

    sections = raw_html.split('<div class="a">')[1:]
    for s_idx, sec in enumerate(sections):
        if '</body>' in sec:
            sec = sec.split('</body>')[0]
        
        h_match = re.search(r'<div class="h">(.*?)</div>', sec, re.S)
        if h_match:
            h_content = h_match.group(1)
            b_match = re.search(r'<p class="b">(.*?)</p>', h_content, re.S)
            w_match = re.search(r'<p class="w">(.*?)</p>', h_content, re.S)
            sec_title = b_match.group(1).strip() if b_match else f"Section {s_idx+1}"
            lines.append(f"## {sec_title}")
            lines.append("")
            if w_match:
                quote = html.unescape(w_match.group(1).strip())
                lines.append(f"> {quote}")
                lines.append("")

        c_match = re.search(r'<div class="c">(.*?)</div>', sec, re.S)
        if not c_match:
            continue
        c_content = c_match.group(1)

        token_pattern = re.compile(r'(<p class="t">.*?</p>|<p>.*?</p>|<textarea>.*?</textarea>|<pre>.*?</pre>|<img[^>]*>)', re.S)
        tokens = token_pattern.findall(c_content)

        for token in tokens:
            if token.startswith('<p class="t">'):
                sub_title = re.search(r'<p class="t">(.*?)</p>', token, re.S).group(1).strip()
                sub_title = re.sub(r'<[^>]+>', '', sub_title)
                sub_title = html.unescape(sub_title)
                lines.append(f"### {sub_title}")
                lines.append("")
            elif token.startswith('<textarea>'):
                code = re.search(r'<textarea>(.*?)</textarea>', token, re.S).group(1)
                code = html.unescape(code).strip('\r\n')
                lines.append("```cpp")
                lines.append(code)
                lines.append("```")
                lines.append("")
            elif token.startswith('<pre>'):
                pre_text = re.search(r'<pre>(.*?)</pre>', token, re.S).group(1)
                pre_text = html.unescape(pre_text).strip('\r\n')
                lines.append("```")
                lines.append(pre_text)
                lines.append("```")
                lines.append("")
            elif token.startswith('<img'):
                src_m = re.search(r'src="([^"]+)"', token)
                if src_m:
                    src = src_m.group(1)
                    full_src = f"https://web.ntnu.edu.tw/~algo/{src}" if not src.startswith('http') else src
                    lines.append(f"![{src}]({full_src})")
                    lines.append("")
            elif token.startswith('<p>'):
                p_text = re.search(r'<p>(.*?)</p>', token, re.S).group(1).strip()
                p_text = re.sub(r'<a href="([^"]+)">(.*?)</a>', r'[\2](\1)', p_text)
                p_text = re.sub(r'<br\s*/?>', '\n', p_text)
                p_text = re.sub(r'</?[a-zA-Z0-9_-]+[^>]*>', '', p_text)
                p_text = html.unescape(p_text).strip()
                if p_text:
                    lines.append(p_text)
                    lines.append("")

    return '\n'.join(lines).strip()

def main():
    ctx = ssl.create_default_context()
    os.makedirs("raw", exist_ok=True)
    results = []

    for item in SOURCES:
        slug = item["slug"]
        path = os.path.join("raw", slug)
        orig_url = item["orig_url"]
        fetch_url = item["fetch_url"]
        title = item["title"]

        print(f"Fetching {slug} from {fetch_url}...")
        req = urllib.request.Request(fetch_url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        try:
            with urllib.request.urlopen(req, context=ctx, timeout=20) as resp:
                if resp.status != 200:
                    print(f"FAILED: Status {resp.status} for {slug}", file=sys.stderr)
                    sys.exit(1)
                raw_bytes = resp.read()
                raw_text = raw_bytes.decode('utf-8', errors='replace')
        except Exception as e:
            print(f"FAILED to fetch {fetch_url}: {e}", file=sys.stderr)
            sys.exit(1)

        # Process content
        if item["type"] == "markdown":
            body = clean_markdown_carl(raw_text)
        elif item["type"] == "html":
            body = parse_ntnu_html(raw_text)

        # Check brake condition: body length < 200 chars
        if len(body) < 200:
            print(f"FAILED: Content too short ({len(body)} chars) for {slug}", file=sys.stderr)
            sys.exit(1)

        # Prepare header
        header = f"> **原始文章標題**：{title}\n> **原始連結**：{orig_url}\n> **擷取日期**：{DATE}\n\n"
        final_content = header + body + "\n"

        with open(path, "w", encoding="utf-8") as f:
            f.write(final_content)

        char_count = len(final_content)
        line_count = len(final_content.splitlines())
        word_count = len(re.findall(r'[\u4e00-\u9fff]|[a-zA-Z0-9]+', final_content))
        results.append({
            "slug": slug,
            "title": title,
            "orig_url": orig_url,
            "lines": line_count,
            "chars": char_count,
            "words": word_count
        })
        print(f"  -> Successfully saved {slug}: {char_count} chars, {word_count} words/tokens, {line_count} lines")

    print("\nAll files fetched successfully!")
    print("\nSummary Table:")
    for r in results:
        print(f"- `raw/{r['slug']}` | 標題: {r['title']} | 字數/詞數: {r['words']} | 總字元: {r['chars']} | 行數: {r['lines']}")

if __name__ == "__main__":
    main()
