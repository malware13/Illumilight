import streamlit as st
import base64

st.set_page_config(
    page_title="ILLUMILIGHT — Social Enterprise",
    page_icon="assets/logo.ico",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def get_image_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

try:
    nav_logo_b64 = get_image_base64("assets/nav.png")
    nav_logo_html = f'<img src="data:image/png;base64,{nav_logo_b64}" style="height:56px; width:auto; display:block; object-fit:contain;" />'
except FileNotFoundError:
    nav_logo_html = '<div class="nav-logo">ILLUMI<span>LIGHT</span></div>'

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
  --nav-height: 72px;
}

* { box-sizing: border-box; }
html { scroll-behavior: smooth; }

.nav, .hero, .section, .site-footer,
.card, .card-title, .card-body, .card-icon,
.team-card, .team-name, .team-role, .team-desc,
.outcome-item, .outcome-title, .outcome-body, .outcome-num,
.risk-card, .risk-title, .risk-body, .risk-num, .risk-mitigation,
.swot-card, .swot-label, .swot-list, .swot-list li,
.section-title, .section-eyebrow, .section-body,
.hero-title, .hero-desc, .hero-subtitle-tag, .hero-eyebrow,
.hero-stat, .hero-stat-num, .hero-stat-label,
.highlight-box, .highlight-box-label, .highlight-box-text,
.spec-item, .spec-text, .spec-icon,
.market-stat-card, .market-stat-num, .market-stat-label,
.footer-pill, .footer-copy, .site-footer-title, .site-footer-sub,
.nav-logo, .fin-card, .fin-num, .fin-label, .fin-note,
.mv-card, .mv-label, .mv-text, .sustain-card, .sustain-title, .sustain-body {
  cursor: default !important;
  user-select: none !important;
  -webkit-user-select: none !important;
}

html, body, [class*="css"] { font-family: 'Outfit', sans-serif; background: var(--bg) !important; color: var(--text); }
.stApp {
  background:
    radial-gradient(ellipse 80% 50% at 20% 0%, rgba(93,184,99,0.06) 0%, transparent 60%),
    radial-gradient(ellipse 60% 40% at 80% 100%, rgba(232,184,75,0.07) 0%, transparent 55%),
    var(--bg) !important;
}
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 0 !important; max-width: 100% !important; }

/* ── NAV ── */
.nav {
  position: sticky; top: 0; z-index: 100;
  background: rgba(13,15,10,0.92);
  backdrop-filter: blur(24px);
  border-bottom: 1px solid var(--border);
  padding: 0 40px;
  height: var(--nav-height);
  display: flex; align-items: center; justify-content: space-between;
  gap: 24px;
}
.nav-left { display: flex; align-items: center; height: var(--nav-height); flex-shrink: 0; }
.nav-logo {
  font-family: 'Playfair Display', serif;
  font-size: 1.4rem; font-weight: 900;
  color: var(--gold); letter-spacing: 0.04em;
}
.nav-logo span { color: var(--text); font-weight: 700; }
.nav-links { display: flex; align-items: center; gap: 2px; flex-wrap: wrap; }
.nav-link {
  font-size: 0.68rem; font-weight: 600; letter-spacing: 0.08em;
  text-transform: uppercase; color: var(--text-3);
  text-decoration: none; padding: 6px 10px; border-radius: 6px;
  transition: color 0.2s, background 0.2s;
  cursor: pointer !important;
}
.nav-link:hover { color: var(--gold); background: var(--gold-dim); }

/* ── SECTION ANCHORS ── */
.section-anchor {
  display: block;
  height: var(--nav-height);
  margin-top: calc(-1 * var(--nav-height));
  visibility: hidden;
  pointer-events: none;
}

