import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 7. Subtle background texture
html = html.replace('transition: background-color 0.3s, color 0.3s;', "transition: background-color 0.3s, color 0.3s;\n            background-image: radial-gradient(circle, var(--text-muted) 1px, transparent 1px);\n            background-size: 20px 20px;\n            background-position: 0 0;\n")

# 1. Nav border top
html = html.replace('.nav-btn.active {\n            background: rgba(74, 222, 128, 0.1);\n            color: var(--accent);\n            border: 1px solid var(--accent);\n        }', 
'''.nav-btn.active {
            background: rgba(74, 222, 128, 0.1);
            color: var(--accent);
            border: 1px solid var(--accent);
            border-left: 4px solid var(--accent);
        }''')

# 1. Sidebar Brand & Illustration
sidebar_brand = '''<div class="brand">
                Gig<span>Profit</span>
                <div style="font-size:0.75rem; color:var(--text-muted); font-weight:600; margin-top:4px;">Your earnings. Decoded.</div>
            </div>
            
            <div style="text-align:center; margin-bottom:1rem;">
                <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="var(--accent)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                    <circle cx="7" cy="17" r="3"></circle>
                    <circle cx="17" cy="17" r="3"></circle>
                    <path d="M14 17h-4"></path>
                    <path d="M14 14v3"></path>
                    <path d="M14 14l3-6"></path>
                    <path d="M17 8h3"></path>
                    <path d="M14 14l-4-4-2 2-2-1"></path>
                </svg>
            </div>'''
html = html.replace('<div class="brand">Gig<span>Profit</span></div>', sidebar_brand)

# 1. Sidebar Platform logos
platform_pills = '''
            <div style="margin-top:auto; display:flex; justify-content:center; gap:0.5rem; margin-bottom:1rem;">
                <div style="width:24px;height:24px;border-radius:50%;background:#e23744;color:#FFF;display:flex;align-items:center;justify-content:center;font-size:0.75rem;font-weight:bold;font-family:sans-serif;">Z</div>
                <div style="width:24px;height:24px;border-radius:50%;background:#fc8019;color:#FFF;display:flex;align-items:center;justify-content:center;font-size:0.75rem;font-weight:bold;font-family:sans-serif;">S</div>
                <div style="width:24px;height:24px;border-radius:50%;background:#0f4c81;color:#FFF;display:flex;align-items:center;justify-content:center;font-size:0.75rem;font-weight:bold;font-family:sans-serif;">R</div>
            </div>
            <button id="themeToggleBtn"'''
html = html.replace('<button id="themeToggleBtn"', platform_pills)
html = html.replace('margin-top: auto;\n            background: var(--bg-base);', 'background: var(--bg-base);')

# 6. Page Titles & 2. Hero Banner
calc_hero = '''<h2 class="section-title">Record Today's Earnings</h2>
                    <p style="color:var(--text-muted); font-size:0.9rem; margin-bottom:1.5rem; margin-top:-0.5rem;">Log your ride data and see where your money really goes</p>
                    
                    <div class="card" style="display:flex; justify-content:space-between; align-items:center; background: linear-gradient(90deg, var(--bg-card) 60%, rgba(74, 222, 128, 0.05) 100%); padding: 1.5rem;">
                        <div>
                            <h2 style="font-size:1.8rem; font-weight:800; margin-bottom:0.3rem;">Know your real ₹</h2>
                            <p style="color:var(--text-muted); font-size:0.85rem; margin-bottom:0.8rem; max-width:85%; line-height:1.4;">Most delivery workers lose 20–35% of earnings to fuel without realizing it.</p>
                            <div style="font-family:'JetBrains Mono', monospace; font-size:0.75rem; color:var(--accent); background:rgba(74, 222, 128, 0.1); padding:0.4rem 0.8rem; border-radius:6px; display:inline-block;">Avg fuel loss: ₹180/day | Monthly: ₹5,400</div>
                        </div>
                        <div style="flex-shrink:0;">
                            <svg width="60" height="60" viewBox="0 0 24 24" fill="none" stroke="var(--accent)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                                <circle cx="7" cy="17" r="3"></circle>
                                <circle cx="17" cy="17" r="3"></circle>
                                <path d="M14 17h-4"></path>
                                <path d="M14 14v3"></path>
                                <path d="M14 14l3-6"></path>
                                <path d="M17 8h3"></path>
                                <path d="M14 14l-4-4-2 2-2-1"></path>
                                <circle cx="11" cy="7" r="4"></circle>
                                <text x="9" y="9" fill="var(--accent)" stroke="none" font-size="7" font-weight="bold" font-family="sans-serif">₹</text>
                            </svg>
                        </div>
                    </div>'''
