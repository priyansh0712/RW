# 🏏 IPL Matches Data Analysis — Excel Project

A comprehensive Excel-based data analysis project on **IPL matches from 2007 to 2024**, covering all stages of a real-world data workflow — from raw data import to an interactive dashboard.

---

## 📁 Project Structure

```
IPL_Analysis_All_Tasks.xlsx
├── Raw Data                  → Original dataset (1095 rows × 20 columns)
├── T1 – Dataset Overview     → Import summary & column metadata
├── T2 – Data Cleaning        → Missing values, duplicates, type checks
├── T3 – Pivot Tables         → Cross-tab analysis by team, season & toss
├── T4 – Advanced Formulas    → VLOOKUP, INDEX-MATCH, IF & nested functions
├── T5 – Data Visualization   → Charts & conditional formatting
├── T6 – Dashboard            → KPI cards, season summary & win rate chart
└── T7 – Documentation        → Naming conventions & usage instructions
```

---

## 📊 Dataset Overview

| Attribute            | Detail                              |
|----------------------|-------------------------------------|
| **File**             | `matches.xlsx`                      |
| **Records**          | 1,095 matches                       |
| **Columns**          | 20                                  |
| **Seasons**          | 2007/08 – 2024 (17 seasons)         |
| **Teams**            | 15+ franchises                      |
| **Venues**           | 58 stadiums across 36 cities        |

### Key Columns

| Column | Description |
|---|---|
| `id` | Unique match identifier |
| `season` | IPL season year |
| `date` | Match date |
| `team1` / `team2` | Competing teams |
| `toss_winner` | Team that won the toss |
| `toss_decision` | Bat or Field |
| `winner` | Match winner |
| `result` | Runs / Wickets / Tie / No Result |
| `result_margin` | Winning margin |
| `player_of_match` | Best performer of the match |
| `venue` / `city` | Match location |
| `match_type` | League / Semi Final / Final / etc. |

---

## 🗂️ Task Breakdown

### Task 1 — Dataset Selection & Import
**Skills:** Data Import, Initial Cleaning  
**Time Estimate:** 15 min | **Weightage:** 5%

- Loaded `matches.xlsx` using pandas
- Verified shape: **1095 rows × 20 columns**
- Documented all column names, data types, and null counts
- Identified date range: **Oct 2007 → Jun 2024**

---

### Task 2 — Data Cleaning & Preparation
**Skills:** Remove duplicates, Handle missing values, Format data types  
**Time Estimate:** 25 min | **Weightage:** 10%

- **Missing values** found in: `winner` (5), `city`, `player_of_match`, `method`, `target_runs`, `target_overs`, `result_margin`
- **Zero duplicate rows** detected across all 1,095 records
- Data types confirmed: `date` as datetime, `result_margin` as float, text fields as string
- Null percentage calculated per column using live Excel formulas (`=D{n}/B{n}`)

---

### Task 3 — Pivot Tables
**Skills:** Data Analysis, Summarization  
**Time Estimate:** 30 min | **Weightage:** 15%

**Pivot 1 — Wins by Team per Season (Top 8 Teams)**
- Rows: Team names | Columns: Seasons | Values: Win count
- Grand Total row auto-calculated with `SUM` formulas

**Pivot 2 — Toss Decision vs. Match Win**
- Rows: Bat / Field | Columns: Toss winner won (Yes/No) | Values: Match count
- Reveals whether winning the toss gives a competitive advantage

---

### Task 4 — Advanced Formulas
**Skills:** VLOOKUP, INDEX-MATCH, IF conditions, Nested functions  
**Time Estimate:** 35 min | **Weightage:** 15%

A **Team Reference Table** was built with: Matches Played, Wins, Win Rate, Most Recent Season.

Live formula demos (change the **yellow cell** to look up any team):

| Formula Type | Purpose |
|---|---|
| `VLOOKUP` | Fetch matches played & wins by team name |
| `INDEX-MATCH` | Fetch win rate & recent season |
| `IF` | Classify team as Elite / Strong / Developing |
| Nested `IF` | Rate win % as Excellent / Good / Average |

All formulas use `IFERROR` wrapping to handle unmatched team names gracefully.

---

### Task 5 — Data Visualization
**Skills:** Charts, Conditional Formatting  
**Time Estimate:** 40 min | **Weightage:** 20%

Three charts embedded in the sheet:

1. **Horizontal Bar Chart** — Top 10 teams by total wins
2. **Pie Chart** — Toss decision split (Field vs Bat)
3. **Column Chart** — Matches played per IPL season

**Conditional Formatting** applied on the wins column using a Red→Yellow→Green color scale to highlight team performance at a glance.

---

### Task 6 — Interactive Dashboard
**Skills:** Slicers, Timeline, Dynamic ranges  
**Time Estimate:** 45 min | **Weightage:** 25%

**KPI Cards** (top section):

| KPI | Value |
|---|---|
| Total Matches | 1,095 |
| Total Seasons | 17 |
| Teams Participated | 15+ |
| Most Successful Team | Mumbai Indians |
| Top Player of Match | AB de Villiers |
| Super Over Matches | 17 |

**Season Summary Table** — one row per season showing: matches, teams, champion, top player, and average winning margin.

**Win Rate Chart** — Horizontal bar chart for top 6 teams with live `ROUND()` formula-driven percentages.

**Conditional Formatting** on the Matches column highlights high-volume seasons in dark blue.

---

### Task 7 — Documentation
**Skills:** Sheet organization, Naming conventions, Instructions  
**Time Estimate:** 20 min | **Weightage:** 10%

- Full **workbook structure guide** listing every sheet and its purpose
- **Naming conventions** for sheets, headers, alternating rows, KPI cards, and formulas
- **Step-by-step usage instructions** for navigating and using the workbook

---

## 🎨 Design Conventions

| Element | Style |
|---|---|
| Header rows | Dark blue fill (`#1F4E79`), white bold text |
| Alternating rows | Light blue (`#D6E4F0`) / white |
| Section titles | Bold, colored `#1F4E79`, with emoji prefix |
| KPI cards | Category-colored fill with matching bold value |
| Null highlights | Orange fill (`#FFE0B2`) on cells with missing data |
| Formula cells | Live Excel formulas — no hardcoded Python values |

---

## ⚙️ Technical Notes

- Built with **Python + openpyxl** for formatting and formulas
- **pandas** used for data analysis and pivot computation
- All calculations use **live Excel formulas** (not hardcoded values) so the workbook recalculates dynamically
- Verified with `recalc.py` — **0 formula errors**, 87 live formulas
- Compatible with Microsoft Excel and LibreOffice Calc

---

## 🚀 How to Use

1. Open `IPL_Analysis_All_Tasks.xlsx` in Excel
2. Start with **Raw Data** to explore the source dataset
3. Navigate to any **T# sheet** for the relevant task analysis
4. In **T4 – Advanced Formulas**, change the **yellow cell** to look up any team name
5. Use **T6 – Dashboard** for a high-level season overview
6. Refer to **T7 – Documentation** for a full guide

---

## 📈 Key Insights

- **Mumbai Indians** lead all-time with 144 wins across 17 seasons
- **Chennai Super Kings** follow closely with 138 wins
- Teams choosing to **field after winning the toss** outnumber those choosing to bat
- **AB de Villiers** holds the most Player of the Match awards (25)
- Season **2013** had the highest number of matches played

---

*Dataset: IPL Matches 2007–2024 | Tool: Microsoft Excel | Analysis: Python (pandas, openpyxl)*