/* ── HERO ── */
.hero {
  min-height: 92vh; display: flex; flex-direction: column;
  align-items: center; justify-content: center;
  text-align: center; padding: 80px 48px;
  position: relative; overflow: hidden;
}
.hero::before {
  content: "💡"; position: absolute; font-size: 28rem;
  opacity: 0.02; pointer-events: none;
  top: 50%; left: 50%; transform: translate(-50%, -50%);
  filter: blur(2px);
}
.hero-eyebrow {
  display: inline-flex; align-items: center; gap: 8px;
  font-size: 0.72rem; font-weight: 600; letter-spacing: 0.2em;
  text-transform: uppercase; color: var(--green);
  background: var(--green-dim); border: 1px solid rgba(93,184,99,0.25);
  border-radius: 100px; padding: 6px 16px; margin-bottom: 28px;
}
.hero-eyebrow-dot {
  width: 6px; height: 6px; border-radius: 50%; background: var(--green);
  animation: pulse 2s ease-in-out infinite;
}
.hero-title {
  font-family: 'Playfair Display', serif;
  font-size: clamp(3.5rem, 8vw, 7rem); font-weight: 900;
  line-height: 0.95; letter-spacing: -0.02em;
  color: var(--text); margin-bottom: 16px;
}
.hero-title em { font-style: italic; color: var(--gold); }
.hero-subtitle-tag {
  font-family: 'Playfair Display', serif; font-style: italic;
  font-size: 1.3rem; color: var(--text-2); margin-bottom: 32px;
}
.hero-desc {
  max-width: 640px; margin: 0 auto 48px;
  font-size: 1.05rem; line-height: 1.75; color: var(--text-2); font-weight: 300;
}
.hero-stats { display: flex; gap: 48px; justify-content: center; flex-wrap: wrap; }
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
  transition: border-color 0.3s, transform 0.3s;
  position: relative; overflow: hidden;
}
.card::before {
  content: ""; position: absolute; inset: 0;
  background: linear-gradient(135deg, var(--gold-dim), transparent);
  opacity: 0; transition: opacity 0.3s;
}
.card:hover { border-color: var(--gold-border); transform: translateY(-4px); }
.card:hover::before { opacity: 1; }
.card-icon { font-size: 2rem; margin-bottom: 16px; }
.card-title { font-family: 'Playfair Display', serif; font-size: 1.1rem; font-weight: 700; color: var(--text); margin-bottom: 10px; }
.card-body { font-size: 0.9rem; line-height: 1.7; color: var(--text-2); font-weight: 300; }

/* ── MISSION / VISION ── */
.mv-grid { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 20px; margin-top: 40px; }
.mv-card {
  background: var(--surface); border: 1px solid var(--border);
  border-radius: var(--r); padding: 28px; transition: border-color 0.3s;
}
.mv-card.mission { border-top: 2px solid var(--green); }
.mv-card.vision { border-top: 2px solid var(--gold); }
.mv-card.profile { border-top: 2px solid #7b9ee8; }
.mv-label {
  font-size: 0.68rem; font-weight: 700; letter-spacing: 0.18em;
  text-transform: uppercase; margin-bottom: 12px;
}
.mv-card.mission .mv-label { color: var(--green); }
.mv-card.vision .mv-label { color: var(--gold); }
.mv-card.profile .mv-label { color: #7b9ee8; }
.mv-text { font-size: 0.9rem; line-height: 1.75; color: var(--text-2); font-weight: 300; }

/* ── OUTCOMES ── */
.outcomes-list { list-style: none; padding: 0; margin-top: 40px; display: flex; flex-direction: column; gap: 20px; }
.outcome-item {
  display: flex; align-items: flex-start; gap: 20px;
  background: var(--surface); border: 1px solid var(--border);
  border-radius: var(--r); padding: 24px 28px; transition: border-color 0.3s;
}
.outcome-item:hover { border-color: rgba(93,184,99,0.3); }
.outcome-num {
  font-family: 'Playfair Display', serif; font-size: 2.5rem; font-weight: 900;
  color: var(--gold); opacity: 0.3; line-height: 1; flex-shrink: 0; min-width: 48px;
}
.outcome-title { font-size: 1rem; font-weight: 600; color: var(--text); margin-bottom: 6px; }
.outcome-body { font-size: 0.9rem; line-height: 1.7; color: var(--text-2); font-weight: 300; }

/* ── TWO COL ── */
.two-col { display: grid; grid-template-columns: 1fr 1fr; gap: 64px; align-items: start; margin-top: 40px; }

/* ── HIGHLIGHT BOX ── */
.highlight-box {
  background: var(--surface2); border: 1px solid var(--gold-border);
  border-radius: var(--r); padding: 32px; position: relative; overflow: hidden;
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
}
.spec-icon { font-size: 1.2rem; flex-shrink: 0; width: 28px; text-align: center; }
.spec-text { font-size: 0.9rem; color: var(--text-2); font-weight: 300; }
.spec-text strong { color: var(--text); font-weight: 600; }

/* ── MARKET STATS ── */
.market-stats { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin-top: 40px; }
.market-stat-card {
  background: var(--surface); border: 1px solid var(--border);
  border-radius: var(--r); padding: 28px; text-align: center;
}
.market-stat-num {
  font-family: 'Playfair Display', serif;
  font-size: 2.8rem; font-weight: 700; color: var(--gold); line-height: 1;
}
.market-stat-label { font-size: 0.8rem; color: var(--text-2); margin-top: 8px; line-height: 1.5; }

/* ── SWOT ── */
.swot-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-top: 40px; }
.swot-card { background: var(--surface); border: 1px solid var(--border); border-radius: var(--r); padding: 24px; }
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
  border-radius: var(--r); padding: 28px; transition: border-color 0.3s;
}
.team-card:hover { border-color: var(--gold-border); }
.team-role {
  font-size: 0.68rem; font-weight: 600; letter-spacing: 0.15em;
  text-transform: uppercase; color: var(--green); margin-bottom: 8px;
}
.team-name { font-family: 'Playfair Display', serif; font-size: 1.1rem; font-weight: 700; color: var(--text); margin-bottom: 10px; }
.team-desc { font-size: 0.85rem; line-height: 1.7; color: var(--text-2); font-weight: 300; }

