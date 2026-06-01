"""Serves StackTrim (static index.html) for Python hosts (Railway, Render, etc.)."""
import os

from flask import Flask, send_from_directory

app = Flask(__name__)
ROOT = os.path.dirname(os.path.abspath(__file__))


@app.route("/")
def index():
    return send_from_directory(ROOT, "index.html")


@app.route("/<path:filename>")
def static_file(filename):
    path = os.path.join(ROOT, filename)
    if os.path.isfile(path):
        return send_from_directory(ROOT, filename)
    return send_from_directory(ROOT, "index.html")
