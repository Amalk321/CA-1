import pandas as pd

file_path = 'C:/Users/HP/Downloads/CA-1/ev_charging.csv'  # Path to the uploaded file


class ChargingStationManager:
    def __init__(self, file_path):
        # Load the dataset from a CSV file
        self.ev_charging = pd.read_csv(file_path)

    # Method to add a new charging session to the dataset
    def add_charging_session(self, vehicleid, sessionid, energy_consumed, charging_duration, cost):
        new_session = pd.DataFrame({
            'VehicleID': [vehicleid],
            'SessionID': [sessionid],
            'Energy_consume': [energy_consumed],
            'Charging_Duration': [charging_duration],
            'Cost': [cost]
        })
        self.ev_charging = pd.concat([self.ev_charging, new_session], ignore_index=True)

    # Method to compute total energy consumption for all vehicles
    def compute_total_energy_all_vehicles(self):
        # Group by VehicleID and sum the energy consumed
        total_energy_per_vehicle = self.ev_charging.groupby('VehicleID')['Energy_consume'].sum()
        return total_energy_per_vehicle



# Compute total energy consumption for all vehicles
manager = ChargingStationManager(file_path)
total_energy_all_vehicles = manager.compute_total_energy_all_vehicles()
print("Total energy consumed by all vehicles:")
print(total_energy_all_vehicles)