import streamlit as st

st.set_page_config(
    page_title="ILLUMILIGHT — Social Enterprise",
    page_icon="💡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;0,900;1,700&family=Outfit:wght@300;400;500;600&display=swap');

:root {
  --bg: #0d0f0a;
  --surface: #13160e;
  --surface2: #1a1f12;
  --gold: #e8b84b;
  --gold-dim: rgba(232,184,75,0.10);
  --gold-border: rgba(232,184,75,0.25);
  --green: #5db863;
  --green-dim: rgba(93,184,99,0.10);
  --text: #f0ece0;
  --text-2: #9a9880;
  --text-3: #4a4a38;
  --border: rgba(255,255,255,0.06);
  --r: 12px;
}

/* ── NO TEXT CURSOR ANYWHERE ── */
*, *::before, *::after {
  cursor: default !important;
  user-select: none !important;
  -webkit-user-select: none !important;
  -moz-user-select: none !important;
}

html, body, [class*="css"] {
  font-family: 'Outfit', sans-serif;
  background: var(--bg) !important;
  color: var(--text);
}
.stApp {
  background:
    radial-gradient(ellipse 80% 50% at 20% 0%, rgba(93,184,99,0.06) 0%, transparent 60%),
    radial-gradient(ellipse 60% 40% at 80% 100%, rgba(232,184,75,0.07) 0%, transparent 55%),
    var(--bg) !important;
}
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 0 !important; max-width: 100% !important; }

/* ── SCROLL REVEAL ── */
.reveal {
  opacity: 0;
  transform: translateY(40px);
  transition: opacity 0.7s cubic-bezier(0.22,1,0.36,1), transform 0.7s cubic-bezier(0.22,1,0.36,1);
}
.reveal.visible {
  opacity: 1;
  transform: translateY(0);
}
.reveal-delay-1 { transition-delay: 0.1s; }
.reveal-delay-2 { transition-delay: 0.2s; }
.reveal-delay-3 { transition-delay: 0.3s; }
.reveal-delay-4 { transition-delay: 0.4s; }
.reveal-delay-5 { transition-delay: 0.5s; }

/* ── NAV ── */
.nav {
  position: sticky; top: 0; z-index: 100;
  background: rgba(13,15,10,0.85);
  backdrop-filter: blur(20px);
  border-bottom: 1px solid var(--border);
  padding: 0 48px; height: 64px;
  display: flex; align-items: center; justify-content: space-between;
  animation: slideDown 0.6s cubic-bezier(0.22,1,0.36,1) both;
}
.nav-logo {
  font-family: 'Playfair Display', serif;
  font-size: 1.4rem; font-weight: 900;
  color: var(--gold); letter-spacing: 0.04em;
}
.nav-logo span { color: var(--text); font-weight: 700; }
.nav-links { display: flex; gap: 6px; }
.nav-link {
  font-size: 0.68rem; font-weight: 600; letter-spacing: 0.12em;
  text-transform: uppercase; color: var(--text-3);
  padding: 5px 12px; border-radius: 100px;
  border: 1px solid transparent;
  transition: color 0.2s, border-color 0.2s, background 0.2s;
  text-decoration: none;
}
.nav-link:hover { color: var(--gold); border-color: var(--gold-border); background: var(--gold-dim); }
.nav-tag {
  font-size: 0.68rem; font-weight: 600; letter-spacing: 0.15em;
  text-transform: uppercase; color: var(--text-3);
  border: 1px solid var(--border); border-radius: 100px; padding: 4px 12px;
}

