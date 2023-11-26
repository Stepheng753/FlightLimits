#!/usr/bin/env python3
from FlightData.FlightDataTracker import FlightDataTracker
from FlightData.FlightDataLogger import FlightDataLogger
from FlightData.FlightDataLimit import FlightDataLimit
from FlightData.FlightDataPmt import FlightDataPmt

if __name__ == "__main__":
    tracker = FlightDataTracker()
    tracker.set_slices("SAN", "NRT", "2024-03-01", "2024-03-30")
    tracker.set_passengers([{"age" : 18}])
    tracker.set_cabin_class("economy")
    all_offers = tracker.get_all_offers()
    tracker.set_selected_flight(all_offers[0])

    logger = FlightDataLogger(tracker ,"logs/")
    logger.set_times_prices(25, 0)
    logger.create_log()
    logger.create_plot(375)

    # limit = FlightDataLimit(tracker, 375)
    # flight = limit.get_flight_at_limit(25, 0)
    # flight.passengers[0].set_age(23)
    # flight.passengers[0].set_family_name("TEST")
    # flight.passengers[0].set_given_name("Stephen")
    # flight.passengers[0].set_title("Mr")
    # flight.passengers[0].set_dob("2000-03-02")
    # flight.passengers[0].set_gender("M")
    # flight.passengers[0].set_phone_number("+18582165827")
    # flight.passengers[0].set_email("StephenG753@Gmail.com")

    # pmt = FlightDataPmt(flight)
    # pmt.create_order()