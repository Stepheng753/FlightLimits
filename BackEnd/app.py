#!/usr/bin/env python3

from flask import Flask
from main import *

app = Flask(__name__)

app.add_url_rule("/", "index", index)
app.add_url_rule("/api/run", "run_preset_params", run_preset_params)
app.add_url_rule("/api/post_test", "get_all_offers", get_all_offers, methods=["POST"])


if __name__ == "__main__":
    app.run(debug=True)