html = html.replace('<h2 class="section-title">Record Today\'s Earnings</h2>', calc_hero)
html = html.replace('<h2 class="section-title">7-Day Weekly Tracker</h2>', '<h2 class="section-title">7-Day Weekly Tracker</h2>\n                    <p style="color:var(--text-muted); font-size:0.9rem; margin-bottom:1.5rem; margin-top:-0.5rem;">Your last 7 days at a glance</p>')
html = html.replace('<h2 class="section-title">Goal Planner</h2>', '<h2 class="section-title">Goal Planner</h2>\n                    <p style="color:var(--text-muted); font-size:0.9rem; margin-bottom:1.5rem; margin-top:-0.5rem;">Set a target. Build a plan.</p>')
html = html.replace('<h2 class="section-title">Dashboard & Settings</h2>', '<h2 class="section-title">Dashboard & Settings</h2>\n                    <p style="color:var(--text-muted); font-size:0.9rem; margin-bottom:1.5rem; margin-top:-0.5rem;">Your full earnings picture</p>')

# 4. Input Icons & 7. calculate button
calc_inputs_html = '''
                            <div class="form-full">
                                <label>⚙️ Select Vehicle</label>
                                <select id="calcVehicle" onchange="updateCalcMileage()"></select>
                            </div>
                            <div>
                                <label><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="var(--accent)" stroke-width="2" style="display:inline;vertical-align:middle"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path></svg> Daily Earnings (₹)</label>
                                <input type="number" id="calcEarnings" placeholder="1500" required>
                            </div>
                            <div>
                                <label><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="var(--accent)" stroke-width="2" style="display:inline;vertical-align:middle"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg> Working Hours</label>
                                <input type="number" id="calcHours" placeholder="10" required>
                            </div>
                            <div>
                                <label><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="var(--accent)" stroke-width="2" style="display:inline;vertical-align:middle"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg> Distance Traveled (km)</label>
                                <input type="number" id="calcDistance" placeholder="120" required>
                            </div>
                            <div>
                                <label><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="var(--accent)" stroke-width="2" style="display:inline;vertical-align:middle"><path d="M12 22a7 7 0 0 0 7-7c0-2-1-3.9-3-5.5s-3.5-4-4-6.5c-.5 2.5-2 4.9-4 6.5C6 11.1 5 13 5 15a7 7 0 0 0 7 7z"></path></svg> Fuel Price (₹/L)</label>
                                <input type="number" id="calcFuelPrice" value="106" required>
                            </div>
                            <div class="form-full">
                                <label><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="var(--accent)" stroke-width="2" style="display:inline;vertical-align:middle"><circle cx="12" cy="12" r="3"></circle><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"></path></svg> Mileage (km/L)</label>
                                <input type="number" id="calcMileage" value="45" required>
                            </div>'''
html = re.sub(r'<div class="form-full">\s*<label>Select Vehicle.*?</label>\s*<input type="number" id="calcMileage" value="45" required>\s*</div>', calc_inputs_html, html, flags=re.DOTALL)