/* ── HERO ── */
.hero {
  min-height: 96vh;
  display: flex; flex-direction: column;
  align-items: center; justify-content: center;
  text-align: center; padding: 80px 48px;
  position: relative; overflow: hidden;
}
.hero-bg-glow {
  position: absolute; width: 600px; height: 600px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(232,184,75,0.07) 0%, transparent 70%);
  top: 50%; left: 50%; transform: translate(-50%, -50%);
  animation: glowPulse 4s ease-in-out infinite;
  pointer-events: none;
}
.hero-eyebrow {
  display: inline-flex; align-items: center; gap: 8px;
  font-size: 0.72rem; font-weight: 600; letter-spacing: 0.2em;
  text-transform: uppercase; color: var(--green);
  background: var(--green-dim); border: 1px solid rgba(93,184,99,0.25);
  border-radius: 100px; padding: 6px 16px; margin-bottom: 28px;
  animation: fadeUp 0.8s 0.2s cubic-bezier(0.22,1,0.36,1) both;
}
.hero-eyebrow-dot {
  width: 6px; height: 6px; border-radius: 50%;
  background: var(--green);
  animation: pulse 2s ease-in-out infinite;
  display: inline-block;
}
.hero-title {
  font-family: 'Playfair Display', serif;
  font-size: clamp(3.5rem, 8vw, 7rem);
  font-weight: 900; line-height: 0.95;
  letter-spacing: -0.02em; color: var(--text); margin-bottom: 16px;
  animation: fadeUp 0.8s 0.35s cubic-bezier(0.22,1,0.36,1) both;
}
.hero-title em { font-style: italic; color: var(--gold); }
.hero-subtitle-tag {
  font-family: 'Playfair Display', serif;
  font-style: italic; font-size: 1.3rem;
  color: var(--text-2); margin-bottom: 32px;
  animation: fadeUp 0.8s 0.5s cubic-bezier(0.22,1,0.36,1) both;
}
.hero-desc {
  max-width: 640px; margin: 0 auto 48px;
  font-size: 1.05rem; line-height: 1.75;
  color: var(--text-2); font-weight: 300;
  animation: fadeUp 0.8s 0.65s cubic-bezier(0.22,1,0.36,1) both;
}
.hero-stats {
  display: flex; gap: 48px; justify-content: center; flex-wrap: wrap;
  animation: fadeUp 0.8s 0.8s cubic-bezier(0.22,1,0.36,1) both;
}
.hero-stat { text-align: center; }
.hero-stat-num {
  font-family: 'Playfair Display', serif;
  font-size: 2.6rem; font-weight: 700; color: var(--gold); line-height: 1;
}
.hero-stat-label {
  font-size: 0.75rem; font-weight: 500; letter-spacing: 0.1em;
  text-transform: uppercase; color: var(--text-3); margin-top: 4px;
}

/* ── SECTION ── */
.section { padding: 96px 48px; max-width: 1100px; margin: 0 auto; }
.section-eyebrow {
  font-size: 0.7rem; font-weight: 600; letter-spacing: 0.2em;
  text-transform: uppercase; color: var(--gold); margin-bottom: 12px;
}
.section-title {
  font-family: 'Playfair Display', serif;
  font-size: clamp(2rem, 4vw, 3rem); font-weight: 700;
  line-height: 1.1; color: var(--text); margin-bottom: 20px;
}
.section-title em { font-style: italic; color: var(--gold); }
.section-body { font-size: 1rem; line-height: 1.8; color: var(--text-2); font-weight: 300; max-width: 700px; }
.divider { border: none; border-top: 1px solid var(--border); margin: 0; }

/* ── CARDS ── */
.cards-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin-top: 48px; }
.card {
  background: var(--surface); border: 1px solid var(--border);
  border-radius: var(--r); padding: 28px;
  transition: border-color 0.3s, transform 0.3s, box-shadow 0.3s;
  position: relative; overflow: hidden;
}
.card::before {
  content: ""; position: absolute; inset: 0;
  background: linear-gradient(135deg, var(--gold-dim), transparent);
  opacity: 0; transition: opacity 0.3s;
}
.card:hover { border-color: var(--gold-border); transform: translateY(-6px); box-shadow: 0 20px 48px rgba(0,0,0,0.4); }
.card:hover::before { opacity: 1; }
.card-icon { font-size: 2rem; margin-bottom: 16px; }
.card-title { font-family: 'Playfair Display', serif; font-size: 1.1rem; font-weight: 700; color: var(--text); margin-bottom: 10px; }
.card-body { font-size: 0.9rem; line-height: 1.7; color: var(--text-2); font-weight: 300; }

/* ── OUTCOMES ── */
.outcomes-list { list-style: none; padding: 0; margin-top: 40px; display: flex; flex-direction: column; gap: 20px; }
.outcome-item {
  display: flex; align-items: flex-start; gap: 20px;
  background: var(--surface); border: 1px solid var(--border);
  border-radius: var(--r); padding: 24px 28px;
  transition: border-color 0.3s, transform 0.3s;
}
.outcome-item:hover { border-color: rgba(93,184,99,0.3); transform: translateX(6px); }
.outcome-num {
  font-family: 'Playfair Display', serif; font-size: 2.5rem; font-weight: 900;
  color: var(--gold); opacity: 0.3; line-height: 1; flex-shrink: 0; min-width: 48px;
}
.outcome-title { font-size: 1rem; font-weight: 600; color: var(--text); margin-bottom: 6px; }
.outcome-body { font-size: 0.9rem; line-height: 1.7; color: var(--text-2); font-weight: 300; }

/* ── TWO COL ── */
.two-col { display: grid; grid-template-columns: 1fr 1fr; gap: 64px; align-items: center; margin-top: 40px; }

