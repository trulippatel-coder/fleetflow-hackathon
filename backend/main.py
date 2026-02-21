# FleetFlow - Basic Fleet Management System

vehicles = []
drivers = []
trips = []

def add_vehicle(name, capacity):
    vehicle = {
        "name": name,
        "capacity": capacity,
        "status": "Available"
    }
    vehicles.append(vehicle)
    print(f"Vehicle {name} added successfully!")

def add_driver(name):
    driver = {
        "name": name,
        "status": "Available"
    }
    drivers.append(driver)
    print(f"Driver {name} added successfully!")

def create_trip(vehicle_name, driver_name, cargo_weight):
    for vehicle in vehicles:
        if vehicle["name"] == vehicle_name and vehicle["status"] == "Available":
            if cargo_weight > vehicle["capacity"]:
                print("Error: Cargo exceeds vehicle capacity!")
                return
            
            for driver in drivers:
                if driver["name"] == driver_name and driver["status"] == "Available":
                    vehicle["status"] = "On Trip"
                    driver["status"] = "On Trip"
                    
                    trip = {
                        "vehicle": vehicle_name,
                        "driver": driver_name,
                        "cargo": cargo_weight,
                        "status": "Active"
                    }
                    trips.append(trip)
                    
                    print("Trip created successfully!")
                    return
    
    print("Error: Vehicle or Driver not available!")
def complete_trip(vehicle_name):
     for trip in trips:
        if trip["vehicle"] == vehicle_name and trip["status"] == "Active":
            trip["status"] = "Completed"
            
            # Update vehicle and driver status back to Available
            for vehicle in vehicles:
                if vehicle["name"] == vehicle_name:
                    vehicle["status"] = "Available"
            
            for driver in drivers:
                if driver["name"] == trip["driver"]:
                    driver["status"] = "Available"
            
            print("Trip completed successfully!")
            return
    
        print("No active trip found for this vehicle.")
def add_maintenance(vehicle_name, issue):
    for vehicle in vehicles:
        if vehicle["name"] == vehicle_name:
            vehicle["status"] = "In Shop"
            
            maintenance = {
                "vehicle": vehicle_name,
                "issue": issue,
                "status": "Under Maintenance"
            }
            
            print(f"Vehicle {vehicle_name} is now under maintenance for: {issue}")
            return
    
    print("Vehicle not found")
def show_dashboard():
    total_vehicles = len(vehicles)
    available = 0
    on_trip = 0
    in_shop = 0
    
    for vehicle in vehicles:
        if vehicle["status"] == "Available":
            available += 1
        elif vehicle["status"] == "On Trip":
            on_trip += 1
        elif vehicle["status"] == "In Shop":
            in_shop += 1
    
    total_trips = len(trips)
    
    print("\n--- FleetFlow Dashboard ---")
    print(f"Total Vehicles: {total_vehicles}")
    print(f"Available Vehicles: {available}")
    print(f"Vehicles On Trip: {on_trip}")
    print(f"Vehicles In Maintenance: {in_shop}")
    print(f"Total Trips: {total_trips}")

# Demo flow
add_vehicle("Truck-01", 500)
add_driver("Rahul")
create_trip("Truck-01", "Rahul", 400)
complete_trip("Truck-01")
add_maintenance("Truck-01", "Oil Change")
show_dashboard()
