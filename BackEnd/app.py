#!/usr/bin/env python3

from flask import Flask
from main import *

app = Flask(__name__)

app.add_url_rule("/", "index", index)
app.add_url_rule("/api/run_preset_params", "run_preset_params", run_preset_params, methods=["GET"])
app.add_url_rule("/api/get_all_offers", "get_all_offers", get_all_offers, methods=["POST"])
app.add_url_rule("/api/get_offer_below_limit", "get_offer_below_limit", get_offer_below_limit, methods=["POST"])
app.add_url_rule("/api/order_flight", "order_flight", order_flight, methods=["POST"])


if __name__ == "__main__":
    app.run(debug=True)