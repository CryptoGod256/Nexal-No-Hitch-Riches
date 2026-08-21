#!/usr/bin/env bash
set -e

mkdir -p ~/nexal-intelligence/public && cd ~/nexal-intelligence/public

cat << 'HTML' > index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NEXAL.intel // Digital NeGron World Feed</title>
    <link href="https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-deep: #050505;
            --bg-panel: #0d0e12;
            --bg-card: #13151b;
            --border-color: #22252a;
            --neon-red: #ff2a2a;
            --neon-green: #39ff14;
            --neon-cyan: #00f0ff;
            --neon-gold: #ffbd2e;
            --text-main: #f0f0f5;
            --text-muted: #8a8d9b;
        }

        * { box-sizing: border-box; margin: 0; padding: 0; }
        body { background-color: var(--bg-deep); color: var(--text-main); font-family: 'Inter', sans-serif; overflow-x: hidden; }
        code, pre, .mono { font-family: 'Share Tech Mono', monospace; }

        /* Terminal Bar */
        .terminal-header {
            background: #000;
            border-bottom: 1px solid var(--border-color);
            padding: 8px 16px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 6px;
            font-size: 0.8rem;
            color: var(--text-muted);
        }
        .terminal-dots span { height: 10px; width: 10px; display: inline-block; border-radius: 50%; margin-right: 6px; }
        .dot-red { background: #ff5f56; } .dot-yellow { background: #ffbd2e; } .dot-green { background: #27c93f; }

        /* Top Navigation */
        nav {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 12px 20px;
            border-bottom: 1px solid var(--border-color);
            background: rgba(5, 5, 5, 0.95);
            position: sticky;
            top: 0;
            z-index: 1000;
        }
        .brand { font-family: 'Share Tech Mono', monospace; font-size: 1.4rem; font-weight: bold; color: #fff; letter-spacing: 2px; white-space: nowrap; }
        .brand span { color: var(--neon-red); text-shadow: 0 0 10px rgba(255, 42, 42, 0.5); }

        .nav-links { display: flex; gap: 6px; list-style: none; white-space: nowrap; overflow-x: auto; padding-bottom: 4px; }
        .nav-links button {
            background: transparent;
            border: 1px solid transparent;
            color: var(--text-muted);
            font-family: 'Share Tech Mono', monospace;
            font-size: 0.8rem;
            cursor: pointer;
            transition: 0.2s;
            padding: 6px 10px;
            border-radius: 6px;
        }
        .nav-links button:hover, .nav-links button.active {
            color: var(--neon-cyan);
            background: rgba(0, 240, 255, 0.08);
            border-color: rgba(0, 240, 255, 0.4);
        }

        .coin-badge {
            background: rgba(0, 240, 255, 0.1);
            border: 1px solid var(--neon-cyan);
            color: var(--neon-cyan);
            padding: 5px 12px;
            border-radius: 20px;
            font-size: 0.8rem;
            font-family: 'Share Tech Mono', monospace;
            white-space: nowrap;
        }

        /* App Layout Container */
        .app-section { display: none; padding: 16px; max-width: 800px; margin: 0 auto; }
        .app-section.active { display: block; }

        /* YOUTUBE-STYLE FILTER CHIPS */
        .feed-filter-bar {
            display: flex;
            gap: 8px;
            overflow-x: auto;
            padding-bottom: 12px;
            margin-bottom: 16px;
            scrollbar-width: none;
        }
        .feed-filter-bar::-webkit-scrollbar { display: none; }
        .chip {
            background: #181b22;
            border: 1px solid var(--border-color);
            color: #d0d0d5;
            padding: 6px 14px;
            border-radius: 8px;
            font-size: 0.85rem;
            font-weight: 500;
            white-space: nowrap;
            cursor: pointer;
            transition: all 0.2s;
        }
        .chip:hover { background: #222632; }
        .chip.active {
            background: #ffffff;
            color: #000000;
            font-weight: 600;
            border-color: #ffffff;
        }

        /* FEED SECTION GROUP TITLE */
        .feed-group-title {
            font-family: 'Share Tech Mono', monospace;
            font-size: 0.85rem;
            color: var(--text-muted);
            letter-spacing: 1px;
            margin: 18px 0 10px 4px;
            text-transform: uppercase;
        }

        /* YOUTUBE-STYLE FEED NOTIFICATION CARD */
        .feed-item {
            display: flex;
            align-items: center;
            justify-content: space-between;
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 12px 14px;
            margin-bottom: 10px;
            gap: 12px;
            transition: background 0.2s, border-color 0.2s;
            cursor: pointer;
        }
        .feed-item:hover {
            background: #1a1d26;
            border-color: rgba(0, 240, 255, 0.3);
        }

        .feed-left {
            display: flex;
            align-items: center;
            gap: 12px;
            flex: 1;
            min-width: 0;
        }

        /* Unread Dot */
        .status-dot {
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background: var(--neon-cyan);
            box-shadow: 0 0 8px var(--neon-cyan);
            flex-shrink: 0;
        }
        .status-dot.red { background: var(--neon-red); box-shadow: 0 0 8px var(--neon-red); }
        .status-dot.green { background: var(--neon-green); box-shadow: 0 0 8px var(--neon-green); }

        /* Avatar Icon */
        .avatar-box {
            width: 44px;
            height: 44px;
            border-radius: 50%;
            background: #202430;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.2rem;
            flex-shrink: 0;
            border: 1px solid var(--border-color);
        }

        .feed-info {
            display: flex;
            flex-direction: column;
            gap: 3px;
            overflow: hidden;
        }
        .feed-title {
            font-size: 0.92rem;
            font-weight: 600;
            color: #fff;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }
        .feed-sub {
            font-size: 0.8rem;
            color: var(--text-muted);
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }
        .feed-time {
            font-size: 0.75rem;
            color: #65697a;
            font-family: 'Share Tech Mono', monospace;
        }

        /* Right Side Media Thumbnail Preview */
        .feed-thumb {
            width: 88px;
            height: 52px;
            border-radius: 8px;
            background: #090a0d;
            border: 1px solid var(--border-color);
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
            position: relative;
            overflow: hidden;
        }
        .feed-thumb.cyber-bg {
            background: linear-gradient(135deg, rgba(255,42,42,0.2), rgba(0,240,255,0.2));
            border-color: rgba(0,240,255,0.4);
        }
        .feed-thumb .play-icon { font-size: 1.1rem; color: #fff; }
        .feed-thumb .badge-text { font-family: 'Share Tech Mono', monospace; font-size: 0.65rem; color: var(--neon-cyan); }
        .feed-thumb.green-thumb { background: rgba(57, 255, 20, 0.1); border-color: var(--neon-green); }
        .feed-thumb.green-thumb .badge-text { color: var(--neon-green); }

        /* Three Dots Menu */
        .menu-dots {
            color: var(--text-muted);
            font-size: 1.1rem;
            padding: 4px;
            cursor: pointer;
        }
        .menu-dots:hover { color: #fff; }

        /* General SaaS Tiers Portal Cards */
        .portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 14px; }
        .portal-card { background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 10px; padding: 16px; display: flex; flex-direction: column; justify-content: space-between; }
        .btn-action {
            background: var(--neon-red);
            color: #fff;
            border: none;
            padding: 10px 14px;
            border-radius: 6px;
            font-weight: 600;
            cursor: pointer;
            font-family: 'Share Tech Mono', monospace;
            font-size: 0.85rem;
        }
        .btn-cyan { background: var(--neon-cyan); color: #050505; }
        .form-group { margin-bottom: 12px; }
        .form-group label { display: block; font-family: 'Share Tech Mono', monospace; font-size: 0.75rem; color: var(--text-muted); margin-bottom: 4px; }
        .form-control { width: 100%; background: #000; border: 1px solid var(--border-color); padding: 10px; border-radius: 6px; color: #fff; font-size: 0.85rem; }
    </style>
</head>
<body>

    <div class="terminal-header">
        <div style="display: flex; align-items: center; gap: 8px;">
            <div class="terminal-dots"><span class="dot-red"></span><span class="dot-yellow"></span><span class="dot-green"></span></div>
            <span class="mono">root@nexal-intel:~/neural-grid$</span>
        </div>
        <span class="mono" style="color: var(--neon-cyan);">DIGITAL NEGRON WORLD // ECOSYSTEM FEED</span>
    </div>

    <nav>
        <div class="brand">NEXAL<span>.intel</span></div>
        <ul class="nav-links">
            <li><button onclick="switchTab('overview')" id="btn-overview" class="active">Overview</button></li>
            <li><button onclick="switchTab('retainers')" id="btn-retainers">SaaS Retainers</button></li>
            <li><button onclick="switchTab('aiplayground')" id="btn-aiplayground">Nexus Leo AI</button></li>
            <li><button onclick="switchTab('matchmeet')" id="btn-matchmeet">Match & Meet</button></li>
        </ul>
        <div class="coin-badge">💎 1,250 Orbs</div>
    </nav>

    <!-- 1. OVERVIEW: REPLICATED YOUTUBE-STYLE SAAS DROPS FEED -->
    <section id="overview" class="app-section active">
        
        <!-- Filter Chips Header -->
        <div class="feed-filter-bar">
            <button class="chip active" onclick="filterFeed('all', this)">All Feeds</button>
            <button class="chip" onclick="filterFeed('leo', this)">Nexus Leo AI</button>
            <button class="chip" onclick="filterFeed('stripe', this)">Stripe Retainers</button>
            <button class="chip" onclick="filterFeed('termux', this)">Termux Droplets</button>
            <button class="chip" onclick="filterFeed('match', this)">Match & Meet</button>
        </div>

        <!-- Group: Live Drops Today -->
        <div class="feed-group-title">Live System Drops // Today</div>

        <!-- ITEM 1: NEXUS LEO 3.1 -->
        <div class="feed-item" data-category="leo" onclick="switchTab('aiplayground')">
            <div class="feed-left">
                <div class="status-dot"></div>
                <div class="avatar-box">🎬</div>
                <div class="feed-info">
                    <div class="feed-title">Nexus Leo 3.1 Neural Matrix</div>
                    <div class="feed-sub">Uploaded: "Cyberpunk Tokyo 8K Drone Flythrough"</div>
                    <div class="feed-time">2 hours ago • Render Complete</div>
                </div>
            </div>
            <div class="feed-thumb cyber-bg">
                <span class="play-icon">▶</span>
                <span class="badge-text">4K • 8s</span>
            </div>
            <div class="menu-dots">⋮</div>
        </div>

        <!-- ITEM 2: PRO OPERATOR RETAINER -->
        <div class="feed-item" data-category="stripe" onclick="switchTab('retainers')">
            <div class="feed-left">
                <div class="status-dot green"></div>
                <div class="avatar-box">💳</div>
                <div class="feed-info">
                    <div class="feed-title">Pro Operator SaaS Retainer</div>
                    <div class="feed-sub">Active Subscription: $79/mo billed via Stripe</div>
                    <div class="feed-time">5 hours ago • Checkout Live</div>
                </div>
            </div>
            <div class="feed-thumb green-thumb">
                <span class="badge-text" style="font-size: 0.9rem; font-weight: bold;">$79/mo</span>
                <span class="badge-text">PRO TIER</span>
            </div>
            <div class="menu-dots">⋮</div>
        </div>

        <!-- ITEM 3: TERMUX CLOUD DROPLETS -->
        <div class="feed-item" data-category="termux">
            <div class="feed-left">
                <div class="status-dot green"></div>
                <div class="avatar-box">⚒️</div>
                <div class="feed-info">
                    <div class="feed-title">Termux Cloud Infrastructure</div>
                    <div class="feed-sub">Synced 3 Node Stack: [Autonomous, Gateway, Portal]</div>
                    <div class="feed-time">7 hours ago • NYC1 Droplet</div>
                </div>
            </div>
            <div class="feed-thumb" style="border-color: #333;">
                <span class="badge-text" style="color: var(--neon-green);">PM2: RUN</span>
                <span class="badge-text">PORT 8080</span>
            </div>
            <div class="menu-dots">⋮</div>
        </div>

        <!-- Group: Yesterday & Prior Drops -->
        <div class="feed-group-title">Prior Signals // Yesterday</div>

        <!-- ITEM 4: MATCH & MEET NETWORK -->
        <div class="feed-item" data-category="match" onclick="switchTab('matchmeet')">
            <div class="feed-left">
                <div class="status-dot"></div>
                <div class="avatar-box">🔥</div>
                <div class="feed-info">
                    <div class="feed-title">Match & Meet Social Matrix</div>
                    <div class="feed-sub">Broadcast: 12 new neural creator matches in ecosystem</div>
                    <div class="feed-time">1 day ago • NeGron Hub</div>
                </div>
            </div>
            <div class="feed-thumb cyber-bg">
                <span class="badge-text">12 MATCHES</span>
                <span class="badge-text">VOICE ON</span>
            </div>
            <div class="menu-dots">⋮</div>
        </div>

        <!-- ITEM 5: ENTERPRISE SYNDICATE -->
        <div class="feed-item" data-category="stripe" onclick="switchTab('retainers')">
            <div class="feed-left">
                <div class="status-dot red"></div>
                <div class="avatar-box">👑</div>
                <div class="feed-info">
                    <div class="feed-title">Enterprise Syndicate Tier</div>
                    <div class="feed-sub">Unlocked: Cloudflare Subdomain & White-Label Gate</div>
                    <div class="feed-time">1 day ago • $499 Tier</div>
                </div>
            </div>
            <div class="feed-thumb" style="border-color: var(--neon-gold);">
                <span class="badge-text" style="color: var(--neon-gold); font-size: 0.85rem; font-weight: bold;">$499</span>
                <span class="badge-text" style="color: var(--neon-gold);">VIP NODE</span>
            </div>
            <div class="menu-dots">⋮</div>
        </div>

    </section>

    <!-- 2. SAAS RETAINERS -->
    <section id="retainers" class="app-section">
        <div class="feed-group-title">SaaS Retainer Subscriptions</div>
        <div class="portal-grid">
            <div class="portal-card">
                <div>
                    <h4 style="color:#fff;">Shard Basic</h4>
                    <div style="font-size:1.5rem; font-weight:bold; color:var(--neon-cyan); margin:6px 0;">$29/mo</div>
                    <p style="font-size:0.8rem; color:var(--text-muted); margin-bottom:12px;">5 Nexus Leo renders + 100 Orbs</p>
                </div>
                <button class="btn-action btn-cyan" onclick="triggerStripeCheckout('Shard Basic', 29)">Select $29</button>
            </div>
            <div class="portal-card" style="border-color: var(--neon-green);">
                <div>
                    <h4 style="color:var(--neon-green);">Pro Operator 🔥</h4>
                    <div style="font-size:1.5rem; font-weight:bold; color:var(--neon-green); margin:6px 0;">$79/mo</div>
                    <p style="font-size:0.8rem; color:var(--text-muted); margin-bottom:12px;">25 Nexus Leo 1080p renders + 350 Orbs</p>
                </div>
                <button class="btn-action" style="background:var(--neon-green); color:#000;" onclick="triggerStripeCheckout('Pro Operator', 79)">Select $79</button>
            </div>
            <div class="portal-card" style="border-color: var(--neon-red);">
                <div>
                    <h4 style="color:var(--neon-red);">Autonomous Elite</h4>
                    <div style="font-size:1.5rem; font-weight:bold; color:var(--neon-red); margin:6px 0;">$199/mo</div>
                    <p style="font-size:0.8rem; color:var(--text-muted); margin-bottom:12px;">100 Nexus Leo 4K renders + 1,000 Orbs</p>
                </div>
                <button class="btn-action" onclick="triggerStripeCheckout('Autonomous Elite', 199)">Select $199</button>
            </div>
        </div>
    </section>

    <!-- 3. AI PLAYGROUND -->
    <section id="aiplayground" class="app-section">
        <div class="feed-group-title">Nexus Leo Video Synthesis</div>
        <div class="form-group">
            <label>SCENE PROMPT</label>
            <textarea id="leo-prompt" class="form-control" rows="3" placeholder="Cyberpunk neon drone shot..."></textarea>
        </div>
        <button class="btn-action btn-cyan" style="width:100%;" onclick="generateLeoVideo()">⚡ Synthesize Video</button>
        <div id="leo-output" style="margin-top:12px; font-size:0.8rem; color:var(--neon-green); font-family:'Share Tech Mono'; display:none;"></div>
    </section>

    <!-- 4. MATCH & MEET -->
    <section id="matchmeet" class="app-section">
        <div class="feed-group-title">Match & Meet Social Hub</div>
        <p style="color:var(--text-muted); font-size:0.9rem;">Connecting creators across the Digital NeGron World metaverse.</p>
    </section>

    <script>
        function switchTab(tabId) {
            document.querySelectorAll('.app-section').forEach(s => s.classList.remove('active'));
            document.querySelectorAll('.nav-links button').forEach(b => b.classList.remove('active'));
            document.getElementById(tabId).classList.add('active');
            let btn = document.getElementById('btn-' + tabId);
            if(btn) btn.classList.add('active');
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }

        function filterFeed(category, btnElement) {
            document.querySelectorAll('.feed-filter-bar .chip').forEach(c => c.classList.remove('active'));
            btnElement.classList.add('active');

            let items = document.querySelectorAll('.feed-item');
            items.forEach(item => {
                if(category === 'all' || item.getAttribute('data-category') === category) {
                    item.style.display = 'flex';
                } else {
                    item.style.display = 'none';
                }
            });
        }

        async function triggerStripeCheckout(planName, priceAmount) {
            try {
                const response = await fetch('/api/create-checkout-session', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ planName, priceAmount })
                });
                const data = await response.json();
                if (data.url) window.location.href = data.url;
                else alert(data.message || 'Stripe Session Ready');
            } catch (err) { alert('Error: ' + err.message); }
        }

        async function generateLeoVideo() {
            let prompt = document.getElementById('leo-prompt').value;
            if(!prompt) return alert('Enter prompt');
            let out = document.getElementById('leo-output');
            out.style.display = 'block';
            out.innerHTML = '[MATRIX] Synthesizing video sequence...';
            setTimeout(() => {
                out.innerHTML = '[SUCCESS] Video render added to feed cloud vault!';
            }, 1200);
        }
    </script>
</body>
</html>
HTML

pm2 restart 3 || pm2 restart "nexal portal"
pm2 save
echo "✅ [NEXAL INTEL] Replicated YouTube-Style SaaS Overview Feed Live!"
