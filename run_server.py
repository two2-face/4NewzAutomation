# run_server.py

from flask import Flask, request
from main import main

app = Flask(__name__)

# Geheimer Schlüssel zum Schutz vor fremdem Zugriff
API_KEY = "mein-sicherer-schlüssel123"

@app.route("/run", methods=["GET"])
def run_bot():
    key = request.args.get("key")
    if key != API_KEY:
        return "⛔️ Nicht autorisiert", 401
    try:
        main()
        return "✅ Bot erfolgreich ausgeführt", 200
    except Exception as e:
        return f"❌ Fehler: {e}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
