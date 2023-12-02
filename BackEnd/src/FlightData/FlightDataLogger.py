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
        self.times = []
        self.prices = []
        self.ids = []
        self.currency = self.Tracker.selected_flight.total_currency

    def set_times_prices(self, num_iterations, time_interval=0) -> None:
        self.times = [self.Tracker.selected_flight.created_at]
        self.ids = [self.Tracker.selected_flight.id]
        self.prices = [self.Tracker.selected_flight.total_amount]

        for _ in range(0, num_iterations - 1):
                time.sleep(time_interval)
                curr_info = self.Tracker.get_updated_selected_flight_info()
                self.times.append(curr_info.created_at)
                self.ids.append(curr_info.id)
                self.prices.append(curr_info.total_amount)

    def create_log(self) -> None:
        log_file_path = self.log_dir + self.save_file + ".log"
        with open(log_file_path, "w") as log_file:
            log_file.write("-----------------------------------------------------------------\n")
            log_file.write(str(self.Tracker.selected_flight.stops_str()) + "\n")
            log_file.write("-----------------------------------------------------------------\n")
            log_file.write("\n")

            for i in range(0, len(self.times)):
                log_file.write(self.times[i].strftime("%m/%d/%y %I:%M:%S %p") + " :: " + \
                                self.ids[i] + " :: $" + "{0:.2f}".format(self.prices[i]) + " " + self.currency + "\n")

    def create_plot(self, limit_value=None) -> None:
        time_values = []
        for i in range(0, len(self.times)):
            time_values.append((self.times[i] - self.times[0]).total_seconds())

        if limit_value is not None:
            limit_vals = [limit_value for _ in self.prices]

        carrier_name = self.Tracker.selected_flight.stops[0]["carrier_name"]
        origin = self.Tracker.slices[0]["origin"]
        destination = self.Tracker.slices[0]["destination"]

        plt.plot(time_values, self.prices, color="green", label="Price Data")
        if limit_value is not None:
            plt.plot(time_values, limit_vals, "--", color="orange", label="Limit Value")
        plt.grid(color="0.95")
        plt.title(carrier_name + " : " + origin + " -> " + destination)
        plt.xlabel("Seconds since Flight Selection")
        plt.ylabel("Flight Total Price ($ " + self.currency + ")")
        plt.legend(loc=1)

        plot_file_path = self.plot_dir + self.save_file + ".png"
        plt.savefig(plot_file_path)
