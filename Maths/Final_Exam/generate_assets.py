"""Generate title section SVGs for the Final Exam README."""
import os

ASSET_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")
os.makedirs(ASSET_DIR, exist_ok=True)

TEMPLATE = r'''<svg width="800" height="55" viewBox="0 0 800 55" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@600&amp;family=Space+Grotesk:wght@500&amp;display=swap');
      
      .title-text {{
        font-family: 'Outfit', sans-serif;
        font-weight: 600;
        font-size: 20px;
        fill: #0f172a;
        animation: slide-right 1s cubic-bezier(0.16, 1, 0.3, 1) forwards;
      }}
      
      .icon-circle {{
        fill: url(#icon-grad);
        animation: pulse 3s infinite alternate;
      }}
      
      .divider-line {{
        stroke: url(#line-grad);
        stroke-width: 2;
        stroke-dasharray: 800;
        stroke-dashoffset: 800;
        animation: line-reveal 2s cubic-bezier(0.16, 1, 0.3, 1) forwards;
      }}
      
      @media (prefers-color-scheme: dark) {{
        .title-text {{
          fill: #f8fafc;
        }}
      }}
      
      @keyframes slide-right {{
        from {{ transform: translateX(-10px); opacity: 0; }}
        to {{ transform: translateX(0); opacity: 1; }}
      }}
      
      @keyframes line-reveal {{
        to {{ stroke-dashoffset: 0; }}
      }}
      
      @keyframes pulse {{
        0% {{ filter: drop-shadow(0 0 2px rgba(16, 185, 129, 0.4)); }}
        100% {{ filter: drop-shadow(0 0 8px rgba(16, 185, 129, 0.8)); }}
      }}
    </style>
    
    <linearGradient id="icon-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#10b981" />
      <stop offset="100%" stop-color="#6366f1" />
    </linearGradient>
    
    <linearGradient id="line-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#10b981" stop-opacity="0.8" />
      <stop offset="30%" stop-color="#6366f1" stop-opacity="0.5" />
      <stop offset="100%" stop-color="#f8fafc" stop-opacity="0" />
    </linearGradient>
  </defs>
  
  <g transform="translate(5, 5)">
    <circle cx="20" cy="20" r="16" class="icon-circle" />
    <path d="{icon_path}" stroke="#ffffff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" fill="none" />
    <text x="50" y="27" class="title-text">{title}</text>
    <line x1="0" y1="45" x2="800" y2="45" class="divider-line" />
  </g>
</svg>'''

TITLES = {
    "title_overview": ("Project Overview", "M20 10 V30 M10 20 H30 M20 14 A6 6 0 1 0 20 26 A6 6 0 1 0 20 14"),
    "title_tools": ("Tools Used", "M12 14 H28 M12 20 H28 M12 26 H28 M16 14 V26"),
    "title_part_a": ("Part A - Theory (Short Questions)", "M14 12 H26 V28 H14 Z M17 17 H23 M17 21 H23 M17 25 H20"),
    "title_part_b": ("Part B - Practical Tasks (Outputs)", "M12 12 H28 V28 H12 Z M16 18 L19 22 L24 16"),
    "title_insights": ("Key Insights", "M20 10 V30 M10 20 H30 M14 26 L20 14 L26 26"),
    "title_results": ("Key Results &amp; Interpretations", "M14 12 L20 28 L26 12 M16 20 H24"),
}

for filename, (title, icon_path) in TITLES.items():
    svg = TEMPLATE.format(title=title, icon_path=icon_path)
    path = os.path.join(ASSET_DIR, f"{filename}.svg")
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Created: {path}")

print("\nAll SVG assets generated!")
