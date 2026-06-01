"""StackTrim static site — stdlib WSGI (no Flask required at import time)."""
import mimetypes
import os

ROOT = os.path.dirname(os.path.abspath(__file__))


def _file_response(path_info: str):
    rel = (path_info or "/").lstrip("/") or "index.html"
    safe = os.path.normpath(os.path.join(ROOT, rel))
    if not safe.startswith(ROOT):
        safe = os.path.join(ROOT, "index.html")
    if not os.path.isfile(safe):
        safe = os.path.join(ROOT, "index.html")
    with open(safe, "rb") as f:
        body = f.read()
    mime, _ = mimetypes.guess_type(safe)
    return body, mime or "text/html; charset=utf-8"


def app(environ, start_response):
    body, content_type = _file_response(environ.get("PATH_INFO", "/"))
    start_response(
        "200 OK",
        [("Content-Type", content_type), ("Content-Length", str(len(body)))],
    )
    return [body]


# Hosts look for any of these names at module level
application = app
handler = app
