#!/usr/bin/env python3

from flask import Flask, request
from duffel_api import Duffel
from FlightData.FlightDataTracker import FlightDataTracker
from FlightData.FlightDataLogger import FlightDataLogger
from FlightData.FlightDataLimit import FlightDataLimit
from FlightData.FlightDataPmt import FlightDataPmt

access_token = "duffel_test_83IaIdX58kDt2kWhvu3mMQZkbZB2mfsfPE5sO-KHld-"
duffel = Duffel(access_token=access_token)

app = Flask(__name__)

@app.route("/")
def index():
    return {}

@app.route("/api/run")
def main():
    tracker = FlightDataTracker()
    tracker.set_slices(origin="CLT", destination="SAN", depart_date="2024-01-01", return_date="2024-01-30")
    tracker.set_passengers(passengers=[{"age" : 23}])
    tracker.set_cabin_class(cabin_class="economy")
    all_offers = tracker.get_all_offers()
    tracker.set_selected_flight(selected_flight=all_offers[0])

    # logger = FlightDataLogger(Tracker=tracker, log_dir="logs/")
    # logger.get_all_offers(num_iterations=25, time_interval=0)
    # logger.create_log(print_all_offers=True)
    # logger.create_plot(limit_value=450)

    limit = FlightDataLimit(Tracker=tracker, limit_val=450)
    flight = limit.get_flight_at_limit(max_iterations=25, time_interval=0)
    flight.passengers[0].set_age(23)
    flight.passengers[0].set_family_name("TEST")
    flight.passengers[0].set_given_name("Stephen")
    flight.passengers[0].set_title("Mr")
    flight.passengers[0].set_dob("2000-03-02")
    flight.passengers[0].set_gender("M")
    flight.passengers[0].set_phone_number("+18582165827")
    flight.passengers[0].set_email("StephenG753@Gmail.com")

    pmt = FlightDataPmt(flight=flight)
    pmt.create_payment_intent()
    return {"client_token" : pmt.pmt_intent.client_token}

@app.route("/api/post_test", methods=["POST"])
def post_test():
    print("======================================")
    print(request.get_json())
    print("======================================")
    return "SUCCESS"

if __name__ == "__main__":
    app.run(debug=True)