/* ── RISK ── */
.risk-grid { display: flex; flex-direction: column; gap: 20px; margin-top: 40px; }
.risk-card {
  display: grid; grid-template-columns: 80px 1fr;
  gap: 24px; align-items: start;
  background: var(--surface); border: 1px solid var(--border);
  border-radius: var(--r); padding: 24px 28px;
}
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

/* ── FINANCIALS ── */
.fin-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin-top: 40px; }
.fin-card {
  background: var(--surface); border: 1px solid var(--border);
  border-radius: var(--r); padding: 28px; text-align: center; transition: border-color 0.3s;
}
.fin-card:hover { border-color: var(--gold-border); }
.fin-num { font-family: 'Playfair Display', serif; font-size: 2.4rem; font-weight: 700; color: var(--gold); line-height: 1; }
.fin-label { font-size: 0.78rem; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase; color: var(--text-3); margin-top: 8px; }
.fin-note { font-size: 0.82rem; color: var(--text-2); margin-top: 10px; line-height: 1.5; font-weight: 300; }
.cost-table { width: 100%; margin-top: 24px; border-collapse: collapse; }
.cost-table th {
  font-size: 0.68rem; font-weight: 700; letter-spacing: 0.15em;
  text-transform: uppercase; color: var(--text-3);
  padding: 8px 12px; text-align: left; border-bottom: 1px solid var(--border);
}
.cost-table td {
  font-size: 0.88rem; color: var(--text-2); font-weight: 300;
  padding: 10px 12px; border-bottom: 1px solid var(--border);
}
.cost-table td:last-child { text-align: right; color: var(--text); font-weight: 500; }
.cost-table tr.total td { color: var(--gold); font-weight: 600; border-top: 1px solid var(--gold-border); border-bottom: none; }

/* ── SUSTAINABILITY ── */
.sustain-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin-top: 40px; }
.sustain-card {
  background: var(--surface); border: 1px solid var(--border);
  border-radius: var(--r); padding: 24px; border-top: 2px solid var(--green);
  transition: border-color 0.3s;
}
.sustain-card:hover { border-color: rgba(93,184,99,0.5); }
.sustain-icon { font-size: 1.8rem; margin-bottom: 12px; }
.sustain-title { font-size: 0.9rem; font-weight: 600; color: var(--text); margin-bottom: 8px; }
.sustain-body { font-size: 0.85rem; line-height: 1.65; color: var(--text-2); font-weight: 300; }

/* ── FOOTER ── */
.site-footer {
  background: var(--surface); border-top: 1px solid var(--border);
  padding: 48px; text-align: center;
}
.site-footer-title {
  font-family: 'Playfair Display', serif;
  font-size: 2rem; font-weight: 900; color: var(--gold); margin-bottom: 8px;
}
.site-footer-sub { font-style: italic; color: var(--text-2); margin-bottom: 28px; }
.footer-pills { display: flex; gap: 10px; justify-content: center; flex-wrap: wrap; }
.footer-pill {
  font-size: 0.72rem; font-weight: 600; letter-spacing: 0.1em;
  text-transform: uppercase; color: var(--text-3);
  border: 1px solid var(--border); border-radius: 100px; padding: 5px 14px;
}
.footer-copy { margin-top: 28px; font-size: 0.78rem; color: var(--text-3); }

@keyframes pulse {
  0%, 100% { opacity: 1; transform: scale(1); }
  50% { opacity: 0.4; transform: scale(0.7); }
}
</style>
""", unsafe_allow_html=True)


# ── NAV ──
st.markdown(f"""
<div class="nav">
  <div class="nav-left">{nav_logo_html}</div>
  <div class="nav-links">
    <a class="nav-link" href="#about">About</a>
    <a class="nav-link" href="#problem">Problem</a>
    <a class="nav-link" href="#solution">Solution</a>
    <a class="nav-link" href="#impact">Impact</a>
    <a class="nav-link" href="#market">Market</a>
    <a class="nav-link" href="#sustainability">Sustainability</a>
    <a class="nav-link" href="#team">Team</a>
    <a class="nav-link" href="#financials">Financials</a>
    <a class="nav-link" href="#risks">Risks</a>
  </div>
