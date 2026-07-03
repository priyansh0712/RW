import os

ASSET_DIR = os.path.join("d:\\RW\\RW_Exam\\Maths\\Final_Exam", "assets")
os.makedirs(ASSET_DIR, exist_ok=True)

# Common styling definition to be used in all SVGs
STYLE_DEFS = r'''
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700;800&amp;family=Space+Grotesk:wght@500;700&amp;display=swap');
      
      .panel-bg {
        fill: #f8fafc;
        stroke: #e2e8f0;
        stroke-width: 1.5;
        rx: 12px;
      }
      
      .panel-title {
        font-family: 'Space Grotesk', sans-serif;
        font-weight: 700;
        font-size: 11px;
        letter-spacing: 1px;
        fill: #475569;
        text-transform: uppercase;
      }
      
      .label-text {
        font-family: 'Outfit', sans-serif;
        font-weight: 700;
        font-size: 14px;
        fill: #0f172a;
      }
      
      .sub-text {
        font-family: 'Outfit', sans-serif;
        font-weight: 500;
        font-size: 11px;
        fill: #475569;
      }
      
      .math-text {
        font-family: 'Space Grotesk', sans-serif;
        font-weight: 700;
        font-size: 14px;
        fill: #1e1b4b; /* Deep high-contrast blue for light mode */
      }
      
      .math-formula-large {
        font-family: 'Space Grotesk', sans-serif;
        font-weight: 700;
        font-size: 18px;
        fill: #1e1b4b;
      }
      
      .graphic-stroke {
        stroke: #4f46e5;
        stroke-width: 2.5;
        stroke-linecap: round;
        stroke-linejoin: round;
        fill: none;
      }
      
      .accent-stroke {
        stroke: #10b981;
        stroke-width: 2;
        stroke-linecap: round;
        stroke-linejoin: round;
        fill: none;
      }
      
      .axis-line {
        stroke: #475569;
        stroke-width: 1.5;
        stroke-linecap: round;
      }
      
      .grid-line {
        stroke: #cbd5e1;
        stroke-width: 1;
        stroke-dasharray: 2 2;
      }
      
      .highlight-box {
        fill: #f1f5f9;
        stroke: #cbd5e1;
        stroke-width: 1;
        rx: 6px;
      }

      /* Color-coding for Bayes Theorem */
      .color-posterior { fill: #e11d48; } /* Rose */
      .color-likelihood { fill: #4f46e5; } /* Indigo */
      .color-prior { fill: #059669; } /* Emerald */
      .color-evidence { fill: #475569; } /* Slate */

      @media (prefers-color-scheme: dark) {
        .panel-bg {
          fill: #0f172a;
          stroke: #1e293b;
        }
        .panel-title {
          fill: #94a3b8;
        }
        .label-text {
          fill: #f8fafc;
        }
        .sub-text {
          fill: #94a3b8;
        }
        .math-text {
          fill: #ffffff; /* Crisp white for dark mode */
        }
        .math-formula-large {
          fill: #ffffff;
        }
        .axis-line {
          stroke: #475569;
        }
        .grid-line {
          stroke: #334155;
        }
        .highlight-box {
          fill: #1e293b;
          stroke: #334155;
        }
        .color-posterior { fill: #fb7185; }
        .color-likelihood { fill: #818cf8; }
        .color-prior { fill: #34d399; }
        .color-evidence { fill: #94a3b8; }
      }
    </style>
'''

