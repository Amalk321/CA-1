Overview
The Charging Station Manager is a Python class designed to manage, track, and analyze electric vehicle (EV) charging sessions from a dataset. It allows for adding new charging sessions, and provides the ability to compute the total energy consumption for all vehicles in the dataset.

Features
Load Dataset: Loads a CSV file containing EV charging session data.
Add Charging Session: Easily add new charging sessions, including details such as Vehicle ID, Session ID, energy consumed, duration, and cost.
Total Energy Consumption: Compute the total energy consumption for each vehicle across all recorded sessions.
Dataset Structure
The dataset used should have the following columns:

VehicleID: Unique identifier for each vehicle.
SessionID: Unique identifier for each charging session.
Energy_consume: Amount of energy consumed during the charging session (in kWh).
Charging_Duration: Duration of the charging session (in hours).
Cost: Cost of the charging session.
Usage
Loading the Dataset: The CSV file containing the charging data is loaded when initializing the ChargingStationManager class.
Adding New Sessions: Add new sessions dynamically to track ongoing charging activities.
Energy Consumption Analysis: Get a summary of total energy consumed for all vehicles, grouped by their Vehicle ID.
Example Use Case
Manage Charging Sessions: Useful for managing and analyzing data at EV charging stations.
Energy Consumption Reports: Provides insights on energy usage patterns for each vehicle over time.
