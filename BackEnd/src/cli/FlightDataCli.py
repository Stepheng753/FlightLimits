#!/usr/bin/env python3

import sys
sys.path.append('../')

from FlightData.FlightDataTracker import FlightDataTracker
from FlightData.FlightDataLogger import FlightDataLogger
from FlightData.FlightDataLimit import FlightDataLimit
from FlightData.FlightDataPmt import FlightDataPmt

class FlightDataCli:

    def __init__(self) -> None:
        self.tracker = FlightDataTracker()
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

        self.tracker.set_slices(origin, destination, depart_date, arrive_date)
        self.tracker.set_passengers(passengers)
        self.tracker.set_cabin_class(cabin_classes[cabin_class_idx - 1])

        print("\n")

    def display_offers(self) -> None:
        all_offers = self.tracker.get_all_offers()
        for offer_idx in range(0, 5):
            print("-----------------------------------------------------------------")
            print("Choice: " + str(offer_idx + 1) + "\n" + \
                        all_offers[offer_idx].stops_str() + "\n" + \
                        all_offers[offer_idx].price_str())
            print("-----------------------------------------------------------------")

        print("\n")
        return all_offers

    def input_choose_offer(self, all_offers) -> None:
        selected_flight_idx = int(input(self.input_format("Enter which Flight you would like to Watch"))) - 1
        self.tracker.set_selected_flight(all_offers[selected_flight_idx])

        print("\n")
        return selected_flight_idx

    def display_selected_offer(self, selected_flight_idx) -> None:
        print("Selected Flight: " + str(selected_flight_idx + 1))
        print(self.tracker.selected_flight)

        print("\n")

    def input_log_parameters(self) -> object:
        num_points = int(input(self.input_format("Enter How Many Points to Plot")))
        time_interval = int(input(self.input_format("Enter in Interval to get Flight Data")))
        limit_value = int(input(self.input_format("Enter in Limit Value")))

        print("\n")
        return {"num_points" : num_points, "time_interval" : time_interval, "limit_value" : limit_value}

    def display_log_plot_completion(self, log_dir, input_log_values) -> None:
        logger = FlightDataLogger(self.tracker, log_dir)
        logger.set_times_prices(input_log_values["num_points"], input_log_values["time_interval"])
        logger.create_log()
        logger.create_plot(input_log_values["limit_value"])

        print("Log File Created at : " + logger.log_dir + logger.save_file + ".log")
        print("Plot File Created at : " + logger.plot_dir + logger.save_file + ".log")
        print("\n")

    def input_limit_parameters(self) -> object:
        num_points = int(input(self.input_format("Enter the Max Num of Iterations")))
        time_interval = int(input(self.input_format("Enter in Interval to get Flight Data")))
        limit_value = int(input(self.input_format("Enter in Limit Value")))

        print("\n")
        return {"num_iterations" : num_points, "time_interval" : time_interval, "limit_value" : limit_value}

    def display_flight_to_order(self, input_limit_values) -> None:
        limit = FlightDataLimit(self.tracker, input_limit_values["limit_value"])
        self.order_flight = limit.get_flight_at_limit(input_limit_values["num_iterations"], input_limit_values["time_interval"])

        print(self.order_flight)
        print("\n")

    def input_passenger_data(self):
        for i in range(0, len(self.order_flight.infants)):
            age = float(input(self.input_format("Infant #" + str(i + 1) + " Enter in Age")))
            family_name = input(self.input_format("Infant #" + str(i + 1) + " Enter in the Family Name"))
            given_name = input(self.input_format("Infant #" + str(i + 1) + " Enter in the Given Name"))
            title = input(self.input_format("Infant #" + str(i + 1) + " Enter in Title"))
            dob = input(self.input_format("Infant #" + str(i + 1) + " Enter in Date of Birth (YYYY-MM-DD)"))
            gender = input(self.input_format("Infant #" + str(i + 1) + " Enter in Gender"))
            phone_number = input(self.input_format("Infant #" + str(i + 1) + " Enter in Phone Number"))
            email = input(self.input_format("Infant #" + str(i + 1) + " Enter in Email"))
            self.order_flight.infants[i].set_age(age)
            self.order_flight.infants[i].set_family_name(family_name)
            self.order_flight.infants[i].set_given_name(given_name)
            self.order_flight.infants[i].set_title(title)
            self.order_flight.infants[i].set_dob(dob)
            self.order_flight.infants[i].set_gender(gender)
            self.order_flight.infants[i].set_phone_number(phone_number)
            self.order_flight.infants[i].set_email(email)
            print()
        j = 0
        for i in range(0, len(self.order_flight.passengers)):
            age = float(input(self.input_format("Passenger #" + str(i + 1) + " Enter in Age")))
            family_name = input(self.input_format("Passenger #" + str(i + 1) + " Enter in the Family Name"))
            given_name = input(self.input_format("Passenger #" + str(i + 1) + " Enter in the Given Name"))
            title = input(self.input_format("Passenger #" + str(i + 1) + " Enter in Title"))
            dob = input(self.input_format("Passenger #" + str(i + 1) + " Enter in Date of Birth (YYYY-MM-DD)"))
            gender = input(self.input_format("Passenger #" + str(i + 1) + " Enter in Gender"))
            phone_number = input(self.input_format("Passenger #" + str(i + 1) + " Enter in Phone Number"))
            email = input(self.input_format("Passenger #" + str(i + 1) + " Enter in Email"))
            self.order_flight.passengers[i].set_age(age)
            self.order_flight.passengers[i].set_family_name(family_name)
            self.order_flight.passengers[i].set_given_name(given_name)
            self.order_flight.passengers[i].set_title(title)
            self.order_flight.passengers[i].set_dob(dob)
            self.order_flight.passengers[i].set_gender(gender)
            self.order_flight.passengers[i].set_phone_number(phone_number)
            self.order_flight.passengers[i].set_email(email)
            if j < len(self.order_flight.infants):
                self.order_flight.passengers[i].set_infant_passenger_id(self.order_flight.infants[j].id)
                j += 1
            print()

        print()

    def display_order_completion(self):
        pmt = FlightDataPmt(self.order_flight)
        order = pmt.create_order()

        print("Order Created at " + str(order.id))