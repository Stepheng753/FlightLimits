import time
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

class FlightDataLogger:

    def __init__(self, Tracker, log_dir) -> None:
        self.Tracker = Tracker
        self.log_dir = log_dir
        self.plot_dir = log_dir + "/plots/"
        self.save_file = self.Tracker.slices[0]["origin"] + "_" + \
                            self.Tracker.slices[0]["destination"] + "-" + \
                                datetime.now().strftime("%m%d%Y_%H-%M")
        self.all_offers = []
        self.currency = self.Tracker.selected_flight.total_currency

    def get_all_offers(self, num_iterations, time_interval=0) -> None:
        self.all_offers = [self.Tracker.selected_flight]

        for _ in range(0, num_iterations - 1):
                time.sleep(time_interval)
                self.all_offers.append(self.Tracker.get_updated_selected_flight_info())

    def create_log(self, print_all_offers=False) -> None:
        log_file_path = self.log_dir + self.save_file + ".log"
        with open(log_file_path, "w") as log_file:
            log_file.write("-----------------------------------------------------------------\n")
            log_file.write(str(self.Tracker.selected_flight.stops_str()) + "\n")
            log_file.write("-----------------------------------------------------------------\n")
            log_file.write("\n")

            for i in range(0, len(self.all_offers)):
                time = self.all_offers[i].created_at
                id = self.all_offers[i].id
                price = self.all_offers[i].total_amount
                log_file.write(time.strftime("%m/%d/%y %I:%M:%S %p") + " :: " + \
                                id + " :: $" + "{0:.2f}".format(price) + " " + self.currency + "\n")

            log_file.write("\n")

            if print_all_offers:
                for i in range(0, len(self.all_offers)):
                    log_file.write(str(self.all_offers[i].offer) + "\n\n")

    def create_plot(self, limit_value=None) -> None:
        time_values = []
        price_values = []
        for i in range(0, len(self.all_offers)):
            time_values.append((self.all_offers[i].created_at - self.all_offers[0].created_at).total_seconds())
            price_values.append(self.all_offers[i].total_amount)

        if limit_value is not None:
            limit_vals = [limit_value for _ in self.all_offers]

        carrier_name = self.Tracker.selected_flight.stops[0]["carrier_name"]
        origin = self.Tracker.slices[0]["origin"]
        destination = self.Tracker.slices[0]["destination"]

        plt.plot(time_values, price_values, color="green", label="Price Data")
        if limit_value is not None:
            plt.plot(time_values, limit_vals, "--", color="orange", label="Limit Value")
        plt.grid(color="0.95")
        plt.title(carrier_name + " : " + origin + " -> " + destination)
        plt.xlabel("Seconds since Flight Selection")
        plt.ylabel("Flight Total Price ($ " + self.currency + ")")
        plt.legend(loc=1)

        plot_file_path = self.plot_dir + self.save_file + ".png"
        plt.savefig(plot_file_path)