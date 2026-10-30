from flask import Flask, render_template_string
import requests

app = Flask(__name__)

# Hut 8 clone HTML inside Python
HTML = """
<!DOCTYPE html>
<html><head><meta name="viewport" content="width=device-width, initial-scale=1">
<title>HUT 8 Python Clone</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:system-ui;background:#fff;color:#111}
.nav{border-bottom:1px solid #e5e7eb;padding:14px 20px;display:flex;justify-content:space-between;max-width:1280px;margin:auto}
.logo{font-weight:900;font-size:22px}
.hero{max-width:1280px;margin:auto;padding:60px 20px;display:grid;grid-template-columns:1.2fr .8fr;gap:20px}
h1{font-size:50px;line-height:.9;letter-spacing:-2px}
.stat-bar{display:grid;grid-template-columns:repeat(3,1fr);gap:1px;background:#e5e7eb;border:1px solid #e5e7eb;margin-top:20px}
.stat{background:#fff;padding:20px}
.stat b{font-size:32px;display:block}
.btn{background:#111;color:#fff;padding:12px 20px;border-radius:999px;text-decoration:none;font-weight:700;font-size:12px;display:inline-block;margin-top:12px}
.card{border:1px solid #e5e7eb;padding:20px;border-radius:12px;margin-top:12px}
</style></head>
<body>
<div class="nav"><div class="logo">HUT 8 / PYTHON</div><div>Power | Infra | Compute</div></div>
<div class="hero">
<div>
<div style="font-size:11px;letter-spacing:2px;color:#888">● LIVE PYTHON VERSION - BTC: {{btc_price}}</div>
<h1>Energy infrastructure platform integrating <span style="color:#666">power, digital infrastructure, and compute.</span></h1>
<p style="margin:16px 0;color:#555">Built with Python Flask — like real Hut 8 (hut8.com). Python powers the backend for live stats.</p>
<div class="stat-bar">
<div class="stat"><b>1,020 MW</b><small>Energy Under Management</small></div>
<div class="stat"><b>{{btc_price}}</b><small>Live BTC from Python</small></div>
<div class="stat"><b>{{hashrate}} EH/s</b><small>Hashrate Calculated by Python</small></div>
</div>
<a class="btn" href="/api">View Python API (like Hut 8 investors)</a>
</div>
<div>
<div class="card"><h3>⛏️ Python Mining Calculator</h3><p style="font-size:12px;color:#666;margin:8px 0">Enter your power in Kampala:</p>
<form><input name="mw" placeholder="e.g. 0.5 MW" style="padding:8px;width:100%"><button class="btn" type="submit">Calculate Profit</button></form>
{% if profit %}<p style="margin-top:10px"><b>Est Profit: ${{profit}}/day</b> (Python calculated)</p>{% endif %}
</div>
<div class="card"><h3>How Hut 8 Was Made</h3><p style="font-size:13px;color:#555;line-height:1.6">2017 Python script? No, $100M power deal.<br>2018 TSX listing.<br>2023 Merger USBTC.<br>2026 Python API for investors.</p></div>
</div>
</div>
</body></html>
"""

@app.route('/')
def home():
    # Live BTC price from Python — real Hut 8 does this
    try:
        btc = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd", timeout=5).json()['bitcoin']['usd']
        btc_price = f"${btc:,}"
    except:
        btc_price = "$67,432"
    
    from flask import request
    mw = request.args.get('mw')
    profit = None
    hashrate = 5.2
    if mw:
        try:
            mw_val = float(mw)
            # Simple calc: 1 MW = ~$150/day at current diff (demo)
            profit = round(mw_val * 150, 2)
            hashrate = round(mw_val * 0.8, 2)
        except:
            pass
    return render_template_string(HTML, btc_price=btc_price, profit=profit, hashrate=hashrate)

@app.route('/api')
def api():
    return {"company": "Hut 8 Clone Python", "energy_mw": 1020, "sites": 15, "inspired_by": "hut8.com", "built_with": "Flask"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

