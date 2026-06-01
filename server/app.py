"""Optional: run StackTrim on Railway/Render (not used by Vercel)."""
import os

from flask import Flask, send_from_directory

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app = Flask(__name__)


@app.route("/")
def index():
    return send_from_directory(HERE, "index.html")


@app.route("/<path:filename>")
def static_files(filename):
    path = os.path.join(HERE, filename)
    if os.path.isfile(path):
        return send_from_directory(HERE, filename)
    return send_from_directory(HERE, "index.html")
