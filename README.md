[CLT_SAN-12022023_04-37.log](https://github.com/Stepheng753/FlightLimits/files/13534610/CLT_SAN-12022023_04-37.log)

# FlightLimits

## Introduction 
FlightLimits is an innovative tool leveraging Flight APIs to enable users to place limit orders for flight tickets at specified prices. It's designed for versatility, offering support for different markets and a variety of order types.

The aim of this project is to create a generic limit order tool for setting limit order on whatever site we would like with little to no custom tailoring needed by the end user.

## Getting Started 

Before you begin using FlightLimits you will need [git](https://git-scm.com/download/mac) and [python](https://www.python.org/downloads/) installed on your machine.

You should also familiarize yourself with how we retrieve flight data using the [Duffel API](https://duffel.com/docs/guides/getting-started-with-flights).

To run FlightLimits, execute the following commands in your terminal:

```gh repo clone Stepheng753/FlightLimits``` # Clone this repo, you may also download [by clicking here](https://github.com/Stepheng753/FlightLimits/archive/refs/heads/main.zip)

```cd FlightLimits``` # Navigate into the FlightLimits project directory

```pip install matplotlib ```         # For data visualization

```pip install duffel-api ```        # To interact with Duffel's flight API 

```python run.py```                            # To execute the program



## How to customize

Run.py contains several parameters that affect which flight tickets we monitor, and how we monitor them for you

You can choose between the following customizations:

-   **Departure Date**: Set your intended date of departure.
-   **Departure Airport**: Choose your airport of departure.
-   **Arrival Airport**: Select your desired destination airport.
-   **Trip Type**: Opt for One Way or Round Trip.
-   **Return Date**: Specify return date for round trips.
-   **Time of Takeoff**: Select preferred takeoff time.
-   **Number of Flight Legs**: Define the number of legs for your journey.
-   **Passenger Age**: Input passenger age for targeted searches.
-   **Cabin Class**: Choose the cabin class (e.g., Economy, Business).


## Output 

Currently, FlightLimits produces 2 different visualizations, text-based and plotted as shown below, with each timestamp representing a possible buy order at that 





![CLT_SAN-12022023_04-55](https://github.com/Stepheng753/FlightLimits/assets/28160617/a4af424b-3a66-4ceb-9dd3-d15111871427)

Log file example 


| Airline           | Flight | Status      | Date & Time           |
|-------------------|--------|-------------|-----------------------|
| American Airlines | AA118  | Departing   | 2024-03-01 00:00:00   |
| American Airlines | AA118  | Arriving    | 2024-03-01 02:01:00   |
| American Airlines | AA118  | Departing   | 2024-03-30 22:27:00   |
| American Airlines | AA118  | Arriving    | 2024-03-31 06:28:00   |

- 12/02/23 09:37:30 AM :: off_0000AcOY4cyW4v7zz88ye6 :: $328.79 USD
- 12/02/23 09:37:32 AM :: off_0000AcOY4tIFPKPyaxUxca :: $328.68 USD
- 12/02/23 09:37:36 AM :: off_0000AcOY5CpukNdbCsOcEe :: $345.48 USD
- 12/02/23 09:37:39 AM :: off_0000AcOY5WZR1cwfNCWHAq :: $336.33 USD
- 12/02/23 09:37:42 AM :: off_0000AcOY5miB0tRdQwjU1L :: $334.02 USD
- 12/02/23 09:37:45 AM :: off_0000AcOY65EO9ruGs3wSjT :: $322.97 USD
- 12/02/23 09:37:48 AM :: off_0000AcOY6Lp8T0o8KfG2E8 :: $323.52 USD
- 12/02/23 09:37:52 AM :: off_0000AcOY6ghkpeNh5qxw8a :: $334.28 USD
- 12/02/23 09:37:55 AM :: off_0000AcOY6wFH3J6fI9lPy5 :: $336.55 USD
- 12/02/23 09:37:57 AM :: off_0000AcOY7Cl3eu2OVMl1jI :: $322.40 USD
- 12/02/23 09:38:00 AM :: off_0000AcOY7SNBbQRuvxiBk6 :: $326.95 USD
- 12/02/23 09:38:03 AM :: off_0000AcOY7hfoiRGUO5XmMi :: $343.38 USD
- 12/02/23 09:38:05 AM :: off_0000AcOY7w9OtFFPHtUbQ2 :: $336.47 USD
- 12/02/23 09:38:08 AM :: off_0000AcOY89tFo4eNts2uCE :: $331.14 USD
- 12/02/23 09:38:10 AM :: off_0000AcOY8O0VJulhgPXtRT :: $342.12 USD
- 12/02/23 09:38:13 AM :: off_0000AcOY8bzbK4Mf3fEMya :: $330.69 USD
- 12/02/23 09:38:15 AM :: off_0000AcOY8rJeLoJYaBj5oC :: $347.25 USD
- 12/02/23 09:38:18 AM :: off_0000AcOY95UReTGgXisuZu :: $342.42 USD
- 12/02/23 09:38:21 AM :: off_0000AcOY9LA7NoW19JUu7L :: $326.05 USD
- 12/02/23 09:38:23 AM :: off_0000AcOY9ZGewI4AtefKFv :: $336.05 USD
- 12/02/23 09:38:26 AM :: off_0000AcOY9nkx4ScFpewiPp :: $337.11 USD




## Book A Flight

To use this to book a flight and not just monitor... docs coming soon


## Premium Upgrades
Check for the customer more often
Tools with which you can select from, extra options




## To Do

* Build a Front End Application - React, React Native
* Upload Flight Data to Database
* Host remote server to call API's at specific times
* Exception Handling all around
* Process Payments - Need Front End First