# 1. Q1 - MEAN, MEDIAN, MODE
q1_svg = rf'''<svg width="600" height="200" viewBox="0 0 600 200" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    {STYLE_DEFS}
  </defs>
  <rect width="600" height="200" class="panel-bg" />
  
  <!-- Left Side: Visual Balance -->
  <g transform="translate(30, 20)">
    <text x="0" y="20" class="panel-title">Q1 Visual Concept</text>
    <text x="0" y="40" class="label-text">Mean as a Physical Balance Point</text>
    
    <!-- Balance scale Pivot -->
    <path d="M 120 120 L 105 160 L 135 160 Z" fill="#94a3b8" fill-opacity="0.3" stroke="#94a3b8" stroke-width="1.5" stroke-linejoin="round" />
    <circle cx="120" cy="120" r="4" fill="#475569" />
    <line x1="80" y1="160" x2="160" y2="160" stroke="#475569" stroke-width="3" stroke-linecap="round" />
    
    <!-- Balanced Beam -->
    <line x1="50" y1="120" x2="190" y2="120" stroke="#4f46e5" stroke-width="3.5" stroke-linecap="round" />
    
    <!-- Hanging Pans -->
    <line x1="55" y1="120" x2="45" y2="145" stroke="#94a3b8" stroke-width="1" />
    <line x1="55" y1="120" x2="65" y2="145" stroke="#94a3b8" stroke-width="1" />
    <line x1="40" y1="145" x2="70" y2="145" stroke="#4f46e5" stroke-width="2" />
    <circle cx="55" cy="138" r="4" fill="#4f46e5" />
    
    <line x1="185" y1="120" x2="175" y2="145" stroke="#94a3b8" stroke-width="1" />
    <line x1="185" y1="120" x2="195" y2="145" stroke="#94a3b8" stroke-width="1" />
    <line x1="170" y1="145" x2="200" y2="145" stroke="#4f46e5" stroke-width="2" />
    <circle cx="185" cy="138" r="4" fill="#4f46e5" />
    
    <text x="120" y="180" text-anchor="middle" class="sub-text">Dataset Balance Point (Mean)</text>
  </g>
  
  <!-- Right Side: Metrics -->
  <g transform="translate(300, 20)">
    <!-- Formula -->
    <rect x="0" y="10" width="270" height="40" class="highlight-box" />
    <text x="15" y="34" class="math-text">Mean (x̄) = Σx / N ≈ ₹69,418</text>
    
    <!-- Compare List -->
    <g transform="translate(15, 75)">
      <!-- Mean -->
      <circle cx="5" cy="5" r="4" fill="#4f46e5" />
      <text x="20" y="8" class="label-text" style="font-size:12px;">Mean (Average): ₹69,418</text>
      
      <!-- Median -->
      <circle cx="5" cy="25" r="4" fill="#10b981" />
      <text x="20" y="28" class="label-text" style="font-size:12px;">Median (Middle Value): ₹69,237</text>
      
      <!-- Mode -->
      <circle cx="5" cy="45" r="4" fill="#ef4444" />
      <text x="20" y="48" class="label-text" style="font-size:12px;">Mode (Most Frequent): ₹15,000</text>
    </g>
    
    <text x="15" y="160" class="sub-text">Mode reveals low-income cluster at ₹15,000</text>
  </g>
</svg>
'''

# 2. Q2 - STANDARD DEVIATION & VARIANCE
q2_svg = rf'''<svg width="600" height="200" viewBox="0 0 600 200" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    {STYLE_DEFS}
    <marker id="arrow-green-q2" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 2 L 8 5 L 0 8 z" fill="#10b981" />
    </marker>
  </defs>
  <rect width="600" height="200" class="panel-bg" />
  
  <!-- Left Side: Curve -->
  <g transform="translate(30, 20)">
    <text x="0" y="20" class="panel-title">Q2 Visual Concept</text>
    <text x="0" y="40" class="label-text">Variance &amp; Standard Deviation</text>
    
    <line x1="20" y1="130" x2="220" y2="130" class="axis-line" />
    
    <!-- Shaded area for sigma -->
    <path d="M 85 130 C 105 130 110 85 120 85 C 130 85 135 130 155 130 Z" fill="#10b981" fill-opacity="0.15" />
    
    <!-- Normal Curve -->
    <path d="M 40 130 C 70 130 90 70 120 70 C 150 70 170 130 200 130" class="graphic-stroke" />
    
    <line x1="120" y1="70" x2="120" y2="130" class="grid-line" />
    <line x1="85" y1="100" x2="155" y2="100" stroke="#10b981" stroke-width="1.5" marker-start="url(#arrow-green-q2)" marker-end="url(#arrow-green-q2)" />
    
    <text x="120" y="145" text-anchor="middle" class="sub-text">Mean (μ)</text>
    <text x="120" y="115" text-anchor="middle" class="sub-text" fill="#10b981" style="font-weight: 600;">Spread (σ)</text>
  </g>
  
  <!-- Right Side: Math Formulas -->
  <g transform="translate(300, 20)">
    <rect x="0" y="10" width="270" height="40" class="highlight-box" />
    <text x="15" y="34" class="math-text">Std Deviation: σ ≈ ₹27,753.30</text>
    
    <g transform="translate(15, 75)">
      <!-- Variance definition -->
      <text x="0" y="10" class="label-text" style="font-size:12px;">Variance (σ²):</text>
      <text x="0" y="28" class="math-text">≈ 770,245,609.88 (₹² units)</text>
      
      <!-- Std Dev definition -->
      <text x="0" y="55" class="label-text" style="font-size:12px;">Standard Deviation (σ):</text>
      <text x="0" y="73" class="math-text">≈ ₹27,753.30 (Original units)</text>
    </g>
    
    <text x="15" y="165" class="sub-text">Std Dev measures spread in the same units as the data</text>
  </g>
</svg>
'''

