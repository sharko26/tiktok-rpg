from flask import Flask, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return "Serveur TikTok RPG en ligne !"

# Route pour l'interface live (frontend)
@app.route("/frontend/<path:filename>")
def overlay(filename):
    return send_from_directory("frontend", filename)

# Route pour le panneau admin
@app.route("/admin_panel/<path:filename>")
def admin_panel(filename):
    return send_from_directory("admin_panel", filename)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
