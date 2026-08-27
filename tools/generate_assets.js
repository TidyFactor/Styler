const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const repoRoot = path.resolve(__dirname, '..');
const assetsDir = path.join(repoRoot, 'assets');

if (!fs.existsSync(assetsDir)) {
  fs.mkdirSync(assetsDir, { recursive: true });
}

// 1. GitHub Social Preview (1280x640)
const socialPreviewHtml = `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>TidyFactor Styler - Social Preview</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      width: 1280px;
      height: 640px;
      background: #080B11;
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      color: #F3F4F6;
      display: flex;
      align-items: center;
      justify-content: center;
      position: relative;
      overflow: hidden;
      -webkit-font-smoothing: antialiased;
    }

    .glow-1 {
      position: absolute;
      top: -150px;
      left: -100px;
      width: 650px;
      height: 650px;
      background: radial-gradient(circle, rgba(2, 132, 199, 0.22) 0%, rgba(8, 11, 17, 0) 70%);
      filter: blur(40px);
      pointer-events: none;
    }
    .glow-2 {
      position: absolute;
      bottom: -150px;
      right: -100px;
      width: 750px;
      height: 750px;
      background: radial-gradient(circle, rgba(16, 185, 129, 0.22) 0%, rgba(8, 11, 17, 0) 70%);
      filter: blur(50px);
      pointer-events: none;
    }
    .glow-3 {
      position: absolute;
      top: 40%;
      right: 25%;
      width: 450px;
      height: 450px;
      background: radial-gradient(circle, rgba(168, 85, 247, 0.15) 0%, rgba(8, 11, 17, 0) 70%);
      filter: blur(60px);
      pointer-events: none;
    }

    .grid-bg {
      position: absolute;
      inset: 0;
      background-image: 
        linear-gradient(to right, rgba(255, 255, 255, 0.04) 1px, transparent 1px),
        linear-gradient(to bottom, rgba(255, 255, 255, 0.04) 1px, transparent 1px);
      background-size: 40px 40px;
      mask-image: radial-gradient(circle at 50% 50%, black 50%, transparent 95%);
      pointer-events: none;
    }

    .container {
      width: 1160px;
      height: 520px;
      display: grid;
      grid-template-columns: 1.18fr 0.82fr;
      gap: 36px;
      position: relative;
      z-index: 10;
    }

    .left-col {
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }

    .top-meta {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .brand-pill {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 6px 14px;
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.12);
      border-radius: 999px;
      font-size: 13px;
      font-weight: 600;
      letter-spacing: 0.5px;
      color: #9CA3AF;
      text-transform: uppercase;
    }

    .brand-dot {
      width: 8px;
      height: 8px;
      background: #0284C7;
      border-radius: 50%;
      box-shadow: 0 0 10px #0284C7;
    }

    .version-badge {
      display: inline-flex;
      align-items: center;
      padding: 4px 10px;
      background: rgba(2, 132, 199, 0.15);
      border: 1px solid rgba(2, 132, 199, 0.35);
      color: #38BDF8;
      font-family: 'JetBrains Mono', monospace;
      font-size: 12px;
      font-weight: 700;
      border-radius: 6px;
    }

    .title-group {
      margin-top: 14px;
    }

    .main-title {
      font-size: 52px;
      font-weight: 800;
      letter-spacing: -1.5px;
      line-height: 1.08;
      color: #FFFFFF;
    }

    .main-title span {
      background: linear-gradient(135deg, #38BDF8 0%, #34D399 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .tagline {
      margin-top: 12px;
      font-size: 18px;
      line-height: 1.45;
      color: #94A3B8;
      font-weight: 500;
      max-width: 580px;
    }

    .features-list {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin-top: 18px;
    }

    .feature-tag {
      display: flex;
      align-items: center;
      gap: 8px;
      padding: 8px 14px;
      background: rgba(15, 23, 42, 0.75);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 8px;
      font-size: 13px;
      font-weight: 600;
      color: #E2E8F0;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
    }

    .feature-tag svg {
      width: 16px;
      height: 16px;
      color: #38BDF8;
    }

    .footer-bar {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding-top: 18px;
      border-top: 1px solid rgba(255, 255, 255, 0.08);
    }

    .agents-group {
      display: flex;
      align-items: center;
      gap: 10px;
      font-size: 12px;
      color: #64748B;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }

    .agent-pill {
      color: #CBD5E1;
      background: rgba(255, 255, 255, 0.05);
      padding: 4px 10px;
      border-radius: 6px;
      border: 1px solid rgba(255, 255, 255, 0.08);
    }

    .right-col {
      display: flex;
      flex-direction: column;
      justify-content: center;
    }

    .card-stack {
      position: relative;
      width: 100%;
    }

    .code-card {
      background: rgba(11, 15, 25, 0.9);
      border: 1px solid rgba(56, 189, 248, 0.3);
      border-radius: 14px;
      box-shadow: 
        0 20px 40px -15px rgba(0, 0, 0, 0.7),
        0 0 30px rgba(56, 189, 248, 0.12);
      backdrop-filter: blur(16px);
      overflow: hidden;
    }

    .card-header {
      padding: 12px 18px;
      background: rgba(255, 255, 255, 0.03);
      border-bottom: 1px solid rgba(255, 255, 255, 0.06);
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .dots { display: flex; gap: 6px; }
    .dot { width: 10px; height: 10px; border-radius: 50%; }
    .dot.red { background: #EF4444; }
    .dot.yellow { background: #F59E0B; }
    .dot.green { background: #10B981; }

    .card-title {
      font-family: 'JetBrains Mono', monospace;
      font-size: 12px;
      color: #94A3B8;
      font-weight: 500;
    }

    .shield-badge {
      display: flex;
      align-items: center;
      gap: 5px;
      font-size: 11px;
      font-weight: 700;
      color: #38BDF8;
      background: rgba(2, 132, 199, 0.12);
      border: 1px solid rgba(2, 132, 199, 0.25);
      padding: 2px 8px;
      border-radius: 4px;
    }

    .code-body {
      padding: 18px;
      font-family: 'JetBrains Mono', monospace;
      font-size: 12px;
      line-height: 1.6;
      color: #E2E8F0;
    }

    .kwd { color: #F472B6; font-weight: 600; }
    .prop { color: #38BDF8; font-weight: 600; }
    .val { color: #34D399; }
    .comment { color: #64748B; font-style: italic; }

    .terminal-card {
      margin-top: 14px;
      background: rgba(15, 23, 42, 0.95);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 10px;
      padding: 12px 16px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-family: 'JetBrains Mono', monospace;
      font-size: 13px;
    }

    .cmd-text {
      color: #38BDF8;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .cmd-text span { color: #E2E8F0; }
    .cmd-prompt { color: #34D399; font-weight: 700; }

    .badge-13 {
      background: linear-gradient(135deg, rgba(56, 189, 248, 0.2), rgba(52, 211, 153, 0.25));
      border: 1px solid rgba(56, 189, 248, 0.4);
      color: #F8FAFC;
      font-size: 11px;
      font-weight: 700;
      padding: 3px 8px;
      border-radius: 6px;
    }
  </style>
</head>
<body>
  <div class="glow-1"></div>
  <div class="glow-2"></div>
  <div class="glow-3"></div>
  <div class="grid-bg"></div>

  <div class="container">
    <div class="left-col">
      <div>
        <div class="top-meta">
          <div class="brand-pill">
            <span class="brand-dot"></span>
            TidyFactor Ecosystem
          </div>
          <span class="version-badge">v1.1.1 RELEASE</span>
        </div>

        <div class="title-group">
          <h1 class="main-title">TidyFactor <span>Styler</span></h1>
          <p class="tagline">Production framework styler, surgical RTL redesign &amp; anti-slop UI engineering engine across React, PHP, WordPress &amp; HTML.</p>
        </div>

        <div class="features-list">
          <div class="feature-tag">
            <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 21a4 4 0 01-4-4V5a2 2 0 012-2h4a2 2 0 012 2v12a4 4 0 01-4 4zm0 0h12a2 2 0 002-2v-4a2 2 0 00-2-2h-2.343M11 7.343l1.657-1.657a2 2 0 012.828 0l2.829 2.829a2 2 0 010 2.828l-8.486 8.485M7 17h.01"/></svg>
            Conform, Don't Compete
          </div>
          <div class="feature-tag">
            <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5h12M9 3v2m1.048 9.5A18.022 18.022 0 016.412 9m6.088 9h7M11 21l5-10 5 10M12.751 5C11.783 10.77 8.07 15.61 3 18.129"/></svg>
            Surgical RTL &amp; Arabic
          </div>
          <div class="feature-tag">
            <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
            Anti-Slop Certified
          </div>
          <div class="feature-tag">
            <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"/></svg>
            8-State Interaction Matrix
          </div>
        </div>
      </div>

      <div class="footer-bar">
        <div class="agents-group">
          <span>AI Agents:</span>
          <span class="agent-pill">Antigravity</span>
          <span class="agent-pill">Claude Code</span>
          <span class="agent-pill">Cursor</span>
          <span class="agent-pill">Codex</span>
        </div>
        <div class="badge-13">13 SLASH COMMANDS</div>
      </div>
    </div>

    <div class="right-col">
      <div class="card-stack">
        <div class="code-card">
          <div class="card-header">
            <div class="dots">
              <div class="dot red"></div>
              <div class="dot yellow"></div>
              <div class="dot green"></div>
            </div>
            <div class="card-title">rtl-logical-properties.css</div>
            <div class="shield-badge">📐 LOGICAL RTL</div>
          </div>
          <div class="code-body">
            <span class="comment">/* Direction-agnostic logical properties */</span><br/>
            .<span class="kwd">styler-component</span> {<br/>
            &nbsp;&nbsp;<span class="prop">margin-inline-start</span>: <span class="val">1.5rem</span>;<br/>
            &nbsp;&nbsp;<span class="prop">padding-inline-end</span>: <span class="val">1.25rem</span>;<br/>
            &nbsp;&nbsp;<span class="prop">inset-inline-start</span>: <span class="val">0</span>;<br/>
            &nbsp;&nbsp;<span class="prop">text-align</span>: <span class="val">start</span>;<br/>
            &nbsp;&nbsp;<span class="prop">border-start-start-radius</span>: <span class="val">0.75rem</span>;<br/>
            }
          </div>
        </div>

        <div class="terminal-card">
          <div class="cmd-text">
            <span class="cmd-prompt">$</span>
            <span>npx @alwkala/tidyfactor-styler add-skill</span>
          </div>
          <div class="shield-badge">⚡ INSTANT INJECT</div>
        </div>
      </div>
    </div>
  </div>
</body>
</html>
`;

