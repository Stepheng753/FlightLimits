from datetime import datetime

class Flight:

    def __init__(self, id=None, stops=None, base_amt=None, fare_taxes=None) -> None:
        self.id = id
        self.stops = stops
        self.base_amt = base_amt
        self.fare_taxes = fare_taxes
        self.total_amt = round(base_amt + fare_taxes, 2)
        self.time_created = datetime.now()

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
        price_string += "Base Amount".ljust(13) + ": $" + str(self.base_amt) + "\n"
        price_string += "Fare Taxes".ljust(13) + ": $" + str(self.fare_taxes) + "\n"
        price_string += "Total Amount".ljust(13) + ": $" + str(self.total_amt)
        return price_string.strip()

    def __eq__(self, __value: object) -> bool:
        return self.stops == __value.stops