</div>
""", unsafe_allow_html=True)


# ── HERO ──
st.markdown("""
<div class="hero">
  <div class="hero-eyebrow">
    <span class="hero-eyebrow-dot"></span>
    Social Enterprise · FEU Cavite Basic Education · SY 2025–2026
  </div>
  <div class="hero-title"><em>ILLUMILIGHT</em></div>
  <div class="hero-subtitle-tag">Liwanag sa Daan, Ginhawa sa Bayan</div>
  <p class="hero-desc">
    A community-centered solar lighting enterprise addressing inadequate street lighting
    in Barangay Maguyam, Silang, Cavite — improving nighttime safety and supporting
    local economic activity through renewable energy.
  </p>
  <div class="hero-stats">
    <div class="hero-stat"><div class="hero-stat-num">13,364</div><div class="hero-stat-label">Residents Served</div></div>
    <div class="hero-stat"><div class="hero-stat-num">3,700+</div><div class="hero-stat-label">Households Addressable</div></div>
    <div class="hero-stat"><div class="hero-stat-num">0₱</div><div class="hero-stat-label">Electricity Cost</div></div>
    <div class="hero-stat"><div class="hero-stat-num">100%</div><div class="hero-stat-label">Solar Powered</div></div>
  </div>
</div>
<hr class="divider">
""", unsafe_allow_html=True)


# ── ABOUT ──
st.markdown("""
<span class="section-anchor" id="about"></span>
<div class="section">
  <div class="section-eyebrow">01 — About Us</div>
  <div class="section-title">Mission, Vision,<br><em>&amp; Company Profile.</em></div>
  <p class="section-body">
    ILLUMILIGHT is a student-led social enterprise founded under FEU Cavite Basic Education's
    Business Ethics and Social Responsibility subject. We exist to address real community
    problems with practical, sustainable solutions.
  </p>
  <div class="mv-grid">
    <div class="mv-card mission">
      <div class="mv-label">Mission</div>
      <div class="mv-text">To provide affordable, solar-powered lighting solutions that improve nighttime safety and support local economic activity in underserved barangays — starting with Barangay Maguyam, Silang, Cavite.</div>
    </div>
    <div class="mv-card vision">
      <div class="mv-label">Vision</div>
      <div class="mv-text">A Philippines where every community — regardless of infrastructure limitations — has access to clean, reliable light that enables people to live, work, and thrive safely after dark.</div>
    </div>
    <div class="mv-card profile">
      <div class="mv-label">Company Profile</div>
      <div class="mv-text">Founded SY 2025–2026 under FEU Cavite Basic Education. A social enterprise focused on renewable energy access for underserved communities through community partnerships, barangay coordination, and direct distribution of solar lighting units.</div>
    </div>
  </div>
</div>
<hr class="divider">
""", unsafe_allow_html=True)


# ── PROBLEM ──
st.markdown("""
<span class="section-anchor" id="problem"></span>
<div class="section">
  <div class="section-eyebrow">02 — The Problem</div>
  <div class="section-title">Dark streets.<br><em>Dimmer futures.</em></div>
  <p class="section-body">
    Barangay Maguyam, home to over 13,000 residents, suffers from inadequate street lighting —
    creating a cycle of insecurity, reduced economic activity, and community isolation that
    disproportionately affects the poorest households.
  </p>
  <div class="cards-grid">
    <div class="card">
      <div class="card-icon">🚶</div>
      <div class="card-title">Mobility &amp; Safety</div>
      <div class="card-body">Poorly lit streets make it dangerous for residents to move at night, reducing access to essential services and increasing the risk of crime and accidents.</div>
    </div>
    <div class="card">
      <div class="card-icon">🏪</div>
      <div class="card-title">Economic Loss</div>
      <div class="card-body">Sari-sari stores, food stalls, and street vendors lose customers after dark — forcing early closures that reduce household income and economic resilience.</div>
    </div>
    <div class="card">
      <div class="card-icon">🌑</div>
      <div class="card-title">Community Isolation</div>
      <div class="card-body">Limited lighting discourages evening social activities, weakening community bonds and reducing collective confidence in shared public spaces.</div>
    </div>
  </div>
  <div class="highlight-box" style="margin-top:32px;">
    <div class="highlight-box-label">Socioeconomic Context</div>
    <div class="highlight-box-text">
      The lack of lighting is not just an infrastructure gap — it is a <strong>socioeconomic barrier</strong>.
      When streets go dark, the informal economy shrinks, families stay indoors, and opportunities
      for community development close with the daylight. For low-income households that depend on
      evening street trade, <strong>darkness means lost livelihood</strong>.
    </div>
  </div>
