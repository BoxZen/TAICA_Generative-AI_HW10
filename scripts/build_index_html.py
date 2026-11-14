import os
import glob
import re
import html

def generate_index_html():
    # Collect all wiki links
    concepts = sorted(glob.glob("wiki/concepts/*.md"))
    syntheses = sorted(glob.glob("wiki/syntheses/*.md"))
    sources = sorted(glob.glob("wiki/sources/*.md"))

    def make_list_items(file_list):
        items = []
        for fp in file_list:
            clean_fp = fp.replace("\\", "/")
            name = os.path.basename(fp).replace(".md", "")
            # get title from file
            with open(fp, "r", encoding="utf-8") as f:
                first_line = f.readline().strip()
                title = first_line.replace("#", "").strip() or name
            items.append(f'<li><a href="{clean_fp}" target="_blank"><strong>{html.escape(name)}</strong><span>{html.escape(title)}</span></a></li>')
        return "\n".join(items)

    concepts_html = make_list_items(concepts)
    syntheses_html = make_list_items(syntheses)
    sources_html = make_list_items(sources)

    html_content = f'''<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>演算法 LLM Wiki 與教學簡報 | TAICA Generative AI HW10</title>
    <style>
        :root {{
            --bg-color: #f8fafc;
            --card-bg: #ffffff;
            --text-main: #0f172a;
            --text-muted: #64748b;
            --primary: #2563eb;
            --primary-hover: #1d4ed8;
            --border-color: #e2e8f0;
            --radius-lg: 16px;
            --radius-md: 10px;
            --shadow-sm: 0 1px 3px rgba(0,0,0,0.05);
            --shadow-md: 0 10px 25px -5px rgba(0,0,0,0.08);
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        body {{
            background-color: var(--bg-color);
            color: var(--text-main);
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans TC", sans-serif;
            line-height: 1.6;
            padding: 40px 20px;
        }}

        .container {{
            max-width: 1080px;
            margin: 0 auto;
        }}

        /* Header */
        header {{
            text-align: center;
            margin-bottom: 48px;
        }}

        .badge-tag {{
            display: inline-block;
            background: #dbeafe;
            color: #1d4ed8;
            font-size: 13px;
            font-weight: 700;
            padding: 4px 14px;
            border-radius: 20px;
            margin-bottom: 12px;
            letter-spacing: 0.5px;
        }}

        h1 {{
            font-size: 34px;
            font-weight: 800;
            color: #0f172a;
            margin-bottom: 12px;
            letter-spacing: -0.5px;
        }}

        .subtitle {{
            font-size: 16px;
            color: var(--text-muted);
            max-width: 680px;
            margin: 0 auto;
        }}

        /* Hero Action Cards */
        .hero-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
            gap: 24px;
            margin-bottom: 50px;
        }}

        .hero-card {{
            background: var(--card-bg);
            border: 2px solid var(--border-color);
            border-radius: var(--radius-lg);
            padding: 32px 28px;
            box-shadow: var(--shadow-sm);
            transition: all 0.25s ease;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }}

        .hero-card:hover {{
            transform: translateY(-4px);
            box-shadow: var(--shadow-md);
            border-color: var(--primary);
        }}

        .hero-icon {{
            font-size: 40px;
            margin-bottom: 16px;
            display: inline-block;
        }}

        .hero-title {{
            font-size: 22px;
            font-weight: 700;
            color: #0f172a;
            margin-bottom: 10px;
        }}

        .hero-desc {{
            font-size: 14.5px;
            color: var(--text-muted);
            margin-bottom: 24px;
            line-height: 1.6;
        }}

        .btn {{
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            padding: 12px 24px;
            border-radius: var(--radius-md);
            font-size: 15px;
            font-weight: 700;
            text-decoration: none;
            transition: all 0.2s ease;
        }}

        .btn-primary {{
            background: var(--primary);
            color: #ffffff;
        }}

        .btn-primary:hover {{
            background: var(--primary-hover);
        }}

        .btn-secondary {{
            background: #f1f5f9;
            color: #334155;
            border: 1px solid var(--border-color);
        }}

        .btn-secondary:hover {{
            background: #e2e8f0;
            color: #0f172a;
        }}

        /* Wiki Catalog Directory */
        .catalog-section {{
            background: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-lg);
            padding: 36px 32px;
            box-shadow: var(--shadow-sm);
        }}

        .catalog-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 24px;
            padding-bottom: 16px;
            border-bottom: 1px solid var(--border-color);
        }}

        .catalog-header h2 {{
            font-size: 22px;
            font-weight: 700;
        }}

        .quick-links {{
            display: flex;
            gap: 12px;
        }}

        .quick-link {{
            font-size: 13px;
            font-weight: 600;
            color: var(--primary);
            text-decoration: none;
            background: #eff6ff;
            padding: 6px 12px;
            border-radius: 6px;
        }}

        .quick-link:hover {{
            background: #dbeafe;
        }}

        .group-title {{
            font-size: 16px;
            font-weight: 700;
            color: #334155;
            margin: 24px 0 12px 0;
            display: flex;
            align-items: center;
            gap: 8px;
        }}

        .file-list {{
            list-style: none;
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            gap: 12px;
        }}

        .file-list li a {{
            display: flex;
            flex-direction: column;
            padding: 12px 14px;
            background: #f8fafc;
            border: 1px solid #edf2f7;
            border-radius: 8px;
            text-decoration: none;
            transition: all 0.15s ease;
        }}

        .file-list li a:hover {{
            background: #ffffff;
            border-color: #3b82f6;
            transform: translateY(-2px);
            box-shadow: 0 4px 10px rgba(0,0,0,0.03);
        }}

        .file-list li a strong {{
            font-size: 14px;
            color: #1e293b;
            margin-bottom: 2px;
            font-family: monospace;
        }}

        .file-list li a span {{
            font-size: 12.5px;
            color: #64748b;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }}

        footer {{
            text-align: center;
            margin-top: 48px;
            font-size: 13px;
            color: var(--text-muted);
        }}
    </style>
</head>
<body>

    <div class="container">
        <header>
            <span class="badge-tag">LLM WIKI & SLIDES DECK</span>
            <h1>演算法思維躍遷教學導航首頁</h1>
            <p class="subtitle">
                基於 Karpathy LLM Wiki 單向事實防線與 100% 知識邊界規範編譯，面向程式設計初學者的演算法知識庫與互動簡報。
            </p>
        </header>

        <!-- Two Main Hero Cards -->
        <div class="hero-grid">
            <!-- Card 1: Interactive Slides -->
            <div class="hero-card">
                <div>
                    <div class="hero-icon">🖥️</div>
                    <h2 class="hero-title">教學型 HTML 簡報</h2>
                    <p class="hero-desc">
                        10 頁自包含、純清爽卡片風 16:9 簡報。從 LeetCode 超時限制、時間與空間複雜度大 O 標記，深入分治法、動態規劃與貪婪演算法決策矩陣。支援鍵盤 ← / → 翻頁。
                    </p>
                </div>
                <a href="slides-output/deck.html" class="btn btn-primary">
                    立即觀看簡報 (deck.html) ➔
                </a>
            </div>

            <!-- Card 2: Wiki Knowledge Base -->
            <div class="hero-card">
                <div>
                    <div class="hero-icon">📚</div>
                    <h2 class="hero-title">演算法 LLM Wiki 知識庫</h2>
                    <p class="hero-desc">
                        嚴格吸收 7 份原始事實文獻，編譯而成之結構化知識庫。包含 11 篇核心概念、4 篇綜合比較、7 篇文獻摘要與全站總覽。段落 100% 具備雙重出處標註。
                    </p>
                </div>
                <a href="wiki/overview.md" class="btn btn-secondary">
                    閱讀全站總覽 (overview.md) ↗
                </a>
            </div>
        </div>

        <!-- Wiki Directory Navigation -->
        <div class="catalog-section">
            <div class="catalog-header">
                <h2>Wiki 知識庫完整條目導覽</h2>
                <div class="quick-links">
                    <a href="wiki/index.md" class="quick-link">全站總目錄 (index.md)</a>
                    <a href="wiki/log.md" class="quick-link">操作日誌 (log.md)</a>
                    <a href="slides-output/report.md" class="quick-link">交件檢查報告</a>
                </div>
            </div>

            <div class="group-title">🎯 核心概念 (Concepts - 11 篇)</div>
            <ul class="file-list">
                {concepts_html}
            </ul>

            <div class="group-title">⚖️ 綜合比較與決策指引 (Syntheses - 4 篇)</div>
            <ul class="file-list">
                {syntheses_html}
            </ul>

            <div class="group-title">📑 原始資料摘要 (Sources - 7 篇)</div>
            <ul class="file-list">
                {sources_html}
            </ul>
        </div>

        <footer>
            <p>演算法主題 LLM Wiki | TAICA Generative AI HW10 | 2026-11-14</p>
        </footer>
    </div>

</body>
</html>
'''

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content.strip() + "\n")

    print(f"✅ GitHub Pages 入口首頁已建立: index.html ({os.path.getsize('index.html')} bytes)")

if __name__ == "__main__":
    generate_index_html()
