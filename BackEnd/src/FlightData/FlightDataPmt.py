from duffel_api import Duffel
import json

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

    def create_payment_intent(self):
        total_amount = self.calculate_customer_charge()
        currency = self.flight.total_currency
        payment = {"amount" : "{0:.2f}".format(total_amount), "currency" : currency}
        self.pmt_intent = duffel.payment_intents.create() \
                                        .payment(payment) \
                                        .execute()

    def write_payment_intent_info(self, dir):
        file_name = dir + "/pmt_intent.json"
        pmt_intent_dict = {"id" : self.pmt_intent.id, "amount" : self.pmt_intent.amount, "currency" : self.pmt_intent.currency,
                            "client_token" : self.pmt_intent.client_token,
                            "created_at" : self.pmt_intent.created_at.strftime("%m%d%Y_%H%M%S"),
                            "updated_at" : self.pmt_intent.updated_at.strftime("%m%d%Y_%H%M%S")}
        pmt_intent_json = json.dumps(pmt_intent_dict, indent=4)

        with open(file_name, "w") as json_file:
            json_file.write(pmt_intent_json)

    def create_order(self):
        payment = {"amount" : self.flight.total_amount, "currency" : self.flight.total_currency, "type" : "balance"}
        order = duffel.orders.create() \
                        .selected_offers([self.flight.id]) \
                        .payments([payment]) \
                        .passengers(self.flight.get_passengers_list_dict()) \
                        .execute()
        return order