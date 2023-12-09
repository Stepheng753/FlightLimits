# FlightLimits

## Introduction

FlightLimits is an innovative tool leveraging Flight APIs to enable users to place limit orders for flight tickets at specified prices. It's designed for versatility, offering support for different markets and a variety of order types.

The aim of this project is to create a generic limit order tool for setting limit order on whatever site we would like with little to no custom tailoring needed by the end user.

## Getting Started

Before you begin using FlightLimits you will need [git](https://git-scm.com/download/) and [python](https://www.python.org/downloads/) installed on your machine.

You should also familiarize yourself with how we retrieve flight data using the [Duffel API](https://duffel.com/docs/guides/getting-started-with-flights).

`gh repo clone Stepheng753/FlightLimits` # Clone this repo, you may also download [by clicking here](https://github.com/Stepheng753/FlightLimits/archive/refs/heads/main.zip)

## Running BackEnd

To run the FlightLimits BackEnd, execute the following commands in your terminal:

`cd FlightLimits/BackEnd` # Navigate into the FlightLimits BackEnd project directory

`source venv/bin/activate` # Activate the virtual environment

`pip install flask` # Install Flask on First Run

`./app.py` # Turn the BackEnd server on

## Running Front End

To run the FlightLimits FrontEnd, execute the following commands in your terminal:

`cd FlightLimits/FrontEnd` # Navigate into the FlightLimits FrontEnd project directory

`npm install` # Install all dependencies

`./run.sh` or `npm run dev` # Run the FrontEnd Server

`"Click Here for Payment Portal"` # Redirect to Payment Portal

`"run.py"` # Calls /api/run function, returns the PaymentIntentClientToken, and renders the Payment Portal

## How to customize

Run.py contains several parameters that affect which flight tickets we monitor, and how we monitor them for you

You can choose between the following customizations:

-   **Origin**: Specify place of Origin
-   **Destination**: Specify place of Destination.
-   **Departure Date**: Specify Departure Date.
-   **Trip Type**: Opt for One Way or Round Trip.
-   **Return Date**: Specify Return Date for round trips.
-   **Passenger Age**: Input passenger age for targeted searches.
-   **Cabin Class**: Choose the cabin class (e.g., Economy, Business).

## Output

Currently, FlightLimits produces 2 different visualizations, text-based and plotted as shown below, with each timestamp representing a possible buy order at that

![CLT_SAN-12022023_04-55](https://github.com/Stepheng753/FlightLimits/assets/28160617/a4af424b-3a66-4ceb-9dd3-d15111871427)

Log file example

| Airline           | Flight | Status    | Date & Time         |
| ----------------- | ------ | --------- | ------------------- |
| American Airlines | AA118  | Departing | 2024-03-01 00:00:00 |
| American Airlines | AA118  | Arriving  | 2024-03-01 02:01:00 |
| American Airlines | AA118  | Departing | 2024-03-30 22:27:00 |
| American Airlines | AA118  | Arriving  | 2024-03-31 06:28:00 |

-   12/02/23 09:37:30 AM :: off_0000AcOY4cyW4v7zz88ye6 :: $328.79 USD
-   12/02/23 09:37:32 AM :: off_0000AcOY4tIFPKPyaxUxca :: $328.68 USD
-   12/02/23 09:37:36 AM :: off_0000AcOY5CpukNdbCsOcEe :: $345.48 USD
-   12/02/23 09:37:39 AM :: off_0000AcOY5WZR1cwfNCWHAq :: $336.33 USD
-   12/02/23 09:37:42 AM :: off_0000AcOY5miB0tRdQwjU1L :: $334.02 USD

## Book A Flight

To use this to book a flight and not just monitor... docs coming soon

## Premium Upgrades

Check for the customer more often
Tools with which you can select from, extra options

## To Do

-   Build a Front End Application - React, React Native
-   Upload Flight Data to Database
-   Host remote server to call API's at specific times
-   Exception Handling all around