// 2. Demo Hero Showcase Dark (1440x900)
const demoHeroDarkHtml = `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>TidyFactor Styler - Demo Hero</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      width: 1440px;
      height: 900px;
      background: #080B11;
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      color: #F8FAFC;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 32px 48px;
      position: relative;
      overflow: hidden;
      -webkit-font-smoothing: antialiased;
    }

    .ambient-glow-top {
      position: absolute;
      top: -120px;
      left: 50%;
      transform: translateX(-50%);
      width: 950px;
      height: 450px;
      background: radial-gradient(ellipse, rgba(2, 132, 199, 0.18) 0%, rgba(52, 211, 153, 0.14) 40%, rgba(8, 11, 17, 0) 70%);
      filter: blur(50px);
      pointer-events: none;
    }

    .grid-pattern {
      position: absolute;
      inset: 0;
      background-image: 
        linear-gradient(to right, rgba(255, 255, 255, 0.035) 1px, transparent 1px),
        linear-gradient(to bottom, rgba(255, 255, 255, 0.035) 1px, transparent 1px);
      background-size: 48px 48px;
      mask-image: radial-gradient(circle at 50% 35%, black 55%, transparent 95%);
      pointer-events: none;
    }

    .hero-container {
      width: 100%;
      max-width: 1220px;
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      position: relative;
      z-index: 10;
    }

    .top-pill {
      display: inline-flex;
      align-items: center;
      gap: 10px;
      padding: 6px 20px;
      background: rgba(15, 23, 42, 0.85);
      border: 1px solid rgba(255, 255, 255, 0.12);
      border-radius: 999px;
      font-size: 13px;
      font-weight: 600;
      color: #94A3B8;
      box-shadow: 0 4px 16px rgba(0, 0, 0, 0.3);
      margin-bottom: 20px;
    }
    .top-pill .dot {
      width: 8px;
      height: 8px;
      background: #0284C7;
      border-radius: 50%;
      box-shadow: 0 0 10px #0284C7;
    }
    .top-pill b { color: #F8FAFC; }

    .headline {
      font-size: 48px;
      font-weight: 800;
      letter-spacing: -1.5px;
      line-height: 1.15;
      max-width: 1020px;
      margin-bottom: 14px;
    }
    .headline .gradient-text {
      background: linear-gradient(135deg, #38BDF8 0%, #34D399 60%, #A78BFA 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .description {
      font-size: 17px;
      line-height: 1.5;
      color: #94A3B8;
      max-width: 860px;
      margin-bottom: 26px;
    }

    .button-group {
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 28px;
    }
    .btn {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 10px 20px;
      border-radius: 9px;
      font-size: 13px;
      font-weight: 700;
      text-decoration: none;
    }
    .btn-primary {
      background: #F8FAFC;
      color: #080B11;
      box-shadow: 0 4px 20px rgba(255, 255, 255, 0.2);
    }
    .btn-secondary {
      background: rgba(255, 255, 255, 0.05);
      color: #F1F5F9;
      border: 1px solid rgba(255, 255, 255, 0.12);
    }

    .terminal-box {
      width: 100%;
      max-width: 820px;
      background: rgba(11, 15, 25, 0.95);
      border: 1px solid rgba(255, 255, 255, 0.12);
      border-radius: 12px;
      box-shadow: 0 16px 40px rgba(0, 0, 0, 0.5);
      overflow: hidden;
      margin-bottom: 24px;
    }
    .terminal-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 8px 16px;
      background: rgba(255, 255, 255, 0.03);
      border-bottom: 1px solid rgba(255, 255, 255, 0.06);
    }
    .term-dots { display: flex; gap: 6px; }
    .term-dot { width: 10px; height: 10px; border-radius: 50%; }
    .term-dot.r { background: #EF4444; }
    .term-dot.y { background: #F59E0B; }
    .term-dot.g { background: #10B981; }
    .term-title {
      font-family: 'JetBrains Mono', monospace;
      font-size: 11px;
      color: #64748B;
    }
    .terminal-content {
      padding: 14px 22px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-family: 'JetBrains Mono', monospace;
      font-size: 14px;
    }
    .term-cmd { display: flex; align-items: center; gap: 12px; }
    .term-prompt { color: #34D399; font-weight: 700; }
    .term-code { color: #38BDF8; font-weight: 600; }
    .copy-btn {
      padding: 4px 10px;
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(255, 255, 255, 0.12);
      border-radius: 5px;
      color: #E2E8F0;
      font-size: 11px;
      font-weight: 600;
    }

    .commands-card {
      width: 100%;
      max-width: 1120px;
      background: rgba(15, 23, 42, 0.75);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 14px;
      padding: 20px 24px;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
      backdrop-filter: blur(12px);
    }
    .commands-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 14px;
    }
    .commands-title {
      font-size: 13px;
      font-weight: 700;
      color: #CBD5E1;
      display: flex;
      align-items: center;
      gap: 8px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }
    .commands-title span { color: #38BDF8; }
    .commands-count {
      font-family: 'JetBrains Mono', monospace;
      font-size: 11px;
      color: #38BDF8;
      background: rgba(2, 132, 199, 0.15);
      border: 1px solid rgba(2, 132, 199, 0.3);
      padding: 3px 8px;
      border-radius: 5px;
      font-weight: 700;
    }
    .commands-grid {
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      gap: 8px;
    }
    .cmd-pill {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 8px 10px;
      background: rgba(11, 15, 25, 0.9);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 7px;
      font-family: 'JetBrains Mono', monospace;
      font-size: 12px;
      color: #E2E8F0;
      box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
    }
    .cmd-pill .name { color: #F8FAFC; font-weight: 600; }
    .cmd-pill .prefix { color: #38BDF8; font-weight: 700; }
    .cmd-pill .icon { color: #64748B; font-size: 10px; }
  </style>
</head>
<body>
  <div class="ambient-glow-top"></div>
  <div class="grid-pattern"></div>

  <div class="hero-container">
    <div class="top-pill">
      <span class="dot"></span>
      <span>PRODUCTION FRAMEWORK STYLER • <b>SURGICAL RTL REDESIGN</b> • ZERO PER-PAGE CSS DRIFT</span>
    </div>

    <h1 class="headline">
      TidyFactor Styler<br/>
      <span class="gradient-text">Production UI Engineering For Any Web Framework</span>
    </h1>

    <p class="description">
      Surgically restyle and build components, sections, and pages directly inside your live codebase (React, PHP, WordPress, HTML) with native Arabic RTL correctness.
    </p>

    <div class="button-group">
      <div class="btn btn-primary">Production Styler Guide →</div>
      <div class="btn btn-secondary">Download .skill Package</div>
      <div class="btn btn-secondary">GitHub Repository ↗</div>
      <div class="btn btn-secondary">NPM Package ↗</div>
    </div>

    <div class="terminal-box">
      <div class="terminal-header">
        <div class="term-dots">
          <div class="term-dot r"></div>
          <div class="term-dot y"></div>
          <div class="term-dot g"></div>
        </div>
        <div class="term-title">bash — AI Agent Quick-Install Command</div>
        <div></div>
      </div>
      <div class="terminal-content">
        <div class="term-cmd">
          <span class="term-prompt">$</span>
          <span class="term-code">npx @alwkala/tidyfactor-styler add-skill</span>
        </div>
        <div class="copy-btn">Copy</div>
      </div>
    </div>

    <div class="commands-card">
      <div class="commands-header">
        <div class="commands-title">
          <span>&gt;_</span> Precision Styler Commands &amp; Workflows
        </div>
        <div class="commands-count">13 Operational Commands</div>
      </div>

      <div class="commands-grid">
        <div class="cmd-pill"><span class="prefix">$/</span><span class="name">brief</span><span class="icon">CDL Brief</span></div>
        <div class="cmd-pill"><span class="prefix">$/</span><span class="name">component</span><span class="icon">Component UI</span></div>
        <div class="cmd-pill"><span class="prefix">$/</span><span class="name">section</span><span class="icon">Section UI</span></div>
        <div class="cmd-pill"><span class="prefix">$/</span><span class="name">page</span><span class="icon">Page Assembly</span></div>
        <div class="cmd-pill"><span class="prefix">$/</span><span class="name">redesign</span><span class="icon">Full Redesign</span></div>

        <div class="cmd-pill"><span class="prefix">$/</span><span class="name">layout</span><span class="icon">8 Archetypes</span></div>
        <div class="cmd-pill"><span class="prefix">$/</span><span class="name">nav-footer</span><span class="icon">N1-N9 &amp; Ft1-Ft8</span></div>
        <div class="cmd-pill"><span class="prefix">$/</span><span class="name">typography</span><span class="icon">Arabic Pairings</span></div>
        <div class="cmd-pill"><span class="prefix">$/</span><span class="name">palette</span><span class="icon">WCAG AA Tokens</span></div>
        <div class="cmd-pill"><span class="prefix">$/</span><span class="name">assets</span><span class="icon">Image Tooling</span></div>

        <div class="cmd-pill"><span class="prefix">$/</span><span class="name">rtl</span><span class="icon">RTL Audit &amp; Fix</span></div>
        <div class="cmd-pill"><span class="prefix">$/</span><span class="name">motion</span><span class="icon">Interaction</span></div>
        <div class="cmd-pill"><span class="prefix">$/</span><span class="name">styles</span><span class="icon">Design School</span></div>
      </div>
    </div>
  </div>
</body>
</html>
`;

