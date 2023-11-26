from duffel_api import Duffel

access_token = "duffel_test_83IaIdX58kDt2kWhvu3mMQZkbZB2mfsfPE5sO-KHld-"
duffel = Duffel(access_token=access_token)

class FlightDataPmt:

    def __init__(self, flight, markup=0) -> None:
        self.flight = flight
        self.markup = markup

    def calculate_customer_charge(self) -> float:
        flight_cost = self.flight.total_amount
        duffel_order_fee = 3.00
        duffel_manage_content_fee = .01
        return round(((flight_cost + self.markup) / (1 - duffel_manage_content_fee)) + duffel_order_fee, 2)

    def create_payment_intent(self) -> object:
        total_amount = self.calculate_customer_charge()
        currency = self.flight.total_currency
        payment = {"amount" : "{0:.2f}".format(total_amount), "currency" : currency}
        self.pmt_intent = duffel.payment_intents.create() \
                                        .payment(payment) \
                                        .execute()

    def confirm_payment(self):
        print(duffel.payment_intents.confirm(self.pmt_intent.id))

    def create_order(self):
        payment = {"amount" : self.flight.total_amount, "currency" : self.flight.total_currency, "type" : "balance"}
        order = duffel.orders.create() \
                        .selected_offers([self.flight.id]) \
                        .payments([payment]) \
                        .passengers(self.flight.get_passengers_list_dict()) \
                        .execute()
        return order