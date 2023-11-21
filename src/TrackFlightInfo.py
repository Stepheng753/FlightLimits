#!/usr/bin/env python3

from duffel_api import Duffel
from Flight import Flight
import time
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

access_token = "duffel_test_83IaIdX58kDt2kWhvu3mMQZkbZB2mfsfPE5sO-KHld-"
duffel = Duffel(access_token=access_token)


class TrackFlightInfo:

    def __init__(self, slices=None, passengers=None, cabin_class=None) -> None:
        self.slices = slices
        self.passengers = passengers
        self.cabin_class = cabin_class
        self.all_flights = []

    def set_slices(self, origin, destination, depart_date, arrive_date=None) -> None:
        self.slices = [{
            "origin": origin,
            "destination": destination,
            "departure_date": depart_date,
        },
        {
            "origin": destination,
            "destination": origin,
            "departure_date": arrive_date,
        }]
        if arrive_date is None:
            self.slices = self.slices[0]

    def set_passengers(self, passengers) -> None:
        self.passengers = passengers

    def set_cabin_class(self, cabin_class) -> None:
        self.cabin_class = cabin_class

    def set_selected_flight_choice_idx(self, selected_flight_choice_idx):
        self.selected_flight_choice_idx = selected_flight_choice_idx

    def input_offer_request_parameters(self) -> None:
        input_format = lambda x: (x).ljust(45) + ": "

        origin = input(input_format("Enter in the IATA Origin Airport Code"))
        destination = input(input_format("Enter in the IATA Destination Airport Code"))

        print("One Way or Round Trip")
        print("\t1) One Way")
        print("\t2) Round Trip")
        one_round_way = input(input_format("Enter One Way or Round Trip"))
        depart_date = input(input_format("Enter in Departure Date (YYYY-MM-DD)"))
        arrive_date = None
        if ("2" in one_round_way.lower()) or ("round" in one_round_way.lower()):
            arrive_date = input(input_format("Enter in Arrival Date (YYYY-MM-DD)"))

        num_adult_passengers = int(input(input_format("Enter in the Number of Adult Passengers")))
        num_child_passengers = int(input(input_format("Enter in the Number of Child Passengers")))
        passengers = []
        for _ in range(0, num_adult_passengers):
            passengers.append({"type" : "adult"})
        for child_idx in range(1, num_child_passengers + 1):
            age = int(input((input_format("Enter in Age of Child #" + str(child_idx) ))))
            passengers.append({"age" : age})

        cabin_classes = ["first", "business", "premium_economy", "economy"]
        print("All Types of Cabin Classes")
        for cabin_idx in range(0, len(cabin_classes)):
            print("\t" + str(cabin_idx + 1) + ") " + cabin_classes[cabin_idx].capitalize())
        cabin_class_idx = int(input(input_format("Enter in the Cabin Class")))

        self.set_slices(origin, destination, depart_date, arrive_date)
        self.set_passengers(passengers)
        self.set_cabin_class(cabin_classes[cabin_class_idx - 1])

        print()

    def display_offers(self) -> None:
        offer_request = duffel.offer_requests.create() \
                .slices(self.slices) \
                .passengers(self.passengers) \
                .cabin_class(self.cabin_class) \
                .return_offers() \
                .execute()

        offers = offer_request.offers

        for offer_idx in range(0, 5):
            offer_id = offers[offer_idx].id
            stop_info = []

            # This is the TO DESTINATION info and the BACK HOME info
            for each_way_idx in range(0, 2):
                num_stops = len(offers[offer_idx].slices[each_way_idx].segments)

                # This is the seperate stops for each flight
                for stop_idx in range(0, num_stops):
                    curr_stop_info = offers[offer_idx].slices[each_way_idx].segments[stop_idx]

                    stop_info.append({
                        "carrier_name" : curr_stop_info.marketing_carrier.name,
                        "carrier_iata_code" : curr_stop_info.marketing_carrier.iata_code,
                        "carrier_flight_num" : curr_stop_info.marketing_carrier_flight_number,
                        "origin" : curr_stop_info.origin.iata_code,
                        "destination" : curr_stop_info.destination.iata_code,
                        "depart_time" : curr_stop_info.departing_at,
                        "arrive_time" : curr_stop_info.arriving_at
                        })

            curr_flight_offer = Flight(id=offer_id, stops=stop_info, base_amt=float(offers[offer_idx].base_amount), fare_taxes=float(offers[offer_idx].tax_amount))
            self.all_flights.append(curr_flight_offer)
            print("-----------------------------------------------------------------")
            print("Choice: " + str(offer_idx + 1) + "\n" + curr_flight_offer.stops_str() + "\n" + curr_flight_offer.price_str())
            print("-----------------------------------------------------------------")

        print("\n")

    def input_choose_offer(self) -> None:
        input_format = lambda x: (x).ljust(45) + ": "
        self.selected_flight_choice_idx = int(input(input_format("Enter which Flight you would like to Watch"))) - 1

    def select_flight(self) -> object:
        print("Selected Flight: " + str(self.selected_flight_choice_idx + 1))
        print(self.all_flights[self.selected_flight_choice_idx])
        current_time = datetime.now()
        current_total_price = self.all_flights[self.selected_flight_choice_idx].total_amt
        return {"time" : current_time, "price" : current_total_price}

    def watch_flight(self) -> object:
        offer_request = duffel.offer_requests.create() \
                .slices(self.slices) \
                .passengers(self.passengers) \
                .cabin_class(self.cabin_class) \
                .return_offers() \
                .execute()

        offers = offer_request.offers

        for offer_idx in range(0, 5):
            offer_id = offers[offer_idx].id
            stop_info = []

            # This is the TO DESTINATION info and the BACK HOME info
            for each_way_idx in range(0, 2):
                num_stops = len(offers[offer_idx].slices[each_way_idx].segments)

                # This is the seperate stops for each flight
                for stop_idx in range(0, num_stops):
                    curr_stop_info = offers[offer_idx].slices[each_way_idx].segments[stop_idx]

                    stop_info.append({
                        "carrier_name" : curr_stop_info.marketing_carrier.name,
                        "carrier_iata_code" : curr_stop_info.marketing_carrier.iata_code,
                        "carrier_flight_num" : curr_stop_info.marketing_carrier_flight_number,
                        "origin" : curr_stop_info.origin.iata_code,
                        "destination" : curr_stop_info.destination.iata_code,
                        "depart_time" : curr_stop_info.departing_at,
                        "arrive_time" : curr_stop_info.arriving_at
                        })

            curr_flight_offer = Flight(id=offer_id, stops=stop_info, base_amt=float(offers[offer_idx].base_amount), fare_taxes=float(offers[offer_idx].tax_amount))

            if curr_flight_offer == self.all_flights[self.selected_flight_choice_idx]:
                current_time = datetime.now()
                current_total_price = curr_flight_offer.total_amt
                return {"time" : current_time, "price" : current_total_price}

    def plot_flight_prices(self, num_iterations, limit_value=0, time_interval=0):
        og_info = self.select_flight()
        x_vals = [(og_info["time"] - og_info["time"]).total_seconds()]
        y_vals = [og_info["price"]]
        for i in range(0, num_iterations - 1):
            time.sleep(time_interval)
            curr_info = self.watch_flight()
            x_vals.append((curr_info["time"] - og_info["time"]).total_seconds())
            y_vals.append(curr_info["price"])
        y_vals_limit = [limit_value for _ in y_vals]

        plt.plot(x_vals, y_vals, color="green", label="Price Data")
        plt.plot(x_vals, y_vals_limit, "--", color="orange", label="Limit Value")
        plt.grid(color="0.95")
        plt.title("Flight Values over Time")
        plt.xlabel("Seconds since Flight Selection")
        plt.ylabel("Flight Total Price ($ USD)")
        plt.legend(loc=1)
        plt.savefig("plots/SAN_to_ANC.png")


if __name__ == "__main__":
    tracker = TrackFlightInfo()
    input_params = False

    if input_params:
        tracker.input_offer_request_parameters()
        tracker.input_choose_offer()
    else:
        tracker.set_slices("SAN", "ANC", "2023-12-20", "2023-12-30")
        tracker.set_passengers([{"type" : "adult"}])
        tracker.set_cabin_class("economy")
        tracker.set_selected_flight_choice_idx(0)

    tracker.display_offers()
    tracker.plot_flight_prices(100, 375)