// 3. Demo Stacks & RTL Pipeline Diagram (1280x640)
const demoRtlPipelineHtml = `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>TidyFactor Styler - Production Engineering Pipeline</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      width: 1280px;
      height: 640px;
      background: #080B11;
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      color: #F8FAFC;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 40px;
      position: relative;
      overflow: hidden;
      -webkit-font-smoothing: antialiased;
    }

    .ambient-glow {
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      width: 900px;
      height: 400px;
      background: radial-gradient(ellipse, rgba(2, 132, 199, 0.15) 0%, rgba(52, 211, 153, 0.12) 50%, transparent 75%);
      filter: blur(50px);
      pointer-events: none;
    }

    .grid-bg {
      position: absolute;
      inset: 0;
      background-image: 
        linear-gradient(to right, rgba(255, 255, 255, 0.03) 1px, transparent 1px),
        linear-gradient(to bottom, rgba(255, 255, 255, 0.03) 1px, transparent 1px);
      background-size: 40px 40px;
      pointer-events: none;
    }

    .container {
      width: 100%;
      max-width: 1180px;
      position: relative;
      z-index: 10;
      display: flex;
      flex-direction: column;
      align-items: center;
    }

    .header {
      text-align: center;
      margin-bottom: 36px;
    }

    .header-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 4px 12px;
      background: rgba(2, 132, 199, 0.15);
      border: 1px solid rgba(2, 132, 199, 0.35);
      border-radius: 999px;
      color: #38BDF8;
      font-size: 12px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-bottom: 10px;
    }

    .header-title {
      font-size: 32px;
      font-weight: 800;
      letter-spacing: -1px;
      color: #FFFFFF;
    }

    .pipeline-grid {
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      gap: 16px;
      width: 100%;
    }

    .step-card {
      background: rgba(15, 23, 42, 0.85);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 12px;
      padding: 22px 16px;
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
    }

    .step-card.highlight {
      border-color: rgba(56, 189, 248, 0.4);
      background: rgba(11, 25, 35, 0.85);
      box-shadow: 0 0 25px rgba(56, 189, 248, 0.15);
    }

    .step-num {
      width: 26px;
      height: 26px;
      background: rgba(255, 255, 255, 0.1);
      border-radius: 50%;
      font-size: 12px;
      font-weight: 700;
      display: flex;
      align-items: center;
      justify-content: center;
      color: #94A3B8;
      margin-bottom: 14px;
    }

    .step-card.highlight .step-num {
      background: #0284C7;
      color: #FFFFFF;
    }

    .step-icon-svg {
      width: 32px;
      height: 32px;
      margin-bottom: 12px;
      color: #38BDF8;
    }

    .step-card.highlight .step-icon-svg {
      color: #34D399;
    }

    .step-title {
      font-size: 15px;
      font-weight: 700;
      color: #F8FAFC;
      margin-bottom: 8px;
    }

    .step-desc {
      font-size: 12px;
      color: #94A3B8;
      line-height: 1.45;
      font-family: 'JetBrains Mono', monospace;
    }
  </style>
</head>
<body>
  <div class="ambient-glow"></div>
  <div class="grid-bg"></div>

  <div class="container">
    <div class="header">
      <div class="header-badge">🛡️ Zero Style Drift Guarantee</div>
      <h2 class="header-title">Production UI Transformation Lifecycle</h2>
    </div>

    <div class="pipeline-grid">
      <div class="step-card">
        <div class="step-num">1</div>
        <svg class="step-icon-svg" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
        <div class="step-title">Stack Detection</div>
        <div class="step-desc">Next.js / PHP / WP / HTML (Conform, Don't Compete)</div>
      </div>

      <div class="step-card">
        <div class="step-num">2</div>
        <svg class="step-icon-svg" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 21a4 4 0 01-4-4V5a2 2 0 012-2h4a2 2 0 012 2v12a4 4 0 01-4 4zm0 0h12a2 2 0 002-2v-4a2 2 0 00-2-2h-2.343M11 7.343l1.657-1.657a2 2 0 012.828 0l2.829 2.829a2 2 0 010 2.828l-8.486 8.485M7 17h.01"/></svg>
        <div class="step-title">Brand Tokens</div>
        <div class="step-desc">brand.json → Native CSS Vars / Tailwind Config</div>
      </div>

      <div class="step-card">
        <div class="step-num">3</div>
        <svg class="step-icon-svg" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 5a1 1 0 011-1h14a1 1 0 011 1v2a1 1 0 01-1 1H5a1 1 0 01-1-1V5zM4 13a1 1 0 011-1h6a1 1 0 011 1v6a1 1 0 01-1 1H5a1 1 0 01-1-1v-6zM16 13a1 1 0 011-1h2a1 1 0 011 1v6a1 1 0 01-1 1h-2a1 1 0 01-1-1v-6z"/></svg>
        <div class="step-title">Scoped Redesign</div>
        <div class="step-desc">8-State interaction matrix &amp; CVA variants</div>
      </div>

      <div class="step-card highlight">
        <div class="step-num">4</div>
        <svg class="step-icon-svg" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5h12M9 3v2m1.048 9.5A18.022 18.022 0 016.412 9m6.088 9h7M11 21l5-10 5 10M12.751 5C11.783 10.77 8.07 15.61 3 18.129"/></svg>
        <div class="step-title">Logical RTL CSS</div>
        <div class="step-desc">Direction-agnostic start/end &amp; Arabic typography</div>
      </div>

      <div class="step-card highlight">
        <div class="step-num">5</div>
        <svg class="step-icon-svg" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
        <div class="step-title">Anti-Slop Audit</div>
        <div class="step-desc">6-Axis pre-emit self-critique pass</div>
      </div>
    </div>
  </div>
</body>
</html>
`;