/* ── HIGHLIGHT BOX ── */
.highlight-box {
  background: var(--surface2); border: 1px solid var(--gold-border);
  border-radius: var(--r); padding: 32px;
  position: relative; overflow: hidden;
}
.highlight-box::after {
  content: ""; position: absolute; top: 0; left: 0; right: 0; height: 2px;
  background: linear-gradient(90deg, var(--gold), var(--green));
}
.highlight-box-label {
  font-size: 0.68rem; font-weight: 600; letter-spacing: 0.18em;
  text-transform: uppercase; color: var(--gold); margin-bottom: 14px;
}
.highlight-box-text { font-size: 1rem; line-height: 1.8; color: var(--text-2); font-weight: 300; }
.highlight-box-text strong { color: var(--text); font-weight: 600; }

/* ── SPECS ── */
.specs-row { display: flex; flex-direction: column; gap: 12px; }
.spec-item {
  display: flex; align-items: center; gap: 14px;
  padding: 14px 18px; background: var(--surface2);
  border: 1px solid var(--border); border-radius: 8px;
  transition: border-color 0.3s, transform 0.2s;
}
.spec-item:hover { border-color: var(--gold-border); transform: translateX(4px); }
.spec-icon { font-size: 1.2rem; flex-shrink: 0; width: 28px; text-align: center; }
.spec-text { font-size: 0.9rem; color: var(--text-2); font-weight: 300; }
.spec-text strong { color: var(--text); font-weight: 600; }

/* ── MARKET ── */
.market-stats { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin-top: 40px; }
.market-stat-card {
  background: var(--surface); border: 1px solid var(--border);
  border-radius: var(--r); padding: 28px; text-align: center;
  transition: border-color 0.3s, transform 0.3s;
}
.market-stat-card:hover { border-color: var(--gold-border); transform: translateY(-4px); }
.market-stat-num {
  font-family: 'Playfair Display', serif;
  font-size: 2.8rem; font-weight: 700; color: var(--gold); line-height: 1;
}
.market-stat-label { font-size: 0.8rem; color: var(--text-2); margin-top: 8px; line-height: 1.5; }

