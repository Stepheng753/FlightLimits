from .Passenger import Passenger

class Flight:

    def __init__(self, offer) -> None:
        self.offer = offer
        self.set_id()
        self.set_stops()
        self.set_base_amt()
        self.set_fare_taxes()
        self.set_total_amount()
        self.set_total_currency()
        self.set_created_at()
        self.set_passengers()

    def set_id(self):
        self.id = self.offer.id

    def set_stops(self):
        self.stops = []

        # This is the TO DESTINATION info and the BACK HOME info
        for each_way_idx in range(0, 2):
            num_stops = len(self.offer.slices[each_way_idx].segments)

            # This is the seperate stops for each flight
            for stop_idx in range(0, num_stops):
                curr_stop_info = self.offer.slices[each_way_idx].segments[stop_idx]

                self.stops.append({
                    "carrier_name" : curr_stop_info.marketing_carrier.name,
                    "carrier_iata_code" : curr_stop_info.marketing_carrier.iata_code,
                    "carrier_flight_num" : curr_stop_info.marketing_carrier_flight_number,
                    "origin" : curr_stop_info.origin.iata_code,
                    "destination" : curr_stop_info.destination.iata_code,
                    "depart_time" : curr_stop_info.departing_at,
                    "arrive_time" : curr_stop_info.arriving_at
                    })

    def set_base_amt(self):
        self.base_amt = float(self.offer.base_amount)

    def set_fare_taxes(self):
        self.fare_taxes = float(self.offer.tax_amount)

    def set_total_amount(self):
        self.total_amount = float(self.offer.total_amount)

    def set_total_currency(self):
        self.total_currency = self.offer.total_currency

    def set_created_at(self):
        self.created_at = self.offer.created_at

    def set_passengers(self):
        self.passengers = []
        self.infants = []
        for i in range(0, len(self.offer.passengers)):
            if "infant" in self.offer.passengers[i].type:
                self.infants.append(Passenger(self.offer.passengers[i].id, self.offer.passengers[i].type))
            else:
                self.passengers.append(Passenger(self.offer.passengers[i].id, self.offer.passengers[i].type))

    def get_passengers_list_dict(self):
        passenger_list_dict = []
        for passenger in self.passengers:
            passenger_list_dict.append(passenger.to_dict())
        for infant in self.infants:
            passenger_list_dict.append(infant.to_dict())
        return passenger_list_dict


    def __str__(self) -> str:
        rtnStr = "-----------------------------------------------------------------\n"
        rtnStr += self.stops_str() + "\n"
        rtnStr += self.price_str() + "\n"
        rtnStr += "-----------------------------------------------------------------"
        return rtnStr

    def stops_str(self) -> str:
        stops_string = ""
        for stop_idx in range(0, len(self.stops)):
            carrier_info = (self.stops[stop_idx]["carrier_name"] + " : " + \
                       self.stops[stop_idx]["carrier_iata_code"] + self.stops[stop_idx]["carrier_flight_num"]).ljust(24)
            depart_info = "Departing " + self.stops[stop_idx]["origin"] + " at : " + str(self.stops[stop_idx]["depart_time"])
            arrive_info = "Arriving  " + self.stops[stop_idx]["destination"] + " at : " + str(self.stops[stop_idx]["arrive_time"])
            stops_string += carrier_info + " : " + depart_info + "\n"
            stops_string += carrier_info + " : " + arrive_info + "\n"
        return stops_string.strip()

    def price_str(self) -> str:
        price_string = ""
        price_string += "Base Amount".ljust(13) + ": $" + str(self.base_amt) + " " + self.total_currency + "\n"
        price_string += "Fare Taxes".ljust(13) + ": $" + str(self.fare_taxes) + " " + self.total_currency + "\n"
        price_string += "Total Amount".ljust(13) + ": $" + str(self.total_amount) + " " + self.total_currency
        return price_string.strip()

    def __eq__(self, __value: object) -> bool:
        return self.stops == __value.stops