# 3. Q3 - RANDOM VARIABLE
q3_svg = rf'''<svg width="600" height="200" viewBox="0 0 600 200" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    {STYLE_DEFS}
  </defs>
  <rect width="600" height="200" class="panel-bg" />
  
  <!-- Left Side: Discrete -->
  <g transform="translate(30, 20)">
    <text x="0" y="20" class="panel-title">Discrete Random Variable</text>
    <text x="0" y="40" class="label-text">Default Status (0 or 1)</text>
    
    <line x1="20" y1="130" x2="200" y2="130" class="axis-line" />
    
    <!-- Countable bar pillars representing 0 and 1 -->
    <rect x="60" y="70" width="20" height="60" fill="#4f46e5" rx="2" />
    <rect x="140" y="100" width="20" height="30" fill="#4f46e5" rx="2" />
    
    <text x="70" y="145" text-anchor="middle" class="sub-text">Paid (0)</text>
    <text x="150" y="145" text-anchor="middle" class="sub-text">Default (1)</text>
    <text x="110" y="168" text-anchor="middle" class="sub-text" style="font-weight: 600;">Finite Countable Outcomes</text>
  </g>
  
  <!-- Right Side: Continuous -->
  <g transform="translate(330, 20)">
    <text x="0" y="20" class="panel-title">Continuous Random Variable</text>
    <text x="0" y="40" class="label-text">Customer Income (Y)</text>
    
    <line x1="20" y1="130" x2="220" y2="130" class="axis-line" />
    
    <!-- Continuous Curve representing PDF -->
    <path d="M 30 130 C 70 130 90 60 120 60 C 150 60 170 130 210 130" class="graphic-stroke" stroke="#10b981" />
    
    <!-- Fill under curve -->
    <path d="M 30 130 C 70 130 90 60 120 60 C 150 60 170 130 210 130 Z" fill="#10b981" fill-opacity="0.1" />
    
    <text x="120" y="145" text-anchor="middle" class="sub-text">Income Value (₹)</text>
    <text x="120" y="168" text-anchor="middle" class="sub-text" style="font-weight: 600;">Infinite Uncountable Outcomes</text>
  </g>
</svg>
'''

