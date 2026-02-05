from flask import Flask, request, jsonify
import httpx

app = Flask(__name__)

@app.route('/fetch')
async def fetch_player():
    uid = request.args.get('uid')
    if not uid:
        return jsonify({"error": "No UID provided"}), 400

    # Using the direct 2026 Garena IND endpoint
    url = "https://client.ind.freefiremobile.com/GetPlayerPersonalShow"
    payload = f"region=IND&uid={uid}"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    async with httpx.AsyncClient(verify=False) as client:
        try:
            r = await client.post(url, data=payload, headers=headers, timeout=10)
            return jsonify(r.json())
        except Exception as e:
            return jsonify({"error": "Garena Server Busy"}), 503

if __name__ == "__main__":
    app.run()