html = html.replace('<button class="btn-primary" style="margin-top: 1rem;" onclick="runCalculator()">Calculate & Log</button>',
  '<button class="btn-primary" style="margin-top: 1rem;" onclick="runCalculator()"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="var(--bg-base)" stroke-width="2" style="display:inline;vertical-align:middle;margin-right:8px"><circle cx="7" cy="17" r="3"></circle><circle cx="17" cy="17" r="3"></circle><path d="M14 17h-4"></path><path d="M14 14v3"></path><path d="M14 14l3-6"></path><path d="M17 8h3"></path><path d="M14 14l-4-4-2 2-2-1"></path></svg>Calculate & Log</button>')

# 5. Results card contextual gauge
res_html = '''<div id="fuelBurnMeter" style="margin-top:1rem; padding:1rem; background:var(--bg-base); border:1px solid var(--border); border-radius:8px;">
                            <div style="display:flex;justify-content:space-between;font-size:0.8rem;margin-bottom:0.5rem;color:var(--text-muted);"><span style="font-family:'JetBrains Mono'">Fuel Burn</span><span id="fuelBurnPct" style="font-family:'JetBrains Mono'">0%</span></div>
                            <div style="width:100%; height:8px; background:var(--bg-card); border-radius:4px; overflow:hidden;"><div id="fuelBurnBar" style="width:0%; height:100%; background:var(--danger); transition:width 0.5s;"></div></div>
                            <p id="fuelBurnMsg" style="margin-top:0.8rem; font-size:0.85rem; font-weight:600; text-align:center;"></p>
                        </div>'''
html = html.replace('</div>\n\n                        <button class="btn-secondary" style="width: 100%; margin-bottom: 1.5rem;" onclick="saveCalculatedData()">', 
f'</div>{res_html}\n\n                        <button class="btn-secondary" style="width: 100%; margin-bottom: 1.5rem; margin-top: 1.5rem;" onclick="saveCalculatedData()">')

# Empty States Additions
empty_wk = '''<div id="emptyWeek" style="display:none; text-align:center; padding:3rem 1rem;">
                        <svg width="80" height="80" viewBox="0 0 24 24" fill="none" stroke="var(--accent)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" style="opacity:0.3; margin-bottom:1rem;">
                            <circle cx="7" cy="17" r="3"></circle>
                            <circle cx="17" cy="17" r="3"></circle>
                            <path d="M14 17h-4"></path>
                            <path d="M14 14v3"></path>
                            <path d="M14 14l3-6"></path>
                            <path d="M17 8h3"></path>
                            <path d="M14 14l-4-4-2 2-2-1"></path>
                            <path d="M2 20h20"></path><path d="M5 20h2M10 20h2M15 20h2M20 20h2" stroke-dasharray="2 2" stroke="var(--bg-base)"></path>
                        </svg>
                        <p style="color:var(--text-muted); font-size:0.9rem;">No rides logged yet. Start by calculating today's earnings.</p>
                    </div>'''
html = html.replace('<div class="metrics-grid" id="weekMetrics">', f'{empty_wk}\n                    <div id="weekContent">\n                    <div class="metrics-grid" id="weekMetrics">')
html = html.replace('</div>\n                </div>\n\n                <!-- TAB 3: GOAL PLANNER -->', '</div>\n                </div></div>\n\n                <!-- TAB 3: GOAL PLANNER -->')

empty_gl = '''<div id="emptyGoal" style="display:none; text-align:center; padding:3rem 1rem; background:var(--bg-card); border-radius:12px; border:1px solid var(--border); margin-bottom: 1.5rem;">
                        <svg width="80" height="80" viewBox="0 0 24 24" fill="none" stroke="var(--accent)" stroke-width="1.5" style="opacity:0.3; margin-bottom:1rem;">
                            <circle cx="12" cy="12" r="10"></circle><circle cx="12" cy="12" r="6"></circle><circle cx="12" cy="12" r="2"></circle>
                        </svg>
                        <p style="color:var(--text-muted); font-size:0.9rem;">Set your monthly goal above and we'll map your path.</p>
                    </div>'''