# 4. Q4 - CONDITIONAL PROBABILITY (IMPROVED: Math Fraction & Restricted Sample Space)
q4_svg = rf'''<svg width="600" height="200" viewBox="0 0 600 200" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    {STYLE_DEFS}
  </defs>
  <rect width="600" height="200" class="panel-bg" />
  
  <!-- Left Side: Venn Diagram highlighting B as the new restricted space -->
  <g transform="translate(20, 20)">
    <text x="0" y="15" class="panel-title">1. Restricted Sample Space</text>
    <text x="0" y="32" class="label-text">Given Condition (Event B)</text>
    
    <!-- Universe Box -->
    <rect x="0" y="50" width="220" height="110" rx="8" stroke="#cbd5e1" stroke-width="1.5" stroke-dasharray="3 3" fill="none" />
    <text x="210" y="65" text-anchor="end" class="sub-text" style="font-size:9px;">Universe S</text>

    <!-- Overlapping Circles -->
    <!-- Event A (Default) -->
    <circle cx="85" cy="105" r="38" fill="#4f46e5" fill-opacity="0.1" stroke="#4f46e5" stroke-width="1.5" />
    
    <!-- Event B (Low Credit Score) -> HIGHLIGHTED & BOLD to show condition -->
    <circle cx="135" cy="105" r="38" fill="#10b981" fill-opacity="0.25" stroke="#10b981" stroke-width="2.5" stroke-dasharray="4 2" />
    
    <!-- Labels -->
    <text x="65" y="108" fill="#4f46e5" font-family="'Outfit', sans-serif" font-weight="700" font-size="11" text-anchor="middle">Default A</text>
    <text x="155" y="108" fill="#059669" font-family="'Outfit', sans-serif" font-weight="800" font-size="11" text-anchor="middle">Score &lt; 600 (B)</text>
    
    <!-- Intersection A and B -->
    <path d="M 110 77 A 38 38 0 0 1 123 105 A 38 38 0 0 1 110 133 A 38 38 0 0 1 97 105 A 38 38 0 0 1 110 77 Z" fill="#7c3aed" fill-opacity="0.4" />
    <text x="110" y="108" fill="#ffffff" font-family="'Outfit', sans-serif" font-weight="800" font-size="9" text-anchor="middle">A ∩ B</text>
    
    <text x="110" y="173" text-anchor="middle" class="sub-text" style="font-size:9.5px; font-weight:700; fill:#059669;">Sample space shrinks from S to B</text>
  </g>
  
  <!-- Right Side: Real Math Fraction Layout -->
  <g transform="translate(260, 20)">
    <text x="0" y="15" class="panel-title">2. Mathematical Representation</text>
    
    <!-- Formula Box -->
    <g transform="translate(0, 28)">
      <rect width="310" height="60" class="highlight-box" />
      
      <!-- Fraction Formula -->
      <text x="15" y="34" class="math-text">Conditional Probability:</text>
      
      <!-- P(A|B) -->
      <text x="180" y="35" text-anchor="end" class="math-text" style="font-size: 15px;">P(A | B) =</text>
      
      <!-- Fraction Numerator -->
      <text x="245" y="25" text-anchor="middle" class="math-text" style="font-size: 13px;">P(A ∩ B)</text>
      <!-- Fraction Line -->
      <line x1="195" y1="31" x2="295" y2="31" stroke="#1e1b4b" stroke-width="1.5" class="axis-line" />
      <!-- Fraction Denominator -->
      <text x="245" y="47" text-anchor="middle" class="math-text" style="font-size: 13px;">P(B)</text>
    </g>

    <!-- Calculation Box -->
    <g transform="translate(0, 100)">
      <!-- Plugged-in value fraction -->
      <!-- Left side text -->
      <text x="0" y="33" class="math-text" style="font-size: 12px; fill:#e11d48;">P(Default | Low Score) =</text>
      
      <!-- Numerator -->
      <text x="200" y="22" text-anchor="middle" class="math-text" style="font-size: 13px; fill:#e11d48;">340</text>
      <!-- Line -->
      <line x1="180" y1="28" x2="220" y2="28" stroke="#e11d48" stroke-width="1.5" />
      <!-- Denominator -->
      <text x="200" y="44" text-anchor="middle" class="math-text" style="font-size: 13px; fill:#e11d48;">860</text>
      
      <!-- Equal Sign and Result -->
      <text x="235" y="33" class="math-text" style="font-size: 14px; fill:#e11d48;">≈ 39.53%</text>
    </g>
    
    <text x="0" y="173" class="sub-text">Default rate doubles for Low Scores (Baseline: 18.52%)</text>
  </g>
</svg>
'''

