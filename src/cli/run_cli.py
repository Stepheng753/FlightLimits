#!/usr/bin/env python3

from FlightDataCli import FlightDataCli

if __name__ == "__main__":
    cli = FlightDataCli()
    cli.input_offer_request_parameters()
    cli.TrackFlightData.set_all_offers()
    cli.display_offers()
    cli.input_choose_offer()
    cli.display_selected_offer()
    input_log_values = cli.input_log_parameters()
    cli.display_log_plot_completion("../logs/", input_log_values)