fs.writeFileSync(path.join(assetsDir, 'github-social-preview.html'), socialPreviewHtml, 'utf8');
fs.writeFileSync(path.join(assetsDir, 'demo-hero-dark.html'), demoHeroDarkHtml, 'utf8');
fs.writeFileSync(path.join(assetsDir, 'demo-rtl-pipeline.html'), demoRtlPipelineHtml, 'utf8');

console.log('[generate_assets] Styler HTML templates written to assets/');

const chromePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";
const edgePath = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe";

let browserExe = fs.existsSync(chromePath) ? chromePath : (fs.existsSync(edgePath) ? edgePath : null);

if (browserExe) {
  console.log(`[generate_assets] Using browser executable: ${browserExe}`);

  const render = (htmlFile, outFile, width, height) => {
    const fileUrl = 'file:///' + path.join(assetsDir, htmlFile).replace(/\\\\/g, '/');
    const outPath = path.join(assetsDir, outFile);
    const cmd = `"${browserExe}" --headless --disable-gpu --screenshot="${outPath}" --window-size=${width},${height} --default-background-color=00000000 --hide-scrollbars "${fileUrl}"`;
    console.log(`[generate_assets] Rendering ${outFile} (${width}x${height})...`);
    execSync(cmd, { stdio: 'inherit' });
  };

  try {
    render('github-social-preview.html', 'github-social-preview.png', 1280, 640);
    fs.copyFileSync(path.join(assetsDir, 'github-social-preview.png'), path.join(assetsDir, 'og-default.png'));
    render('demo-hero-dark.html', 'demo-hero-dark.png', 1440, 900);
    render('demo-rtl-pipeline.html', 'demo-rtl-pipeline.png', 1280, 640);
    console.log('[generate_assets] ✓ All Styler PNG assets successfully rendered and saved to assets/!');
  } catch (err) {
    console.error('[generate_assets] Error rendering with browser:', err.message);
  }
}