</div>
<hr class="divider">
""", unsafe_allow_html=True)


# ── SOLUTION ──
st.markdown("""
<span class="section-anchor" id="solution"></span>
<div class="section">
  <div class="section-eyebrow">03 — Our Solution</div>
  <div class="section-title">Hangable solar lights.<br><em>Infinite impact.</em></div>
  <div class="two-col">
    <div>
      <p class="section-body">
        ILLUMILIGHT offers affordable, hangable solar lights that capture sunlight through
        built-in solar panels and store energy in rechargeable batteries — powering bright
        LED lights throughout the night with zero electricity cost.
      </p>
      <p class="section-body" style="margin-top:16px;">
        Unlike decorative solar lanterns, our product is designed specifically for community
        safety: bright enough to illuminate pathways, storefronts, and streets — easy enough
        for any household to install without technical expertise.
      </p>
      <div class="highlight-box" style="margin-top:24px;">
        <div class="highlight-box-label">Value Proposition</div>
        <div class="highlight-box-text">
          ILLUMILIGHT delivers <strong>safe, reliable nighttime light</strong> at a one-time,
          affordable cost — no electricity bills, no wiring, no contractor needed.
          Every unit purchased directly benefits a household and the surrounding street.
        </div>
      </div>
    </div>
    <div>
      <div class="specs-row">
        <div class="spec-item"><span class="spec-icon">☀️</span><span class="spec-text"><strong>Solar-powered</strong> — charges automatically during the day</span></div>
        <div class="spec-item"><span class="spec-icon">🔋</span><span class="spec-text"><strong>Rechargeable batteries</strong> — stores energy for all-night use</span></div>
        <div class="spec-item"><span class="spec-icon">💡</span><span class="spec-text"><strong>High-brightness LEDs</strong> — functional street visibility, not just decorative</span></div>
        <div class="spec-item"><span class="spec-icon">🪝</span><span class="spec-text"><strong>Hangable design</strong> — easy installation on walls, posts, and stalls</span></div>
        <div class="spec-item"><span class="spec-icon">🛠️</span><span class="spec-text"><strong>Installation support</strong> — guidance and maintenance training included</span></div>
        <div class="spec-item"><span class="spec-icon">🌿</span><span class="spec-text"><strong>Zero emissions</strong> — environmentally sustainable energy source</span></div>
        <div class="spec-item"><span class="spec-icon">📦</span><span class="spec-text"><strong>Ready to use</strong> — no electrician, no permits, no infrastructure needed</span></div>
      </div>
    </div>
  </div>
</div>
<hr class="divider">
""", unsafe_allow_html=True)


# ── IMPACT ──
st.markdown("""
<span class="section-anchor" id="impact"></span>
<div class="section">
  <div class="section-eyebrow">04 — Social Impact</div>
  <div class="section-title">What we're<br><em>building toward.</em></div>
  <div class="highlight-box" style="margin-top:32px; max-width:720px;">
    <div class="highlight-box-label">Impact Goal</div>
    <div class="highlight-box-text">
      To improve <strong>nighttime safety</strong> and support <strong>local economic activity</strong>
      in Barangay Maguyam through accessible, renewable outdoor solar lighting — enabling
      residents to move freely and small businesses to operate longer, creating a safer,
      more active, and economically vibrant community.
    </div>
  </div>
  <ul class="outcomes-list">
    <li class="outcome-item">
      <div class="outcome-num">01</div>
      <div>
        <div class="outcome-title">🌟 Safer Streets at Night</div>
        <div class="outcome-body">With solar lights hung outside homes, stores, and pathways, residents can walk outside more safely during evening hours — reducing crime risk and accidents.</div>
      </div>
    </li>
    <li class="outcome-item">
      <div class="outcome-num">02</div>
      <div>
        <div class="outcome-title">📈 More Business Activity at Night</div>
        <div class="outcome-body">Small stores and food vendors can illuminate their stalls — extending operating hours, attracting more customers, and increasing household income.</div>
      </div>
    </li>
    <li class="outcome-item">
      <div class="outcome-num">03</div>
      <div>
        <div class="outcome-title">🤝 Greater Community Confidence</div>
        <div class="outcome-body">Residents feel more comfortable engaging in evening errands, social activities, and community gatherings — strengthening the social fabric of the barangay.</div>
      </div>
    </li>
    <li class="outcome-item">
      <div class="outcome-num">04</div>
      <div>
        <div class="outcome-title">🌱 Environmental Benefit</div>
        <div class="outcome-body">Every solar light displaces kerosene lamp use — reducing carbon emissions, indoor air pollution, and fire risk while modeling sustainable energy adoption.</div>
      </div>
    </li>
  </ul>
