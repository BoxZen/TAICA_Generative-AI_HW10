import os
import re
import html

DRAFTS_DIR = "slides-output/drafts"
DECK_PATH = "slides-output/deck.html"

def load_slides():
    slides = []
    for i in range(1, 11):
        filename = f"slide-{i:02d}.md"
        filepath = os.path.join(DRAFTS_DIR, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        lines = content.strip().splitlines()
        title = lines[0].replace("#", "").strip()

        # extract source line
        source_line = ""
        body_bullets = []
        for line in lines[1:]:
            line_str = line.strip()
            if not line_str:
                continue
            if line_str.startswith("來源出處"):
                source_line = line_str
            elif line_str.startswith("-"):
                # bullet item
                body_bullets.append(line_str.lstrip("- ").strip())
            else:
                body_bullets.append(line_str)

        # parse source line: e.g. 來源出處：wiki/... , raw/... , https://...
        raw_source_name = "raw/文獻"
        source_url = "#"
        if "raw/" in source_line:
            raw_match = re.search(r'(raw/[^\s,)]+)', source_line)
            if raw_match:
                raw_source_name = raw_match.group(1)
        url_match = re.search(r'(https?://[^\s,)]+)', source_line)
        if url_match:
            source_url = url_match.group(1)

        slides.append({
            "index": i,
            "title": title,
            "bullets": body_bullets,
            "raw_name": raw_source_name,
            "url": source_url
        })
    return slides

def render_deck():
    slides = load_slides()

    slides_html_list = []
    for s in slides:
        idx = s["index"]
        title = s["title"]
        bullets = s["bullets"]
        raw_name = s["raw_name"]
        url = s["url"]

        # format bullet points with badges
        bullet_items_html = []
        for b in bullets:
            # check bold prefix: e.g. **核心信念**：...
            m = re.match(r'\*\*([^*]+)\*\*[：:]\s*(.*)', b)
            if m:
                label = m.group(1)
                text = m.group(2)
                item_html = f'''<div class="card-item">
                    <span class="badge">{html.escape(label)}</span>
                    <span class="item-text">{html.escape(text)}</span>
                </div>'''
            else:
                item_html = f'''<div class="card-item">
                    <span class="item-text">{html.escape(b)}</span>
                </div>'''
            bullet_items_html.append(item_html)

        bullets_rendered = "\n".join(bullet_items_html)

        slide_html = f'''
        <div class="slide" id="slide-{idx}" data-slide="{idx}">
            <div class="slide-header">
                <span class="slide-tag">PART {idx:02d}</span>
                <h2 class="slide-title">{html.escape(title)}</h2>
            </div>
            <div class="slide-body">
                {bullets_rendered}
            </div>
            <div class="slide-footer">
                <div class="footer-left">
                    <span class="deck-brand">演算法 LLM Wiki 教學簡報</span>
                </div>
                <div class="footer-right">
                    <a class="source-link" href="{url}" target="_blank" rel="noopener noreferrer">
                        出處：{html.escape(raw_name)}（查看原文 ↗）
                    </a>
                </div>
            </div>
        </div>
        '''
        slides_html_list.append(slide_html)

    all_slides_html = "\n".join(slides_html_list)

    html_template = f'''<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>演算法思維躍遷：效能與設計典範指南 (10 頁精華簡報)</title>
    <style>
        :root {{
            --bg-color: #0f172a;
            --slide-bg: #fcfbf9;
            --slide-border: #e2e8f0;
            --text-main: #1e293b;
            --text-muted: #64748b;
            --accent: #2563eb;
            --accent-light: #eff6ff;
            --badge-bg: #dbeafe;
            --badge-text: #1d4ed8;
            --radius-lg: 18px;
            --radius-md: 10px;
            --shadow: 0 20px 40px -15px rgba(0, 0, 0, 0.4);
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        body {{
            background-color: var(--bg-color);
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans TC", sans-serif;
            color: var(--text-main);
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            overflow: hidden;
        }}

        /* 16:9 Presentation Container */
        .presentation-container {{
            position: relative;
            width: 92vw;
            max-width: 1120px;
            aspect-ratio: 16 / 9;
            background: var(--slide-bg);
            border-radius: var(--radius-lg);
            box-shadow: var(--shadow);
            border: 1px solid rgba(255, 255, 255, 0.1);
            overflow: hidden;
            display: flex;
            flex-direction: column;
        }}

        /* Top Progress Bar */
        .progress-bar-container {{
            width: 100%;
            height: 5px;
            background: #e2e8f0;
            position: absolute;
            top: 0;
            left: 0;
            z-index: 20;
        }}

        .progress-bar {{
            height: 100%;
            width: 10%;
            background: linear-gradient(90deg, #3b82f6, #2563eb);
            transition: width 0.3s ease;
        }}

        /* Slide Top Navbar */
        .top-nav {{
            position: absolute;
            top: 18px;
            right: 28px;
            z-index: 25;
            display: flex;
            align-items: center;
            gap: 12px;
        }}

        .page-counter {{
            font-size: 14px;
            font-weight: 700;
            color: var(--text-muted);
            background: rgba(241, 245, 249, 0.85);
            padding: 4px 12px;
            border-radius: 20px;
            letter-spacing: 0.5px;
        }}

        /* Slide Component */
        .slide {{
            display: none;
            flex-direction: column;
            justify-content: space-between;
            width: 100%;
            height: 100%;
            padding: 42px 50px 28px 50px;
            animation: fadeIn 0.25s ease-out;
        }}

        .slide.active {{
            display: flex;
        }}

        @keyframes fadeIn {{
            from {{ opacity: 0.4; transform: translateY(4px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}

        /* Header */
        .slide-header {{
            margin-bottom: 18px;
        }}

        .slide-tag {{
            display: inline-block;
            font-size: 11px;
            font-weight: 800;
            color: #2563eb;
            background: #dbeafe;
            padding: 3px 10px;
            border-radius: 6px;
            margin-bottom: 8px;
            letter-spacing: 1px;
        }}

        .slide-title {{
            font-size: 26px;
            font-weight: 800;
            color: #0f172a;
            line-height: 1.35;
            letter-spacing: -0.3px;
        }}

        /* Body Cards */
        .slide-body {{
            flex: 1;
            display: flex;
            flex-direction: column;
            justify-content: center;
            gap: 12px;
            padding: 6px 0;
        }}

        .card-item {{
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-left: 4px solid #3b82f6;
            padding: 12px 18px;
            border-radius: var(--radius-md);
            display: flex;
            align-items: center;
            gap: 14px;
            box-shadow: 0 2px 6px rgba(0, 0, 0, 0.02);
            transition: transform 0.15s ease;
        }}

        .card-item:hover {{
            transform: translateX(4px);
            border-left-color: #1d4ed8;
        }}

        .badge {{
            font-size: 13px;
            font-weight: 700;
            color: var(--badge-text);
            background: var(--badge-bg);
            padding: 4px 10px;
            border-radius: 6px;
            white-space: nowrap;
            flex-shrink: 0;
        }}

        .item-text {{
            font-size: 15.5px;
            color: #334155;
            line-height: 1.5;
            font-weight: 500;
        }}

        /* Footer */
        .slide-footer {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding-top: 14px;
            border-top: 1px solid #edf2f7;
            font-size: 12px;
            color: var(--text-muted);
        }}

        .deck-brand {{
            font-weight: 600;
            letter-spacing: 0.3px;
        }}

        .source-link {{
            color: #2563eb;
            text-decoration: none;
            font-weight: 600;
            background: #f1f5f9;
            padding: 4px 10px;
            border-radius: 6px;
            transition: all 0.2s ease;
        }}

        .source-link:hover {{
            background: #e2e8f0;
            color: #1d4ed8;
            text-decoration: underline;
        }}

        /* Control Dock Below Presentation */
        .control-dock {{
            margin-top: 20px;
            display: flex;
            align-items: center;
            gap: 20px;
            background: rgba(30, 41, 59, 0.85);
            backdrop-filter: blur(8px);
            padding: 10px 24px;
            border-radius: 40px;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }}

        .btn {{
            background: #334155;
            color: #ffffff;
            border: none;
            padding: 8px 18px;
            border-radius: 20px;
            font-size: 14px;
            font-weight: 600;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 6px;
            transition: all 0.2s ease;
        }}

        .btn:hover:not(:disabled) {{
            background: #2563eb;
            transform: translateY(-1px);
        }}

        .btn:disabled {{
            opacity: 0.35;
            cursor: not-allowed;
        }}

        .shortcut-hint {{
            color: #94a3b8;
            font-size: 12px;
            letter-spacing: 0.3px;
        }}

        kbd {{
            background: #475569;
            color: #f8fafc;
            padding: 2px 6px;
            border-radius: 4px;
            font-size: 11px;
            font-family: monospace;
        }}
    </style>
</head>
<body>

    <div class="presentation-container">
        <!-- Top Progress Bar -->
        <div class="progress-bar-container">
            <div class="progress-bar" id="progressBar"></div>
        </div>

        <!-- Top Right Nav -->
        <div class="top-nav">
            <div class="page-counter" id="pageCounter">1 / 10</div>
        </div>

        <!-- Slides Output -->
        {all_slides_html}
    </div>

    <!-- Navigation Control Dock -->
    <div class="control-dock">
        <button class="btn" id="prevBtn" onclick="changeSlide(-1)">
            <span>←</span> 上一頁
        </button>
        <span class="shortcut-hint">可用鍵盤 <kbd>←</kbd> <kbd>→</kbd> 或 <kbd>Space</kbd> 翻頁</span>
        <button class="btn" id="nextBtn" onclick="changeSlide(1)">
            下一頁 <span>→</span>
        </button>
    </div>

    <script>
        let currentSlide = 1;
        const totalSlides = 10;

        function updateSlide() {{
            // update visibility
            document.querySelectorAll('.slide').forEach((s, idx) => {{
                s.classList.toggle('active', (idx + 1) === currentSlide);
            }});

            // update counter
            document.getElementById('pageCounter').innerText = `${{currentSlide}} / ${{totalSlides}}`;

            // update progress bar
            const progressPercent = (currentSlide / totalSlides) * 100;
            document.getElementById('progressBar').style.width = `${{progressPercent}}%`;

            // update buttons
            document.getElementById('prevBtn').disabled = (currentSlide === 1);
            document.getElementById('nextBtn').disabled = (currentSlide === totalSlides);
        }}

        function changeSlide(direction) {{
            const target = currentSlide + direction;
            if (target >= 1 && target <= totalSlides) {{
                currentSlide = target;
                updateSlide();
            }}
        }}

        // Keyboard navigation
        document.addEventListener('keydown', (e) => {{
            if (e.key === 'ArrowLeft') {{
                changeSlide(-1);
            }} else if (e.key === 'ArrowRight' || e.key === ' ') {{
                e.preventDefault();
                changeSlide(1);
            }}
        }});

        // Initialize
        updateSlide();
    </script>
</body>
</html>
'''

    with open(DECK_PATH, "w", encoding="utf-8") as f:
        f.write(html_template.strip() + "\n")

    print(f"✅ HTML 簡報渲染完成: {DECK_PATH} (共包含 {len(slides)} 頁教學投影片)")

if __name__ == "__main__":
    render_deck()
