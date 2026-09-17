#!/usr/bin/env python3
"""Local static server that maps /milford to milford.html, matching CloudFront."""

from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlparse
import os

ROOT = Path(__file__).resolve().parent


class Handler(SimpleHTTPRequestHandler):
    def translate_path(self, path):
        parsed = urlparse(path)
        path_only = unquote(parsed.path)
        if path_only != "/" and not Path(path_only.lstrip("/")).suffix:
            html_file = ROOT / f"{path_only.lstrip('/')}.html"
            if html_file.is_file():
                path = f"/{html_file.relative_to(ROOT).as_posix()}"
        return super().translate_path(path)


if __name__ == "__main__":
    os.chdir(ROOT)
    port = int(os.environ.get("PORT", "8000"))
    print(f"Serving at http://127.0.0.1:{port}/", flush=True)
    ThreadingHTTPServer(("127.0.0.1", port), Handler).serve_forever()
