import time
from .nodes.Flight import Flight

class FlightDataLimit:

    def __init__(self, Tracker, limit_val) -> None:
        self.Tracker = Tracker
        self.limit_val = limit_val

    def get_flight_at_limit(self, max_iterations, time_interval) -> Flight:
        self.all_offers = [self.Tracker.selected_flight]
        if self.Tracker.selected_flight.total_amount <= self.limit_val:
            return self.Tracker.selected_flight

        for _ in range(0, max_iterations):
            curr_info = self.Tracker.get_updated_selected_flight_info()
            self.all_offers.append(curr_info)
            if curr_info.total_amount <= self.limit_val:
                return curr_info
            time.sleep(time_interval)

        print("Could Not Find Order Under Limit!")
        return -1

    def get_all_offers(self):
        return self.all_offers
