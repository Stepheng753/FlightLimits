from flask import request
from FlightData.FlightDataTracker import FlightDataTracker
from FlightData.FlightDataLogger import FlightDataLogger
from FlightData.FlightDataLimit import FlightDataLimit
from FlightData.FlightDataPmt import FlightDataPmt

def index():
    return {}

def run_preset_params():
    tracker = FlightDataTracker()
    tracker.set_slices(origin="CLT", destination="SAN", depart_date="2024-01-01", return_date="2024-01-30")
    tracker.set_passengers(passengers=[{"age" : 23}])
    tracker.set_cabin_class(cabin_class="economy")
    all_offers = tracker.get_all_offers()
    tracker.set_selected_flight(selected_flight=all_offers[0])

    # logger = FlightDataLogger(Tracker=tracker, log_dir="logs/")
    # logger.get_all_offers(num_iterations=25, time_interval=0)
    # logger.create_log(print_all_offers=True)
    # logger.create_plot(limit_value=450)

    limit = FlightDataLimit(Tracker=tracker, limit_val=450)
    flight = limit.get_flight_at_limit(max_iterations=25, time_interval=0)
    flight.passengers[0].set_age(23)
    flight.passengers[0].set_family_name("TEST")
    flight.passengers[0].set_given_name("Stephen")
    flight.passengers[0].set_title("Mr")
    flight.passengers[0].set_dob("2000-03-02")
    flight.passengers[0].set_gender("M")
    flight.passengers[0].set_phone_number("+18582165827")
    flight.passengers[0].set_email("StephenG753@Gmail.com")

    pmt = FlightDataPmt(flight=flight)
    pmt.create_payment_intent()
    return {"client_token" : pmt.pmt_intent.client_token}

def get_all_offers():
    params = request.get_json()
    origin = params["origin"]
    destination = params["destination"]
    depart_date = params["departDate"]
    return_date = params["returnDate"]
    passengers = []
    for _ in range(0, int(params["numAdults"])):
        passengers.append({"age": 18})
    for _ in range(0, int(params["numChilds"])):
        passengers.append({"age": 1})
    cabin_class = params["cabin"]

    tracker = FlightDataTracker()
    tracker.set_slices(origin=origin, destination=destination, depart_date=depart_date, return_date=return_date)
    tracker.set_passengers(passengers=passengers)
    tracker.set_cabin_class(cabin_class=cabin_class)
    all_offers = tracker.get_all_offers()
    rtn_offers = {}
    for i in range(0, 5):
        rtn_offers[str(i)] = all_offers[i].convertToDict()
    return rtn_offers
