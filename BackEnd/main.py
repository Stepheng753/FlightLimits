from flask import request
from FlightData.nodes.Flight import Flight
from FlightData.FlightDataTracker import FlightDataTracker
from FlightData.FlightDataLogger import FlightDataLogger
from FlightData.FlightDataLimit import FlightDataLimit
from FlightData.FlightDataPmt import FlightDataPmt

def get_param_value(params, key):
    return params["data"][params["indices"][key]]["value"]

def index():
    return {}

def get_all_offers():
    params = request.get_json()
    origin = get_param_value(params, "Origin")
    destination = get_param_value(params, "Destination")
    depart_date = get_param_value(params, "Depart Date")
    return_date = get_param_value(params, "Return Date")
    passengers = []
    for _ in range(0, int(get_param_value(params, "Number of Adults"))):
        passengers.append({"age": 18})
    for _ in range(0, int(get_param_value(params, "Number of Children"))):
        passengers.append({"age": 1})
    cabin_class = get_param_value(params, "Cabin")

    tracker = FlightDataTracker()
    tracker.set_slices(origin=origin, destination=destination, depart_date=depart_date, return_date=return_date)
    tracker.set_passengers(passengers=passengers)
    tracker.set_cabin_class(cabin_class=cabin_class)
    all_offers = tracker.get_all_offers()
    tracker_info = {"tracker_slices": tracker.slices,
                    "tracker_passengers" : tracker.passengers,
                    "tracker_cabin_class" : tracker.cabin_class}
    offer_info = {}
    for i in range(0, 5):
        offer_info[str(i)] = all_offers[i].convertToDict()
    return {"tracker_info" : tracker_info, "offer_info" : offer_info}

def get_offer_below_limit():
    params = request.get_json()
    id = params["flight_id"]
    tracker_info = params["tracker_info"]
    max_iterations = int(get_param_value(params, "Max Iterations"))
    time_interval = int(get_param_value(params, "Time Interval"))
    limit_val = int(get_param_value(params, "Limit Value"))

    tracker = FlightDataTracker(tracker_info["tracker_slices"], tracker_info["tracker_passengers"], tracker_info["tracker_cabin_class"])
    offer = tracker.get_offer(id)
    tracker.set_selected_flight(Flight(offer))

    limit = FlightDataLimit(Tracker=tracker, limit_val=limit_val)
    flight = limit.get_flight_at_limit(max_iterations=max_iterations, time_interval=time_interval)

    if flight != -1:
            return {"flight": flight.convertToDict()}

    return {"ERROR": "Could Not Find Order Under Limit!"}

def order_flight():
    params = request.get_json()
    tracker = FlightDataTracker()
    flight = Flight(tracker.get_offer(params["flight_id"]))
    flight.passengers[0].set_family_name(get_param_value(params, "Last Name"))
    flight.passengers[0].set_given_name(get_param_value(params, "First Name"))
    flight.passengers[0].set_title(get_param_value(params, "Title"))
    flight.passengers[0].set_dob(get_param_value(params, "Date of Birth"))
    flight.passengers[0].set_gender(get_param_value(params, "Gender"))
    flight.passengers[0].set_phone_number(get_param_value(params, "Phone Number"))
    flight.passengers[0].set_email(get_param_value(params, "Email"))


    pmt = FlightDataPmt(flight=flight)
    order = pmt.create_order()
    if order.id != None:
        return {"order" : order, "success" : True, "error": "Failed"}
    return {"success" : False, "error" : "Could Not Place Order"}