# 5. Q5 - BAYES' THEOREM (IMPROVED: Math Fraction, Color-Coded Terms & Callouts)
q5_svg = rf'''<svg width="600" height="220" viewBox="0 0 600 220" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    {STYLE_DEFS}
  </defs>
  <rect width="600" height="220" class="panel-bg" />
  
  <g transform="translate(25, 20)">
    <!-- Header -->
    <text x="0" y="15" class="panel-title">Q5 Bayes' Theorem Visual Model</text>
    <text x="0" y="32" class="label-text">Risk Update Equation (Prior to Posterior)</text>
    
    <!-- Fraction Equation Box -->
    <g transform="translate(0, 50)">
      <rect width="550" height="85" class="highlight-box" style="stroke:#10b981; stroke-opacity:0.5;" />
      
      <!-- Posterior: P(Default | Score) -->
      <text x="20" y="48" class="math-formula-large color-posterior">P(Default | Low Score)</text>
      
      <!-- Equals -->
      <text x="225" y="48" class="math-formula-large">=</text>
      
      <!-- Numerator: Likelihood * Prior -->
      <text x="390" y="36" text-anchor="middle" class="math-formula-large">
        <tspan class="color-likelihood">P(Low Score | Default)</tspan>
        <tspan fill="#475569"> · </tspan>
        <tspan class="color-prior">P(Default)</tspan>
      </text>
      
      <!-- Division Line -->
      <line x1="245" y1="44" x2="535" y2="44" stroke="#475569" stroke-width="2" />
      
      <!-- Denominator: Marginal Evidence -->
      <text x="390" y="65" text-anchor="middle" class="math-formula-large color-evidence">P(Low Score)</text>
    </g>
    
    <!-- Color-Coded Explanations / Callouts -->
    <g transform="translate(5, 150)">
      <!-- Col 1: Posterior -->
      <text x="0" y="12" class="sub-text color-posterior" style="font-weight:700;">Posterior Probability</text>
      <text x="0" y="27" class="sub-text">P(A|B) ≈ 39.53%</text>
      <text x="0" y="42" class="sub-text" style="font-size:9.5px;">Updated default probability</text>
      
      <!-- Col 2: Likelihood -->
      <text x="160" y="12" class="sub-text color-likelihood" style="font-weight:700;">Likelihood</text>
      <text x="160" y="27" class="sub-text">P(B|A) ≈ 36.72%</text>
      <text x="160" y="42" class="sub-text" style="font-size:9.5px;">Default group score rate</text>
      
      <!-- Col 3: Prior -->
      <text x="300" y="12" class="sub-text color-prior" style="font-weight:700;">Prior Baseline</text>
      <text x="300" y="27" class="sub-text">P(Default) = 18.52%</text>
      <text x="300" y="42" class="sub-text" style="font-size:9.5px;">Base risk of entire dataset</text>
      
      <!-- Col 4: Evidence -->
      <text x="440" y="12" class="sub-text color-evidence" style="font-weight:700;">Marginal Evidence</text>
      <text x="440" y="27" class="sub-text">P(Score) = 17.20%</text>
      <text x="440" y="42" class="sub-text" style="font-size:9.5px;">Low score rate overall</text>
    </g>
  </g>
</svg>
'''

