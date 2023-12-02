from duffel_api import Duffel
from .nodes.Flight import Flight

access_token = "duffel_test_83IaIdX58kDt2kWhvu3mMQZkbZB2mfsfPE5sO-KHld-"
duffel = Duffel(access_token=access_token)


class FlightDataTracker:

    def __init__(self, slices=None, passengers=None, cabin_class=None) -> None:
        self.slices = slices
        self.passengers = passengers
        self.cabin_class = cabin_class
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
            self.slices = [self.slices[0]]

    def set_passengers(self, passengers) -> None:
        self.passengers = passengers

    def set_cabin_class(self, cabin_class) -> None:
        self.cabin_class = cabin_class

    def set_selected_flight(self, selected_flight) -> None:
        self.selected_flight = selected_flight

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
            all_offers.append(Flight(offer))
        return all_offers

    def get_updated_selected_flight_info(self) -> Flight:
        all_offers = self.get_all_offers()

        for offer in all_offers:
            if offer == self.selected_flight:
                return offer
