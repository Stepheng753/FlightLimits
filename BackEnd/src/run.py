#!/usr/bin/env python3
import json
from duffel_api import Duffel
from FlightData.FlightDataTracker import FlightDataTracker
from FlightData.FlightDataLogger import FlightDataLogger
from FlightData.FlightDataLimit import FlightDataLimit
from FlightData.FlightDataPmt import FlightDataPmt

access_token = "duffel_test_83IaIdX58kDt2kWhvu3mMQZkbZB2mfsfPE5sO-KHld-"
duffel = Duffel(access_token=access_token)

def main():
    confirm = "y"

    if "y" not in confirm:
        tracker = FlightDataTracker()
        tracker.set_slices(origin="CLT", destination="SAN", depart_date="2024-01-01", arrive_date="2024-01-30")
        tracker.set_passengers(passengers=[{"age" : 23}])
        tracker.set_cabin_class(cabin_class="economy")
        all_offers = tracker.get_all_offers()
        tracker.set_selected_flight(selected_flight=all_offers[0])

        logger = FlightDataLogger(Tracker=tracker, log_dir="logs/")
        logger.get_all_offers(num_iterations=25, time_interval=0)
        logger.create_log(print_all_offers=True)
        logger.create_plot(limit_value=450)

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
        pmt.write_payment_intent_info(dir="../../.payment_intent/")
    else:
        data = json.load(open("../../.payment_intent/pmt_intent.json"))
        id = data["id"]
        try:
            print(duffel.payment_intents.confirm(id))
            pmt.create_order()
        except:
            print("Payment Intent hasn't succeeded")
            return

if __name__ == "__main__":
    main()