/* ── SWOT ── */
.swot-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-top: 40px; }
.swot-card {
  background: var(--surface); border: 1px solid var(--border);
  border-radius: var(--r); padding: 24px;
  transition: transform 0.3s, box-shadow 0.3s;
}
.swot-card:hover { transform: translateY(-4px); box-shadow: 0 16px 40px rgba(0,0,0,0.3); }
.swot-card.strengths { border-top: 2px solid var(--green); }
.swot-card.weaknesses { border-top: 2px solid #e87b4b; }
.swot-card.opportunities { border-top: 2px solid var(--gold); }
.swot-card.threats { border-top: 2px solid #e84b4b; }
.swot-label { font-size: 0.7rem; font-weight: 700; letter-spacing: 0.15em; text-transform: uppercase; margin-bottom: 14px; }
.swot-card.strengths .swot-label { color: var(--green); }
.swot-card.weaknesses .swot-label { color: #e87b4b; }
.swot-card.opportunities .swot-label { color: var(--gold); }
.swot-card.threats .swot-label { color: #e84b4b; }
.swot-list { list-style: none; padding: 0; display: flex; flex-direction: column; gap: 8px; }
.swot-list li { font-size: 0.88rem; color: var(--text-2); font-weight: 300; line-height: 1.5; padding-left: 14px; position: relative; }
.swot-list li::before { content: "—"; position: absolute; left: 0; color: var(--text-3); }

/* ── TEAM ── */
.team-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin-top: 48px; }
.team-card {
  background: var(--surface); border: 1px solid var(--border);
  border-radius: var(--r); padding: 28px;
  transition: border-color 0.3s, transform 0.3s, box-shadow 0.3s;
  position: relative; overflow: hidden;
}
.team-card::after {
  content: ""; position: absolute; bottom: 0; left: 0; right: 0; height: 2px;
  background: linear-gradient(90deg, var(--green), var(--gold));
  transform: scaleX(0); transform-origin: left;
  transition: transform 0.4s cubic-bezier(0.22,1,0.36,1);
}
.team-card:hover { border-color: var(--gold-border); transform: translateY(-5px); box-shadow: 0 20px 48px rgba(0,0,0,0.4); }
.team-card:hover::after { transform: scaleX(1); }
.team-role { font-size: 0.68rem; font-weight: 600; letter-spacing: 0.15em; text-transform: uppercase; color: var(--green); margin-bottom: 8px; }
.team-name { font-family: 'Playfair Display', serif; font-size: 1.1rem; font-weight: 700; color: var(--text); margin-bottom: 10px; }
.team-desc { font-size: 0.85rem; line-height: 1.7; color: var(--text-2); font-weight: 300; }

/* ── RISK ── */
.risk-grid { display: flex; flex-direction: column; gap: 20px; margin-top: 40px; }
.risk-card {
  display: grid; grid-template-columns: 80px 1fr;
  gap: 24px; align-items: start;
  background: var(--surface); border: 1px solid var(--border);
  border-radius: var(--r); padding: 24px 28px;
  transition: border-color 0.3s, transform 0.3s;
}
.risk-card:hover { border-color: var(--gold-border); transform: translateX(6px); }
.risk-num {
  font-family: 'Playfair Display', serif; font-size: 3rem; font-weight: 900;
  color: var(--text-3); line-height: 1; text-align: center;
}
.risk-title { font-size: 0.95rem; font-weight: 600; color: var(--text); margin-bottom: 6px; }
.risk-body { font-size: 0.88rem; line-height: 1.7; color: var(--text-2); font-weight: 300; }
.risk-mitigation {
  margin-top: 10px; padding: 10px 14px;
  background: var(--green-dim); border-left: 2px solid var(--green);
  border-radius: 4px; font-size: 0.82rem; color: var(--green); font-weight: 500;
}

/* ── PROGRESS BAR ── */
.progress-bar {
  position: fixed; top: 0; left: 0; height: 3px; z-index: 200;
  background: linear-gradient(90deg, var(--green), var(--gold));
  width: 0%; transition: width 0.1s linear;
}

/* ── BACK TO TOP ── */
.back-to-top {
  position: fixed; bottom: 32px; right: 32px; z-index: 200;
  width: 44px; height: 44px; border-radius: 50%;
  background: var(--surface2); border: 1px solid var(--gold-border);
  display: flex; align-items: center; justify-content: center;
  font-size: 1.1rem; opacity: 0; transform: translateY(12px);
  transition: opacity 0.3s, transform 0.3s;
  text-decoration: none; color: var(--gold);
}
.back-to-top.visible { opacity: 1; transform: translateY(0); }
.back-to-top:hover { background: var(--gold-dim); }

/* ── FOOTER ── */
.site-footer {
  background: var(--surface); border-top: 1px solid var(--border);
  padding: 64px 48px; text-align: center;
}
.site-footer-title {
  font-family: 'Playfair Display', serif;
  font-size: 2.5rem; font-weight: 900; color: var(--gold); margin-bottom: 8px;
  animation: glowText 3s ease-in-out infinite alternate;
}
.site-footer-sub { font-style: italic; color: var(--text-2); margin-bottom: 28px; font-family: 'Playfair Display', serif; }
.footer-pills { display: flex; gap: 10px; justify-content: center; flex-wrap: wrap; margin-bottom: 24px; }
.footer-pill {
  font-size: 0.72rem; font-weight: 600; letter-spacing: 0.1em;
  text-transform: uppercase; color: var(--text-3);
  border: 1px solid var(--border); border-radius: 100px; padding: 5px 14px;
  transition: border-color 0.3s, color 0.3s;
}
.footer-pill:hover { border-color: var(--gold-border); color: var(--gold); }
.footer-copy { font-size: 0.78rem; color: var(--text-3); }

/* ── ANIMATIONS ── */
@keyframes slideDown {
  from { opacity: 0; transform: translateY(-20px); }
  to { opacity: 1; transform: translateY(0); }
}
@keyframes fadeUp {
  from { opacity: 0; transform: translateY(28px); }
  to { opacity: 1; transform: translateY(0); }
}
@keyframes pulse {
  0%, 100% { opacity: 1; transform: scale(1); }
  50% { opacity: 0.4; transform: scale(0.7); }
}
@keyframes glowPulse {
  0%, 100% { opacity: 1; transform: translate(-50%, -50%) scale(1); }
  50% { opacity: 0.5; transform: translate(-50%, -50%) scale(1.15); }
}
@keyframes glowText {
  from { text-shadow: 0 0 20px rgba(232,184,75,0.3); }
  to { text-shadow: 0 0 40px rgba(232,184,75,0.7); }
}
@keyframes countUp {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}

/* Animated underline on section titles */
.section-title-wrap { position: relative; display: inline-block; margin-bottom: 24px; }
.section-title-wrap::after {
  content: ""; position: absolute; bottom: -8px; left: 0;
  width: 0; height: 2px;
  background: linear-gradient(90deg, var(--gold), var(--green));
  transition: width 0.8s cubic-bezier(0.22,1,0.36,1) 0.3s;
}
.section-title-wrap.visible::after { width: 60px; }
</style>
""", unsafe_allow_html=True)

# ── NAV ──
st.markdown("""
<div class="progress-bar" id="progressBar"></div>
<a class="back-to-top" id="backToTop" href="#">↑</a>

<div class="nav">
  <div class="nav-logo">ILLUMI<span>LIGHT</span></div>
  <div class="nav-links">
    <a class="nav-link" href="#problem">Problem</a>
    <a class="nav-link" href="#solution">Solution</a>
    <a class="nav-link" href="#impact">Impact</a>
    <a class="nav-link" href="#market">Market</a>
    <a class="nav-link" href="#swot">SWOT</a>
    <a class="nav-link" href="#team">Team</a>
    <a class="nav-link" href="#risks">Risks</a>
  </div>
  <div class="nav-tag">SY 2025–2026 · FEU Cavite</div>
</div>
""", unsafe_allow_html=True)

# ── HERO ──
st.markdown("""
<div class="hero" id="hero">
  <div class="hero-bg-glow"></div>
  <div class="hero-eyebrow">
    <span class="hero-eyebrow-dot"></span>
    Social Enterprise · FEU Cavite Basic Education
  </div>
  <div class="hero-title"><em>ILLUMILIGHT</em></div>
  <div class="hero-subtitle-tag">Liwanag sa Daan, Ginhawa sa Bayan</div>
  <p class="hero-desc">
    A community-centered solar lighting enterprise addressing inadequate street lighting
    in Barangay Maguyam, Silang, Cavite — improving nighttime safety and supporting
    local economic activity through renewable energy.
  </p>
  <div class="hero-stats">
    <div class="hero-stat">
      <div class="hero-stat-num" data-target="13364" data-suffix="">0</div>
      <div class="hero-stat-label">Residents Served</div>
    </div>
    <div class="hero-stat">
      <div class="hero-stat-num" data-target="3700" data-suffix="+">0</div>
      <div class="hero-stat-label">Households Addressable</div>
    </div>
    <div class="hero-stat">
      <div class="hero-stat-num">₱0</div>
      <div class="hero-stat-label">Electricity Cost</div>
    </div>
    <div class="hero-stat">
      <div class="hero-stat-num" data-target="100" data-suffix="%">0</div>
      <div class="hero-stat-label">Solar Powered</div>
    </div>
  </div>
</div>
<hr class="divider">
""", unsafe_allow_html=True)

# ── PROBLEM ──
st.markdown("""
<div class="section reveal" id="problem">
  <div class="section-eyebrow reveal reveal-delay-1">01 — The Problem</div>
  <div class="section-title-wrap reveal reveal-delay-2">
    <div class="section-title">Dark streets.<br><em>Dimmer futures.</em></div>
  </div>
  <p class="section-body reveal reveal-delay-3">
    Inadequate street lighting in Barangay Maguyam creates a cycle of insecurity and lost
    economic opportunity. When darkness falls, safety concerns shrink community life.
  </p>
  <div class="cards-grid">
    <div class="card reveal reveal-delay-2">
      <div class="card-icon">🚶</div>
      <div class="card-title">Mobility & Safety</div>
      <div class="card-body">Poorly lit streets make it difficult and unsafe for residents to move around at night, reducing access to essential services and daily activities.</div>
    </div>
    <div class="card reveal reveal-delay-3">
      <div class="card-icon">🏪</div>
      <div class="card-title">Economic Loss</div>
      <div class="card-body">Sari-sari stores, food stalls, and street vendors lose customers when streets are dark, forcing early closures and reducing household income.</div>
    </div>
    <div class="card reveal reveal-delay-4">
      <div class="card-icon">🌑</div>
      <div class="card-title">Community Isolation</div>
      <div class="card-body">Limited lighting discourages social activities in the evening, weakening community bonds and reducing confidence in public spaces.</div>
    </div>
  </div>
</div>
<hr class="divider">
""", unsafe_allow_html=True)

# ── SOLUTION ──
st.markdown("""
<div class="section reveal" id="solution">
  <div class="section-eyebrow reveal reveal-delay-1">02 — Our Solution</div>
  <div class="section-title-wrap reveal reveal-delay-2">
    <div class="section-title">Hangable solar lights.<br><em>Infinite impact.</em></div>
  </div>
  <div class="two-col">
    <div class="reveal reveal-delay-2">
      <p class="section-body">
        ILLUMILIGHT offers affordable, hangable solar lights that capture sunlight through
        built-in solar panels and store energy in rechargeable batteries — powering bright
        LED lights throughout the night with zero electricity cost.
      </p>
      <p class="section-body" style="margin-top:16px;">
        Unlike decorative solar lanterns, our product is designed specifically for community
        safety: bright enough to illuminate pathways, storefronts, and streets — easy enough
        for any household to install.
      </p>
    </div>
    <div class="specs-row reveal reveal-delay-3">
      <div class="spec-item"><span class="spec-icon">☀️</span><span class="spec-text"><strong>Solar-powered</strong> — charges automatically during the day</span></div>
      <div class="spec-item"><span class="spec-icon">🔋</span><span class="spec-text"><strong>Rechargeable batteries</strong> — stores energy for all-night use</span></div>
      <div class="spec-item"><span class="spec-icon">💡</span><span class="spec-text"><strong>High-brightness LEDs</strong> — functional street visibility, not just decorative</span></div>
      <div class="spec-item"><span class="spec-icon">🪝</span><span class="spec-text"><strong>Hangable design</strong> — easy installation on walls, posts, and stalls</span></div>
      <div class="spec-item"><span class="spec-icon">🛠️</span><span class="spec-text"><strong>Installation support</strong> — guidance and maintenance training included</span></div>
      <div class="spec-item"><span class="spec-icon">🌿</span><span class="spec-text"><strong>Zero emissions</strong> — environmentally sustainable energy source</span></div>
    </div>
  </div>
</div>
<hr class="divider">
""", unsafe_allow_html=True)

# ── IMPACT ──
st.markdown("""
<div class="section reveal" id="impact">
  <div class="section-eyebrow reveal reveal-delay-1">03 — Impact</div>
  <div class="section-title-wrap reveal reveal-delay-2">
    <div class="section-title">What we're<br><em>building toward.</em></div>
  </div>
  <div class="highlight-box reveal reveal-delay-3" style="margin-top:32px; max-width:720px;">
    <div class="highlight-box-label">Impact Goal</div>
    <div class="highlight-box-text">
      To improve <strong>nighttime safety</strong> and support <strong>local economic activity</strong>
      in Barangay Maguyam through accessible, renewable outdoor solar lighting that enables
      residents to move freely and small businesses to operate longer — creating a safer,
      more active, and economically vibrant community.
    </div>
  </div>
  <ul class="outcomes-list">
    <li class="outcome-item reveal reveal-delay-2">
      <div class="outcome-num">01</div>
      <div>
        <div class="outcome-title">🌟 Safer Streets at Night</div>
        <div class="outcome-body">With solar lights hung outside homes, stores, and pathways, the barangay becomes brighter — enabling residents to walk outside more safely and comfortably during evening hours.</div>
      </div>
    </li>
    <li class="outcome-item reveal reveal-delay-3">
      <div class="outcome-num">02</div>
      <div>
        <div class="outcome-title">📈 More Business Activity at Night</div>
        <div class="outcome-body">Small stores and food vendors can illuminate their stalls with solar lights, making spaces visible and well-lit — allowing them to serve customers for longer hours and increase their income.</div>
      </div>
    </li>
    <li class="outcome-item reveal reveal-delay-4">
      <div class="outcome-num">03</div>
      <div>
        <div class="outcome-title">🤝 Greater Community Confidence</div>
        <div class="outcome-body">With accessible outdoor solar lighting, residents feel more comfortable engaging in evening errands, social activities, and community gatherings — strengthening the overall social fabric of the barangay.</div>
      </div>
    </li>
  </ul>
</div>
<hr class="divider">
""", unsafe_allow_html=True)

# ── TARGET MARKET ──
st.markdown("""
<div class="section reveal" id="market">
  <div class="section-eyebrow reveal reveal-delay-1">04 — Target Market</div>
  <div class="section-title-wrap reveal reveal-delay-2">
    <div class="section-title">Who we<br><em>serve.</em></div>
  </div>
  <div class="market-stats">
    <div class="market-stat-card reveal reveal-delay-2">
      <div class="market-stat-num" data-target="13364" data-suffix="">0</div>
      <div class="market-stat-label">Total residents in Barangay Maguyam, Silang, Cavite</div>
    </div>
    <div class="market-stat-card reveal reveal-delay-3">
      <div class="market-stat-num" data-target="3700" data-suffix="+">0</div>
      <div class="market-stat-label">Households that can be directly served by the project</div>
    </div>
    <div class="market-stat-card reveal reveal-delay-4">
      <div class="market-stat-num">∞</div>
      <div class="market-stat-label">Expansion potential to nearby barangays in Silang municipality</div>
    </div>
  </div>
  <div class="cards-grid" style="margin-top:20px;">
    <div class="card reveal reveal-delay-2">
      <div class="card-icon">🏠</div>
      <div class="card-title">Households</div>
      <div class="card-body">Families who travel at night and need safe, well-lit pathways outside their homes and in surrounding streets.</div>
    </div>
    <div class="card reveal reveal-delay-3">
      <div class="card-icon">🛒</div>
      <div class="card-title">Small Businesses</div>
      <div class="card-body">Sari-sari stores, food stalls, and street vendors who rely on evening customers and benefit from extended operating hours.</div>
    </div>
    <div class="card reveal reveal-delay-4">
      <div class="card-icon">🏛️</div>
      <div class="card-title">Community Leaders</div>
      <div class="card-body">Barangay officials and local leaders who seek to improve public safety and support nighttime economic development.</div>
    </div>
  </div>
</div>
<hr class="divider">
""", unsafe_allow_html=True)

# ── SWOT ──
st.markdown("""
<div class="section reveal" id="swot">
  <div class="section-eyebrow reveal reveal-delay-1">05 — Competitor Landscape</div>
  <div class="section-title-wrap reveal reveal-delay-2">
    <div class="section-title">Where we<br><em>stand out.</em></div>
  </div>
  <p class="section-body reveal reveal-delay-3">
    While electrical contractors and government-led programs focus on infrastructure completion,
    ILLUMILIGHT leads with community engagement — aligning technology with social and
    economic outcomes specific to each barangay.
  </p>
  <div class="swot-grid">
    <div class="swot-card strengths reveal reveal-delay-2">
      <div class="swot-label">Strengths</div>
      <ul class="swot-list">
        <li>Community-centered approach with barangay coordination</li>
        <li>Renewable and zero-electricity-cost solution</li>
        <li>Affordable and easy to install — no infrastructure needed</li>
        <li>Addresses both safety and economic outcomes simultaneously</li>
      </ul>
    </div>
    <div class="swot-card weaknesses reveal reveal-delay-3">
      <div class="swot-label">Weaknesses</div>
      <ul class="swot-list">
        <li>Dependent on daily sunlight for recharging</li>
        <li>Limited illumination range compared to grid-powered lights</li>
        <li>Requires community buy-in and behavioral adoption</li>
        <li>Early-stage enterprise with limited operational track record</li>
      </ul>
    </div>
    <div class="swot-card opportunities reveal reveal-delay-3">
      <div class="swot-label">Opportunities</div>
      <ul class="swot-list">
        <li>Expansion to nearby barangays and municipalities</li>
        <li>Partnerships with barangay, NGOs, and local sponsors</li>
        <li>Growing demand for sustainable and renewable energy</li>
        <li>Government support for green community infrastructure</li>
      </ul>
    </div>
    <div class="swot-card threats reveal reveal-delay-4">
      <div class="swot-label">Threats</div>
      <ul class="swot-list">
        <li>Government street lighting programs as free alternatives</li>
        <li>Community resistance to adopting new products</li>
        <li>Weather and environmental conditions affecting performance</li>
        <li>Funding instability impacting long-term operations</li>
      </ul>
    </div>
  </div>
</div>
<hr class="divider">
""", unsafe_allow_html=True)

# ── TEAM ──
st.markdown("""
<div class="section reveal" id="team">
  <div class="section-eyebrow reveal reveal-delay-1">06 — Management Team</div>
  <div class="section-title-wrap reveal reveal-delay-2">
    <div class="section-title">The people<br><em>behind the light.</em></div>
  </div>
  <div class="team-grid">
    <div class="team-card reveal reveal-delay-1">
      <div class="team-role">Team Leader</div>
      <div class="team-name">Geummuelle Anne Masungsong</div>
      <div class="team-desc">Provides strategic direction, coordinates all project activities, and oversees stakeholder engagement with barangay officials and community leaders.</div>
    </div>
    <div class="team-card reveal reveal-delay-2">
      <div class="team-role">Operations & Logistics</div>
      <div class="team-name">Sophia Cassandra Ambulo</div>
      <div class="team-desc">Manages procurement, distribution, and installation of solar lights — translating the enterprise's plans into on-the-ground outcomes.</div>
    </div>
    <div class="team-card reveal reveal-delay-3">
      <div class="team-role">Marketing & Communications</div>
      <div class="team-name">Marthina Bridgette Casanova</div>
      <div class="team-desc">Designs community campaigns, manages social media outreach, and coordinates public announcements to drive awareness and adoption.</div>
    </div>
    <div class="team-card reveal reveal-delay-3">
      <div class="team-role">Finance Manager</div>
      <div class="team-name">Pauleen Anne Cruz</div>
      <div class="team-desc">Oversees budgeting, expenditure monitoring, and financial reporting — ensuring sustainable and transparent resource management.</div>
    </div>
    <div class="team-card reveal reveal-delay-4">
      <div class="team-role">Product & Technical Lead</div>
      <div class="team-name">Hans Xyrus Lee</div>
      <div class="team-desc">Manages solar light design, installation, and maintenance — providing technical guidance to ensure product durability and community usability.</div>
    </div>
    <div class="team-card reveal reveal-delay-5" style="background:var(--surface2); border-color:var(--gold-border);">
      <div class="team-role" style="color:var(--gold);">Subject Professor</div>
      <div class="team-name">Leomar L. Cabanday</div>
      <div class="team-desc">Business Ethics and Social Responsibility · FEU Cavite Basic Education Department · SY 2025–2026</div>
    </div>
  </div>
</div>
<hr class="divider">
""", unsafe_allow_html=True)

# ── RISKS ──
st.markdown("""
<div class="section reveal" id="risks">
  <div class="section-eyebrow reveal reveal-delay-1">07 — Risk Management</div>
  <div class="section-title-wrap reveal reveal-delay-2">
    <div class="section-title">Risks we've<br><em>planned for.</em></div>
  </div>
  <div class="risk-grid">
    <div class="risk-card reveal reveal-delay-2">
      <div class="risk-num">01</div>
      <div>
        <div class="risk-title">Community Adoption Resistance</div>
        <div class="risk-body">Residents or business owners may be hesitant to switch from traditional lighting sources like kerosene lamps or electric bulbs.</div>
        <div class="risk-mitigation">✓ Mitigation: Community education campaigns + pilot installations in high-traffic areas to build trust and demonstrate value.</div>
      </div>
    </div>
    <div class="risk-card reveal reveal-delay-3">
      <div class="risk-num">02</div>
      <div>
        <div class="risk-title">Product Performance Under Local Conditions</div>
        <div class="risk-body">Solar lights may underperform due to weather exposure, wear over time, or insufficient sunlight during rainy seasons.</div>
        <div class="risk-mitigation">✓ Mitigation: Prioritize high-quality durable units + provide installation guidance and basic maintenance training.</div>
      </div>
    </div>
    <div class="risk-card reveal reveal-delay-4">
      <div class="risk-num">03</div>
      <div>
        <div class="risk-title">Stakeholder Engagement Delays</div>
        <div class="risk-body">Delays or lack of engagement from barangay officials and community leaders could slow installation and reduce project coverage.</div>
        <div class="risk-mitigation">✓ Mitigation: Maintain continuous communication with local authorities and present data-backed safety and economic improvements.</div>
      </div>
    </div>
  </div>
</div>
<hr class="divider">
""", unsafe_allow_html=True)

# ── FOOTER ──
st.markdown("""
<div class="site-footer">
  <div class="site-footer-title">ILLUMILIGHT</div>
  <div class="site-footer-sub">Liwanag sa Daan, Ginhawa sa Bayan</div>
  <div class="footer-pills">
    <span class="footer-pill">Business Ethics & Social Responsibility</span>
    <span class="footer-pill">FEU Cavite Basic Education</span>
    <span class="footer-pill">SY 2025–2026</span>
    <span class="footer-pill">Barangay Maguyam, Silang, Cavite</span>
  </div>
  <div class="footer-copy">
    Ambulo · Casanova · Cruz · Lee · Masungsong &nbsp;|&nbsp; Adviser: Leomar L. Cabanday
  </div>
</div>
""", unsafe_allow_html=True)

# ── JAVASCRIPT ──
st.markdown("""
<script>
(function() {

  // ── Scroll reveal ──
  const revealEls = document.querySelectorAll('.reveal');
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        e.target.classList.add('visible');
        // Also trigger underline on section-title-wrap
        if (e.target.classList.contains('section-title-wrap')) {
          e.target.classList.add('visible');
        }
        observer.unobserve(e.target);
      }
    });
  }, { threshold: 0.12 });
  revealEls.forEach(el => observer.observe(el));

  // ── Counter animation ──
  function animateCounter(el) {
    const target = parseInt(el.getAttribute('data-target'));
    const suffix = el.getAttribute('data-suffix') || '';
    if (!target) return;
    const duration = 1800;
    const start = performance.now();
    function update(now) {
      const elapsed = now - start;
      const progress = Math.min(elapsed / duration, 1);
      const ease = 1 - Math.pow(1 - progress, 4);
      const value = Math.floor(ease * target);
      el.textContent = value.toLocaleString() + suffix;
      if (progress < 1) requestAnimationFrame(update);
    }
    requestAnimationFrame(update);
  }

  const counterObserver = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        animateCounter(e.target);
        counterObserver.unobserve(e.target);
      }
    });
  }, { threshold: 0.5 });

  document.querySelectorAll('[data-target]').forEach(el => counterObserver.observe(el));

  // ── Progress bar ──
  const bar = document.getElementById('progressBar');
  function updateProgress() {
    const scrollTop = window.scrollY || document.documentElement.scrollTop;
    const total = document.documentElement.scrollHeight - window.innerHeight;
    const pct = total > 0 ? (scrollTop / total) * 100 : 0;
    if (bar) bar.style.width = pct + '%';
  }

  // ── Back to top ──
  const btn = document.getElementById('backToTop');
  function updateBackToTop() {
    if (!btn) return;
    if (window.scrollY > 400) btn.classList.add('visible');
    else btn.classList.remove('visible');
  }

  window.addEventListener('scroll', () => {
    updateProgress();
    updateBackToTop();
  }, { passive: true });

  updateProgress();
  updateBackToTop();

})();
</script>
""", unsafe_allow_html=True)
