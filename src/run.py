#!/usr/bin/env python3

from FlightData.TrackFlightData import TrackFlightData

if __name__ == "__main__":
    tracker = TrackFlightData()
    tracker.set_slices("SAN", "ANC", "2023-12-20", "2023-12-30")
    tracker.set_passengers([{"type" : "adult"}])
    tracker.set_cabin_class("economy")
    tracker.set_all_offers()
    tracker.set_selected_flight_choice_idx(0)
    tracker.set_limit_value(375)
    log_file = tracker.log_flight_prices("logs/", 5)
    tracker.plot_flight_prices(log_file)