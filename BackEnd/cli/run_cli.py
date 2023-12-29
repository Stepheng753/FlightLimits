#!/usr/bin/env python3

from FlightDataCli import FlightDataCli

if __name__ == "__main__":
    cli = FlightDataCli()
    cli.input_offer_request_parameters()
    all_offers = cli.display_offers()
    selected_flight_idx = cli.input_choose_offer(all_offers)
    cli.display_selected_offer(selected_flight_idx)

    # input_log_values = cli.input_log_parameters()
    # cli.display_log_plot_completion("../logs_test/", input_log_values)

    input_limit_values = cli.input_limit_parameters()
    cli.display_flight_to_order(input_limit_values)
    cli.input_passenger_data()
    cli.display_order_completion()