</div>
<hr class="divider">
""", unsafe_allow_html=True)


# ── MARKET ──
st.markdown("""
<span class="section-anchor" id="market"></span>
<div class="section">
  <div class="section-eyebrow">05 — Target Market &amp; Market Analysis</div>
  <div class="section-title">Who we<br><em>serve.</em></div>
  <div class="market-stats">
    <div class="market-stat-card">
      <div class="market-stat-num">13,364</div>
      <div class="market-stat-label">Total residents in Barangay Maguyam, Silang, Cavite</div>
    </div>
    <div class="market-stat-card">
      <div class="market-stat-num">3,700+</div>
      <div class="market-stat-label">Households directly addressable in the primary service area</div>
    </div>
    <div class="market-stat-card">
      <div class="market-stat-num">∞</div>
      <div class="market-stat-label">Expansion potential to nearby barangays in Silang municipality</div>
    </div>
  </div>
  <div class="cards-grid" style="margin-top:20px;">
    <div class="card">
      <div class="card-icon">🏠</div>
      <div class="card-title">Households</div>
      <div class="card-body">Families who move around at night and need safe, well-lit pathways. Primary purchasers of individual solar light units.</div>
    </div>
    <div class="card">
      <div class="card-icon">🛒</div>
      <div class="card-title">Small Businesses</div>
      <div class="card-body">Sari-sari stores, food stalls, and street vendors who rely on evening customers and benefit from extended operating hours through better lighting.</div>
    </div>
    <div class="card">
      <div class="card-icon">🏛️</div>
      <div class="card-title">Community Leaders</div>
      <div class="card-body">Barangay officials who seek scalable solutions for public safety and nighttime economic development without large infrastructure budgets.</div>
    </div>
  </div>
  <div class="swot-grid">
    <div class="swot-card strengths">
      <div class="swot-label">Strengths</div>
      <ul class="swot-list">
        <li>Community-centered with direct barangay coordination</li>
        <li>Renewable, zero-electricity-cost solution</li>
        <li>Affordable and easy to install — no infrastructure needed</li>
        <li>Addresses safety and economic outcomes simultaneously</li>
      </ul>
    </div>
    <div class="swot-card weaknesses">
      <div class="swot-label">Weaknesses</div>
      <ul class="swot-list">
        <li>Dependent on daily sunlight for recharging</li>
        <li>Limited illumination range vs. grid-powered lights</li>
        <li>Requires community buy-in and behavioral adoption</li>
        <li>Early-stage with limited operational track record</li>
      </ul>
    </div>
    <div class="swot-card opportunities">
      <div class="swot-label">Opportunities</div>
      <ul class="swot-list">
        <li>Expansion to nearby barangays and municipalities</li>
        <li>Partnerships with NGOs, LGUs, and local sponsors</li>
        <li>Growing demand for sustainable renewable energy</li>
        <li>Government support for green community infrastructure</li>
      </ul>
    </div>
    <div class="swot-card threats">
      <div class="swot-label">Threats</div>
      <ul class="swot-list">
        <li>Government lighting programs as free alternatives</li>
        <li>Community resistance to adopting new products</li>
        <li>Weather conditions affecting solar performance</li>
        <li>Funding instability impacting long-term operations</li>
      </ul>
    </div>
  </div>
