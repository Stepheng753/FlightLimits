
from duffel_api import Duffel
from .Flight import Flight
import time
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

access_token = "duffel_test_83IaIdX58kDt2kWhvu3mMQZkbZB2mfsfPE5sO-KHld-"
duffel = Duffel(access_token=access_token)


class TrackFlightData:

    def __init__(self, slices=None, passengers=None, cabin_class=None, limit_value=0) -> None:
        self.slices = slices
        self.passengers = passengers
        self.cabin_class = cabin_class
        self.limit_value = limit_value
        self.selected_flight = None

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

    def set_limit_value(self, limit_value) -> None:
        self.limit_value = limit_value

    def set_selected_flight(self, selected_flight) -> None:
        self.selected_flight = selected_flight

    def offer_to_Flight(self, offer) -> Flight:
        offer_id = offer.id
        stop_info = []

        # This is the TO DESTINATION info and the BACK HOME info
        for each_way_idx in range(0, 2):
            num_stops = len(offer.slices[each_way_idx].segments)

            # This is the seperate stops for each flight
            for stop_idx in range(0, num_stops):
                curr_stop_info = offer.slices[each_way_idx].segments[stop_idx]

                stop_info.append({
                    "carrier_name" : curr_stop_info.marketing_carrier.name,
                    "carrier_iata_code" : curr_stop_info.marketing_carrier.iata_code,
                    "carrier_flight_num" : curr_stop_info.marketing_carrier_flight_number,
                    "origin" : curr_stop_info.origin.iata_code,
                    "destination" : curr_stop_info.destination.iata_code,
                    "depart_time" : curr_stop_info.departing_at,
                    "arrive_time" : curr_stop_info.arriving_at
                    })

        return Flight(id=offer_id, stops=stop_info, base_amt=float(offer.base_amount), fare_taxes=float(offer.tax_amount))

    def get_all_offers(self) -> list:
        offer_request = duffel.offer_requests.create() \
                .slices(self.slices) \
                .passengers(self.passengers) \
                .cabin_class(self.cabin_class) \
                .return_offers() \
                .execute()
        offers = offer_request.offers

        all_offers = []
        for offer in offers:
            curr_flight_offer = self.offer_to_Flight(offer)
            all_offers.append(curr_flight_offer)
        return all_offers

    def get_updated_selected_flight_info(self) -> Flight:
        all_offers = self.get_all_offers()

        for offer in all_offers:
            if offer == self.selected_flight:
                return offer

    def log_flight_prices(self, file_dir, num_iterations, time_interval=0) -> str:
        origin = self.slices[0]["origin"]
        destination = self.slices[0]["destination"]
        current_time = datetime.now().strftime("%m%d%Y_%H-%M")
        save_file = file_dir + origin + "_" + destination + "-" + current_time + ".log"
        with open(save_file, "w") as log_file:
            log_file.write("-----------------------------------------------------------------\n")
            log_file.write(str(self.selected_flight.stops_str()) + "\n")
            log_file.write("-----------------------------------------------------------------\n")
            log_file.write("\n")
            log_file.write(self.selected_flight.time_created.strftime("%m/%d/%y %I:%M:%S %p") + " :: " + \
                            self.selected_flight.id + " :: $" + "{0:.2f}".format(self.selected_flight.total_amt) + "\n")
            for _ in range(0, num_iterations - 1):
                time.sleep(time_interval)
                curr_info = self.get_updated_selected_flight_info()
                log_file.write(curr_info.time_created.strftime("%m/%d/%y %I:%M:%S %p") + " :: " + \
                                curr_info.id + " :: $" + "{0:.2f}".format(curr_info.total_amt) + "\n")

        return save_file

    def plot_flight_prices(self, log_file) -> str:
        time_values = []
        price_values = []

        with open(log_file, "r") as read_log_file:
            lines = read_log_file.readlines()
            first_log_idx = lines.index('\n') + 1
            first_time_val = datetime.strptime(lines[first_log_idx][:20].strip(), "%m/%d/%y %I:%M:%S %p")
            for i in range(first_log_idx, len(lines)):
                time = datetime.strptime(lines[i][:lines[i].index("::") - 1].strip(), "%m/%d/%y %I:%M:%S %p")
                price = float(lines[i][lines[i].index("$") + 1 : ].strip())

                time_values.append((time - first_time_val).total_seconds())
                price_values.append(price)

        limit_vals = [self.limit_value for _ in price_values]

        carrier_name = self.selected_flight.stops[0]["carrier_name"]
        origin = self.slices[0]["origin"]
        destination = self.slices[0]["destination"]

        plt.plot(time_values, price_values, color="green", label="Price Data")
        plt.plot(time_values, limit_vals, "--", color="orange", label="Limit Value")
        plt.grid(color="0.95")
        plt.title(carrier_name + " : " + origin + " -> " + destination)
        plt.xlabel("Seconds since Flight Selection")
        plt.ylabel("Flight Total Price ($ USD)")
        plt.legend(loc=1)

        save_dir = log_file[0 : log_file.rfind("/")] + "/plots/"
        save_file = log_file[log_file.rfind("/") + 1 : log_file.index(".log")] + ".png"
        save_path = save_dir + save_file
        plt.savefig(save_path)

        return save_path

    def calculate_time_interval_btwn_calls(self, total_seconds) -> float:
        MAX_CALLS = 1_500
        return total_seconds / MAX_CALLS


    def get_flight_at_limit(self, total_seconds) -> str:
        time_interval = self.calculate_time_interval_btwn_calls(total_seconds)
        time_interval = 10 if time_interval < 1 else time_interval
        for _ in range(0, 15):
            curr_info = self.get_updated_selected_flight_info()
            if curr_info.total_amt <= self.limit_value:
                print(duffel.offers.get(curr_info.id))
                return curr_info.id
            time.sleep(time_interval)
