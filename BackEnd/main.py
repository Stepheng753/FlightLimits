from flask import request
from FlightData.nodes.Flight import Flight
from FlightData.FlightDataTracker import FlightDataTracker
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
        passengers.append({"type": "adult"})
    for _ in range(0, int(get_param_value(params, "Number of Children"))):
        passengers.append({"type": "child"})
    for _ in range(0, int(get_param_value(params, "Number of Infants"))):
        passengers.append({"type": "infant_without_seat"})
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

    tracker = FlightDataTracker(tracker_info["tracker_slices"],
                                tracker_info["tracker_passengers"],
                                tracker_info["tracker_cabin_class"])
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
    for i in range(0, len(params["adults"])):
        flight.adults[i].set_family_name(get_param_value(params["adults"][str(i)], "Adult Last Name"))
        flight.adults[i].set_given_name(get_param_value(params["adults"][str(i)], "Adult First Name"))
        flight.adults[i].set_title(get_param_value(params["adults"][str(i)], "Adult Title"))
        flight.adults[i].set_dob(get_param_value(params["adults"][str(i)], "Adult Date of Birth"))
        flight.adults[i].set_gender(get_param_value(params["adults"][str(i)], "Adult Gender"))
        flight.adults[i].set_phone_number(get_param_value(params["adults"][str(i)], "Adult Phone Number"))
        flight.adults[i].set_email(get_param_value(params["adults"][str(i)], "Adult Email"))
    for i in range(0, len(params["children"])):
        flight.children[i].set_family_name(get_param_value(params["children"][str(i)], "Child Last Name"))
        flight.children[i].set_given_name(get_param_value(params["children"][str(i)], "Child First Name"))
        flight.children[i].set_title(get_param_value(params["children"][str(i)], "Child Title"))
        flight.children[i].set_dob(get_param_value(params["children"][str(i)], "Child Date of Birth"))
        flight.children[i].set_gender(get_param_value(params["children"][str(i)], "Child Gender"))
        flight.children[i].set_phone_number(get_param_value(params["children"][str(i)], "Child Phone Number"))
        flight.children[i].set_email(get_param_value(params["children"][str(i)], "Child Email"))
    for i in range(0, len(params["infants"])):
        flight.infants[i].set_family_name(get_param_value(params["infants"][str(i)], "Infant Last Name"))
        flight.infants[i].set_given_name(get_param_value(params["infants"][str(i)], "Infant First Name"))
        flight.infants[i].set_title(get_param_value(params["infants"][str(i)], "Infant Title"))
        flight.infants[i].set_dob(get_param_value(params["infants"][str(i)], "Infant Date of Birth"))
        flight.infants[i].set_gender(get_param_value(params["infants"][str(i)], "Infant Gender"))
        flight.infants[i].set_phone_number(get_param_value(params["infants"][str(i)], "Infant Phone Number"))
        flight.infants[i].set_email(get_param_value(params["infants"][str(i)], "Infant Email"))

    pmt = FlightDataPmt(flight=flight)
    order = pmt.create_order()
    if order.id != None:
        return {"order" : order, "success" : True, "error": "Failed"}
    return {"success" : False, "error" : "Could Not Place Order"}