</div>
<hr class="divider">
""", unsafe_allow_html=True)


# ── SUSTAINABILITY ──
st.markdown("""
<span class="section-anchor" id="sustainability"></span>
<div class="section">
  <div class="section-eyebrow">06 — Sustainability</div>
  <div class="section-title">Built to<br><em>last.</em></div>
  <p class="section-body">
    ILLUMILIGHT is designed for long-term social and environmental sustainability — not just
    as a one-time project, but as a replicable model for community-led renewable energy access.
  </p>
  <div class="sustain-grid">
    <div class="sustain-card">
      <div class="sustain-icon">♻️</div>
      <div class="sustain-title">Environmental Sustainability</div>
      <div class="sustain-body">Solar-powered units produce zero emissions, displace kerosene usage, and reduce the community's carbon footprint — aligning with national renewable energy goals.</div>
    </div>
    <div class="sustain-card">
      <div class="sustain-icon">💰</div>
      <div class="sustain-title">Economic Sustainability</div>
      <div class="sustain-body">Revenue from unit sales covers procurement costs. Expanded distribution and community partnerships create a self-sustaining model beyond the initial project cycle.</div>
    </div>
    <div class="sustain-card">
      <div class="sustain-icon">🤝</div>
      <div class="sustain-title">Social Sustainability</div>
      <div class="sustain-body">Community education, installation training, and barangay partnership ensure residents can maintain and expand the program independently — building local ownership.</div>
    </div>
    <div class="sustain-card">
      <div class="sustain-icon">📡</div>
      <div class="sustain-title">Scalability</div>
      <div class="sustain-body">The model is barangay-agnostic. After proving impact in Maguyam, ILLUMILIGHT can replicate across neighboring barangays and partner with municipal LGUs for wider rollout.</div>
    </div>
    <div class="sustain-card">
      <div class="sustain-icon">🎓</div>
      <div class="sustain-title">Knowledge Transfer</div>
      <div class="sustain-body">Maintenance training and installation guides are provided with every unit — ensuring communities can sustain the lighting infrastructure independently.</div>
    </div>
    <div class="sustain-card">
      <div class="sustain-icon">🏅</div>
      <div class="sustain-title">SDG Alignment</div>
      <div class="sustain-body">Supports UN SDG 7 (Affordable and Clean Energy), SDG 11 (Sustainable Communities), and SDG 1 (No Poverty) through renewable energy access for underserved communities.</div>
    </div>
  </div>
</div>
<hr class="divider">
""", unsafe_allow_html=True)


# ── TEAM ──
st.markdown("""
<span class="section-anchor" id="team"></span>
<div class="section">
  <div class="section-eyebrow">07 — Management Team</div>
  <div class="section-title">The people<br><em>behind the light.</em></div>
  <div class="team-grid">
    <div class="team-card">
      <div class="team-role">Team Leader</div>
      <div class="team-name">Geummuelle Anne Masungsong</div>
      <div class="team-desc">Provides strategic direction, coordinates all project activities, and oversees stakeholder engagement with barangay officials and community leaders.</div>
    </div>
    <div class="team-card">
      <div class="team-role">Operations &amp; Logistics</div>
      <div class="team-name">Sophia Cassandra Ambulo</div>
      <div class="team-desc">Manages procurement, distribution, and installation of solar lights — translating the enterprise's plans into on-the-ground outcomes.</div>
    </div>
    <div class="team-card">
      <div class="team-role">Marketing &amp; Communications</div>
      <div class="team-name">Marthina Bridgette Casanova</div>
      <div class="team-desc">Designs community campaigns, manages social media outreach, and coordinates public announcements to drive awareness and adoption.</div>
    </div>
    <div class="team-card">
      <div class="team-role">Finance Manager</div>
      <div class="team-name">Pauleen Anne Cruz</div>
      <div class="team-desc">Oversees budgeting, expenditure monitoring, and financial reporting — ensuring sustainable and transparent resource management.</div>
    </div>
    <div class="team-card">
      <div class="team-role">Product &amp; Technical Lead</div>
      <div class="team-name">Hans Xyrus Lee</div>
      <div class="team-desc">Manages solar light design, installation, and maintenance — providing technical guidance to ensure product durability and community usability.</div>
    </div>
    <div class="team-card" style="background: var(--surface2); border-color: var(--gold-border);">
      <div class="team-role" style="color:var(--gold);">Subject Professor</div>
      <div class="team-name">Leomar L. Cabanday</div>
      <div class="team-desc">Business Ethics and Social Responsibility · FEU Cavite Basic Education Department · SY 2025–2026</div>
    </div>
  </div>
