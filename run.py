import os

from server import server

server.launch(port=int(os.environ.get("PORT", None)))