# 6. Q6 - EMPIRICAL VS THEORETICAL
q6_svg = rf'''<svg width="600" height="200" viewBox="0 0 600 200" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    {STYLE_DEFS}
    <style>
      .divider-vertical {{
        stroke: #cbd5e1;
        stroke-width: 1.5;
      }}
      @media (prefers-color-scheme: dark) {{
        .divider-vertical {{
          stroke: #334155;
        }}
      }}
    </style>
  </defs>
  <rect width="600" height="200" class="panel-bg" />
  
  <!-- Left Column: Theoretical -->
  <g transform="translate(30, 20)">
    <text x="0" y="20" class="panel-title">1. Theoretical Probability</text>
    <text x="0" y="40" class="label-text">Based on Mathematical Reasoning</text>
    
    <!-- Spinner/Coin Flip Diagram -->
    <circle cx="50" cy="115" r="30" fill="none" stroke="#4f46e5" stroke-width="2" />
    <path d="M 50 115 L 50 85" stroke="#4f46e5" stroke-width="2" stroke-linecap="round" />
    <path d="M 50 115 L 75 130" stroke="#4f46e5" stroke-width="2" stroke-linecap="round" />
    <circle cx="50" cy="115" r="4" fill="#4f46e5" />
    
    <g transform="translate(100, 95)">
      <text x="0" y="12" class="sub-text" style="font-weight:600;">Coin Toss Example:</text>
      <text x="0" y="30" class="math-text">P(Heads) = 1/2 = 0.50</text>
    </g>
    
    <text x="0" y="168" class="sub-text">Assumes ideal symmetry &amp; conditions</text>
  </g>
  
  <!-- Divider -->
  <line x1="300" y1="30" x2="300" y2="170" class="divider-vertical" />
  
  <!-- Right Column: Empirical -->
  <g transform="translate(330, 20)">
    <text x="0" y="20" class="panel-title">2. Empirical Probability</text>
    <text x="0" y="40" class="label-text">Based on Observed Data</text>
    
    <!-- Database Table Icon -->
    <rect x="20" y="90" width="50" height="45" rx="4" fill="none" stroke="#10b981" stroke-width="2" />
    <line x1="20" y1="102" x2="70" y2="102" stroke="#10b981" stroke-width="1.5" />
    <line x1="20" y1="114" x2="70" y2="114" stroke="#10b981" stroke-width="1.5" />
    <circle cx="30" cy="96" r="2" fill="#10b981" />
    <circle cx="40" cy="96" r="2" fill="#10b981" />
    
    <g transform="translate(85, 95)">
      <text x="0" y="12" class="sub-text" style="font-weight:600;">Loan Dataset Example:</text>
      <text x="0" y="30" class="math-text">P(Default) = 926 / 5000 = 18.52%</text>
    </g>
    
    <text x="0" y="168" class="sub-text">Based on historical observations</text>
  </g>
</svg>
'''

# 7. Q7 - POISSON DISTRIBUTION
q7_svg = rf'''<svg width="600" height="200" viewBox="0 0 600 200" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    {STYLE_DEFS}
  </defs>
  <rect width="600" height="200" class="panel-bg" />
  
  <!-- Left Side: Bar graph of PMF -->
  <g transform="translate(30, 20)">
    <text x="0" y="20" class="panel-title">Poisson PMF Plot</text>
    <text x="0" y="40" class="label-text">Events Count (λ = 5)</text>
    
    <line x1="20" y1="130" x2="220" y2="130" class="axis-line" />
    
    <!-- Poisson bars -->
    <rect x="35" y="122" width="8" height="8" fill="#4f46e5" rx="1" />
    <rect x="55" y="105" width="8" height="25" fill="#4f46e5" rx="1" />
    <rect x="75" y="80" width="8" height="50" fill="#4f46e5" rx="1" />
    <rect x="95" y="65" width="8" height="65" fill="#4f46e5" rx="1" />
    <rect x="115" y="60" width="8" height="70" fill="#4f46e5" rx="1" />
    <rect x="135" y="70" width="8" height="60" fill="#4f46e5" rx="1" />
    <rect x="155" y="88" width="8" height="42" fill="#4f46e5" rx="1" />
    <rect x="175" y="108" width="8" height="22" fill="#4f46e5" rx="1" />
    <rect x="195" y="120" width="8" height="10" fill="#4f46e5" rx="1" />
    
    <text x="120" y="145" text-anchor="middle" class="sub-text">Number of applications (k)</text>
    <text x="120" y="165" text-anchor="middle" class="sub-text" style="font-weight: 600;">λ = Average Rate of 5 per hour</text>
  </g>
  
  <!-- Right Side: Formula & Usage -->
  <g transform="translate(300, 20)">
    <rect x="0" y="10" width="270" height="45" class="highlight-box" />
    <text x="15" y="28" class="math-text">P(X = k) = (λ^k · e^-λ) / k!</text>
    <text x="15" y="40" class="sub-text">Poisson Probability Mass Function</text>
    
    <g transform="translate(15, 75)">
      <text x="0" y="15" class="label-text" style="font-size:12px;">Business Applications:</text>
      <circle cx="5" cy="30" r="3" fill="#4f46e5" />
      <text x="15" y="33" class="sub-text">Predicting bank branch application arrivals</text>
      
      <circle cx="5" cy="48" r="3" fill="#4f46e5" />
      <text x="15" y="51" class="sub-text">Website transaction volume spikes</text>
      
      <circle cx="5" cy="66" r="3" fill="#4f46e5" />
      <text x="15" y="69" class="sub-text">ATM withdrawal request modeling</text>
    </g>
    
    <text x="15" y="165" class="sub-text">Models discrete arrivals in continuous time</text>
  </g>
</svg>
'''