html = html.replace('<div id="goalBreakdown" style="display: none;">', f'{empty_gl}\n                    <div id="goalBreakdown" style="display: none;">')

empty_dh = '''<div id="emptyDash" style="display:none; text-align:center; padding:3rem 1rem; background:var(--bg-card); border-radius:12px; border:1px solid var(--border); margin-bottom: 1.5rem;">
                        <svg width="80" height="80" viewBox="0 0 24 24" fill="none" stroke="var(--accent)" stroke-width="1.5" style="opacity:0.3; margin-bottom:1rem;">
                            <path d="M18 20V10M12 20V4M6 20v-6"></path>
                            <rect x="16" y="10" width="4" height="10"></rect>
                            <rect x="10" y="4" width="4" height="16"></rect>
                            <rect x="4" y="14" width="4" height="6"></rect>
                        </svg>
                        <p style="color:var(--text-muted); font-size:0.9rem;">Your dashboard fills up as you log rides.</p>
                    </div>'''
html = html.replace('<div class="card ai-card">', f'{empty_dh}\n                    <div class="card ai-card" id="dashAiWrapper">')


# JS Additions for results
js_res = '''
    const fuelPctVal = ((fuelCost / earnings) * 100);
    document.getElementById('fuelBurnPct').textContent = fuelPct.toFixed(1) + '%';
    document.getElementById('fuelBurnBar').style.width = Math.min(100, fuelPctVal) + '%';
    
    let fm = document.getElementById('fuelBurnMsg');
    if(fuelPctVal < 20) { fm.textContent = "Great efficiency! You're keeping fuel costs low."; fm.className = "text-green"; document.getElementById('fuelBurnBar').style.background = "var(--accent)"; }
    else if(fuelPctVal <= 35) { fm.textContent = "Average efficiency. Small optimizations can help."; fm.className = "text-amber"; document.getElementById('fuelBurnBar').style.background = "var(--warning)"; }
    else { fm.textContent = "High fuel spend. Check route and vehicle tips below."; fm.className = "text-red"; document.getElementById('fuelBurnBar').style.background = "var(--danger)"; }
'''
html = html.replace('const fuelPct = ((fuelCost/earnings)*100).toFixed(1);', 'const fuelPct = ((fuelCost/earnings)*100).toFixed(1);')
html = html.replace('document.getElementById(\'calcResultsSection\').style.display = \'block\';', 'document.getElementById(\'calcResultsSection\').style.display = \'block\';\n'+js_res)

js_wk = '''
    if(logs.length === 0) {
        document.getElementById('emptyWeek').style.display = 'block';
        if(document.getElementById('weekContent')) document.getElementById('weekContent').style.display = 'none';
        return;
    } else {
        document.getElementById('emptyWeek').style.display = 'none';
        if(document.getElementById('weekContent')) document.getElementById('weekContent').style.display = 'block';
    }
'''
html = html.replace('if(logs.length === 0) return;', js_wk)

js_gl = '''
    if(!target || !days) {
        document.getElementById('emptyGoal').style.display = 'block';
        return; 
    } else { document.getElementById('emptyGoal').style.display = 'none'; }
'''
html = html.replace('saveState(\'gp_goal\', state.goal);', 'saveState(\'gp_goal\', state.goal);\n'+js_gl)

js_dh = '''
    if(state.logs.length < 3) {
        document.getElementById('emptyDash').style.display = 'block';
        document.getElementById('dashAiWrapper').style.display = 'none';
    } else {
        document.getElementById('emptyDash').style.display = 'none';
        document.getElementById('dashAiWrapper').style.display = 'block';
    }
'''
html = html.replace('function refreshDashboard() {\n    renderVehicles();', 'function refreshDashboard() {\n    renderVehicles();\n    '+js_dh)


with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
