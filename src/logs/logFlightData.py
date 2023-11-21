#!/usr/bin/env python3

from duffel_api import Duffel

access_token = "duffel_test_83IaIdX58kDt2kWhvu3mMQZkbZB2mfsfPE5sO-KHld-"
duffel = Duffel(access_token=access_token)

slices = [
  {
    "origin": "SAN",
    "destination": "ANC",
    "departure_date": "2023-12-20",
  },
  {
    "origin": "ANC",
    "destination": "SAN",
    "departure_date": "2023-12-30"
  }
]
passengers = [{ "type": "adult" }]
cabin_class = "economy"

offer_request = duffel.offer_requests.create() \
                                        .slices(slices) \
                                        .passengers(passengers) \
                                        .cabin_class(cabin_class) \
                                        .return_offers() \
                                        .execute()
offers = offer_request.offers
print_all_offers = True

if print_all_offers:
  with open("all_offers.log", "w") as all_offers_txt:
      for offer in offers:
          all_offers_txt.write(str(offer))
          all_offers_txt.write("\n\n")

with open('offer.log', 'w') as offer_txt:
    # This is all the flights given the info above
    for offer_idx in range(0, 15):
        offer_id = offers[offer_idx].id
        offer_txt.write("-----------------------------------------------------------------\n")
        offer_txt.write("ID: " + offer_id + "\n")

        # This is the TO DESTINATION info and the BACK HOME info
        for each_way_idx in range(0, 2):
            num_stops = len(offers[offer_idx].slices[each_way_idx].segments)

            # This is the seperate stops for each flight
            for stop_idx in range(0, num_stops):
                curr_stop_info = offers[offer_idx].slices[each_way_idx].segments[stop_idx]

                airline_info     = curr_stop_info.marketing_carrier.name + " : " + \
                                    curr_stop_info.marketing_carrier.iata_code + curr_stop_info.marketing_carrier_flight_number
                depart_city_code = curr_stop_info.origin.iata_code
                arrive_city_code = curr_stop_info.destination.iata_code
                depart_time      = curr_stop_info.departing_at
                arrive_time      = curr_stop_info.arriving_at

                offer_txt.write(airline_info.ljust(24) + " Departing " + depart_city_code + " at : " + str(depart_time) + "\n")
                offer_txt.write(airline_info.ljust(24) + " Arriving  " + arrive_city_code + " at : " + str(arrive_time) + "\n")

            offer_txt.write("\n")

        offer_txt.write("Base Amount".ljust(13) + ": $" + str(offers[offer_idx].base_amount) + "\n")
        offer_txt.write("Fare Taxes".ljust(13) + ": $" + str(offers[offer_idx].tax_amount) + "\n")
        offer_txt.write("Total Amount".ljust(13) + ": $" + str(offers[offer_idx].total_amount) + "\n")
        offer_txt.write("-----------------------------------------------------------------\n")