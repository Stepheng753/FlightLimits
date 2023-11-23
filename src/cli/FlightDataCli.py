#!/usr/bin/env python3

import sys
sys.path.append('../')

from FlightData.TrackFlightData import TrackFlightData

class FlightDataCli:

    def __init__(self) -> None:
        self.TrackFlightData = TrackFlightData()
        self.input_format = lambda x: (x).ljust(45) + ": "

    def input_offer_request_parameters(self) -> None:
        origin = input(self.input_format("Enter in the IATA Origin Airport Code"))
        destination = input(self.input_format("Enter in the IATA Destination Airport Code"))

        print("One Way or Round Trip")
        print("\t1) One Way")
        print("\t2) Round Trip")
        one_round_way = input(self.input_format("Enter One Way or Round Trip"))
        depart_date = input(self.input_format("Enter in Departure Date (YYYY-MM-DD)"))
        arrive_date = None
        if ("2" in one_round_way.lower()) or ("round" in one_round_way.lower()):
            arrive_date = input(self.input_format("Enter in Arrival Date (YYYY-MM-DD)"))

        num_adult_passengers = int(input(self.input_format("Enter in the Number of Adult Passengers")))
        num_child_passengers = int(input(self.input_format("Enter in the Number of Child Passengers")))
        passengers = []
        for _ in range(0, num_adult_passengers):
            passengers.append({"type" : "adult"})
        for child_idx in range(1, num_child_passengers + 1):
            age = int(input((self.input_format("Enter in Age of Child #" + str(child_idx) ))))
            passengers.append({"age" : age})

        cabin_classes = ["first", "business", "premium_economy", "economy"]
        print("All Types of Cabin Classes")
        for cabin_idx in range(0, len(cabin_classes)):
            print("\t" + str(cabin_idx + 1) + ") " + cabin_classes[cabin_idx].capitalize())
        cabin_class_idx = int(input(self.input_format("Enter in the Cabin Class")))

        self.TrackFlightData.set_slices(origin, destination, depart_date, arrive_date)
        self.TrackFlightData.set_passengers(passengers)
        self.TrackFlightData.set_cabin_class(cabin_classes[cabin_class_idx - 1])

        print("\n")

    def display_offers(self) -> None:
        for offer_idx in range(0, len(self.TrackFlightData.all_offers)):
            print("-----------------------------------------------------------------")
            print("Choice: " + str(offer_idx + 1) + "\n" + \
                        self.TrackFlightData.all_offers[offer_idx].stops_str() + "\n" + \
                        self.TrackFlightData.all_offers[offer_idx].price_str())
            print("-----------------------------------------------------------------")

        print("\n")

    def input_choose_offer(self) -> None:
        self.TrackFlightData.set_selected_flight_choice_idx( \
            int(input(self.input_format("Enter which Flight you would like to Watch"))) - 1)

        print("\n")

    def display_selected_offer(self) -> None:
        print("Selected Flight: " + str(self.TrackFlightData.selected_flight_choice_idx + 1))
        print(self.TrackFlightData.all_offers[self.TrackFlightData.selected_flight_choice_idx])

        print("\n")

    def input_log_parameters(self) -> object:
        num_points = int(input(self.input_format("Enter How Many Points to Plot")))
        time_interval = int(input(self.input_format("Enter in Interval to get Flight Data")))
        limit_value = int(input(self.input_format("Enter in Limit Value")))

        print("\n")
        return {"num_points" : num_points, "time_interval" : time_interval, "limit_value" : limit_value}

    def display_log_plot_completion(self, file_dir, input_plot_values) -> None:
        self.TrackFlightData.set_limit_value(input_plot_values["limit_value"])
        log_file = self.TrackFlightData.log_flight_prices(file_dir, \
                    input_plot_values["num_points"], input_plot_values["time_interval"])
        plot_file = self.TrackFlightData.plot_flight_prices(log_file)

        print("Log File Created at : " + log_file)
        print("Plot File Created at : " + plot_file)
        print("\n")