# 9. Q8 - EIGENVALUES & EIGENVECTORS
q8_svg = rf'''<svg width="600" height="200" viewBox="0 0 600 200" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    {STYLE_DEFS}
    <marker id="arrow-blue-q8" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 2 L 8 5 L 0 8 z" fill="#4f46e5" />
    </marker>
    <marker id="arrow-green-q8" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 2 L 8 5 L 0 8 z" fill="#10b981" />
    </marker>
  </defs>
  <rect width="600" height="200" class="panel-bg" />
  
  <!-- Left Side: Vector Transformations -->
  <g transform="translate(30, 20)">
    <text x="0" y="20" class="panel-title">Matrix Transformation</text>
    <text x="0" y="40" class="label-text">Eigenvector Scaling</text>
    
    <line x1="20" y1="130" x2="200" y2="130" class="axis-line" />
    <line x1="20" y1="30" x2="20" y2="130" class="axis-line" />
    
    <!-- Eigenvector (no rotation, only scaled) -->
    <!-- Original vector v -->
    <line x1="20" y1="130" x2="90" y2="90" stroke="#4f46e5" stroke-width="2.5" marker-end="url(#arrow-blue-q8)" />
    <text x="80" y="85" fill="#4f46e5" font-family="'Outfit', sans-serif" font-weight="700" font-size="10">v</text>
    
    <!-- Transformed vector Av = λv -->
    <line x1="20" y1="130" x2="160" y2="50" stroke="#10b981" stroke-width="2.5" marker-end="url(#arrow-green-q8)" />
    <text x="150" y="45" fill="#10b981" font-family="'Outfit', sans-serif" font-weight="700" font-size="10">Av (λv)</text>
    
    <text x="110" y="152" text-anchor="middle" class="sub-text">Eigenvector direction is invariant</text>
  </g>
  
  <!-- Right Side: Equation & Use -->
  <g transform="translate(300, 20)">
    <rect x="0" y="10" width="270" height="45" class="highlight-box" />
    <text x="15" y="28" class="math-text">Eigenvector Equation: A · v = λ · v</text>
    <text x="15" y="40" class="sub-text">A: matrix | v: eigenvector | λ: eigenvalue</text>
    
    <g transform="translate(15, 75)">
      <text x="0" y="15" class="label-text" style="font-size:12px;">Role in Data Analysis:</text>
      <circle cx="5" cy="30" r="3" fill="#4f46e5" />
      <text x="15" y="33" class="sub-text">Identifies principal components in PCA</text>
      
      <circle cx="5" cy="48" r="3" fill="#4f46e5" />
      <text x="15" y="51" class="sub-text">Captures direction of maximum variance</text>
      
      <circle cx="5" cy="66" r="3" fill="#4f46e5" />
      <text x="15" y="69" class="sub-text">Reduces dimensionality with minimal loss</text>
    </g>
    
    <text x="15" y="165" class="sub-text">Eigenvectors define the principal axes</text>
  </g>
</svg>
'''

# Write SVG files
svg_files = {
    "q1_mean_median_mode.svg": q1_svg,
    "q2_std_dev_variance.svg": q2_svg,
    "q3_random_variable.svg": q3_svg,
    "q4_conditional_probability.svg": q4_svg,
    "q5_bayes_theorem.svg": q5_svg,
    "q6_empirical_theoretical.svg": q6_svg,
    "q7_poisson_distribution.svg": q7_svg,
    "q8_eigenvalues_eigenvectors.svg": q8_svg,
}

for name, code in svg_files.items():
    path = os.path.join(ASSET_DIR, name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(code.strip())
    print(f"Created assets/{name}")

print("All individual SVG diagrams generated successfully!")