</div>
<hr class="divider">
""", unsafe_allow_html=True)


# ── FINANCIALS ──
st.markdown("""
<span class="section-anchor" id="financials"></span>
<div class="section">
  <div class="section-eyebrow">08 — Financial Highlights</div>
  <div class="section-title">The numbers<br><em>behind the light.</em></div>
  <p class="section-body">
    ILLUMILIGHT operates on a lean, cost-recovery model. Revenue from unit sales directly
    covers procurement and operating costs — with a clear path to breakeven in the first
    operational cycle.
  </p>
  <div class="fin-grid">
    <div class="fin-card">
      <div class="fin-num">₱3,500</div>
      <div class="fin-label">Estimated Startup Cost</div>
      <div class="fin-note">Covers initial unit procurement, basic materials, and community outreach for the pilot phase.</div>
    </div>
    <div class="fin-card">
      <div class="fin-num">₱500</div>
      <div class="fin-label">Selling Price Per Unit</div>
      <div class="fin-note">Priced for community affordability while maintaining a sustainable margin above procurement cost.</div>
    </div>
    <div class="fin-card">
      <div class="fin-num">10 units</div>
      <div class="fin-label">Breakeven Volume</div>
      <div class="fin-note">Selling 10 units at ₱500 each recovers the ₱3,500 startup investment plus operating expenses.</div>
    </div>
  </div>
  <div class="highlight-box" style="margin-top:20px;">
    <div class="highlight-box-label">Startup Cost Breakdown</div>
    <table class="cost-table">
      <thead>
        <tr><th>Item</th><th>Details</th><th>Estimated Cost</th></tr>
      </thead>
      <tbody>
        <tr><td>Solar Light Units (initial batch)</td><td>5–7 units for pilot distribution</td><td>₱2,000–₱2,500</td></tr>
        <tr><td>Packaging &amp; Labels</td><td>Basic product packaging</td><td>₱200–₱300</td></tr>
        <tr><td>Community Outreach Materials</td><td>Flyers, printed guides, signage</td><td>₱300–₱400</td></tr>
        <tr><td>Transportation &amp; Distribution</td><td>Delivery to pilot sites in Maguyam</td><td>₱300–₱400</td></tr>
        <tr class="total"><td colspan="2"><strong>Total Estimated Startup Cost</strong></td><td><strong>~₱3,500</strong></td></tr>
      </tbody>
    </table>
  </div>
  <div class="highlight-box" style="margin-top:16px;">
    <div class="highlight-box-label">Revenue Projection &amp; Breakeven</div>
    <div class="highlight-box-text">
      At a selling price of <strong>₱500 per unit</strong>, selling <strong>10 units</strong> generates
      ₱5,000 in revenue — covering the ₱3,500 startup cost and yielding a <strong>~₱1,500 surplus</strong>
      for reinvestment into the next batch. Scaling to 20 units projects ₱10,000 revenue, enabling
      procurement of 30+ units for the next distribution cycle and accelerating community coverage.
    </div>
  </div>
</div>
<hr class="divider">
""", unsafe_allow_html=True)


# ── RISKS ──
st.markdown("""
<span class="section-anchor" id="risks"></span>
<div class="section">
  <div class="section-eyebrow">09 — Risk Management</div>
  <div class="section-title">Risks we've<br><em>planned for.</em></div>
  <div class="risk-grid">
    <div class="risk-card">
      <div class="risk-num">01</div>
      <div>
        <div class="risk-title">Community Adoption Resistance</div>
        <div class="risk-body">Residents or business owners may be hesitant to switch from traditional lighting sources like kerosene lamps or electric bulbs.</div>
        <div class="risk-mitigation">✓ Mitigation: Community education campaigns + pilot installations in high-traffic areas to build trust and demonstrate value before wider rollout.</div>
      </div>
    </div>
    <div class="risk-card">
      <div class="risk-num">02</div>
      <div>
        <div class="risk-title">Product Performance Under Local Conditions</div>
        <div class="risk-body">Solar lights may underperform due to weather exposure, wear over time, or insufficient sunlight during rainy seasons in Cavite.</div>
        <div class="risk-mitigation">✓ Mitigation: Prioritize high-quality durable units + provide installation guidance and basic maintenance training to all recipients.</div>
      </div>
    </div>
    <div class="risk-card">
      <div class="risk-num">03</div>
      <div>
        <div class="risk-title">Stakeholder Engagement Delays</div>
        <div class="risk-body">Delays or lack of engagement from barangay officials could slow installation schedules and reduce project coverage during the pilot phase.</div>
        <div class="risk-mitigation">✓ Mitigation: Maintain continuous communication with local authorities and present data-backed safety and economic impact evidence.</div>
      </div>
    </div>
    <div class="risk-card">
      <div class="risk-num">04</div>
      <div>
        <div class="risk-title">Funding &amp; Resource Constraints</div>
        <div class="risk-body">Limited startup capital may restrict the initial number of units distributed, reducing early-stage community coverage and visibility.</div>
        <div class="risk-mitigation">✓ Mitigation: Phased rollout starting with a small pilot batch — reinvesting revenue from initial sales to fund subsequent procurement cycles.</div>
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
    <span class="footer-pill">Business Ethics &amp; Social Responsibility</span>
    <span class="footer-pill">FEU Cavite Basic Education</span>
    <span class="footer-pill">SY 2025–2026</span>
    <span class="footer-pill">Barangay Maguyam, Silang, Cavite</span>
  </div>
  <div class="footer-copy">
    Ambulo · Casanova · Cruz · Lee · Masungsong &nbsp;|&nbsp; Adviser: Leomar L. Cabanday
  </div>
</div>
""", unsafe_allow_html=True)
