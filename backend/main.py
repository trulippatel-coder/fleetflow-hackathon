# FleetFlow - Basic Fleet Management System
from datetime import datetime

vehicles = []
drivers = []
trips = []

def add_vehicle(name, capacity):
    for vehicle in vehicles:
        if vehicle["name"] == name:
            print("Vehicle already exists!")
            return
    
    vehicle = {
        "name": name,
        "capacity": capacity,
        "status": "Available"
    }
    vehicles.append(vehicle)
    print(f"Vehicle {name} added successfully!")

def add_driver(name, license_expiry):
    for driver in drivers:
        if driver["name"] == name:
            print("Driver already exists!")
            return
    
    driver = {
        "name": name,
        "status": "Available",
        "license_expiry": license_expiry
    }
    
    drivers.append(driver)
    print(f"Driver {name} added successfully!")

def create_trip(vehicle_name, driver_name, cargo_weight):
    vehicle = None
    driver = None
    
    for v in vehicles:
        if v["name"] == vehicle_name:
            vehicle = v
            break
    
    for d in drivers:
        if d["name"] == driver_name:
            driver = d
            break
    
    if vehicle is None:
        print("Vehicle not found!")
        return
    
    if driver is None:
        print("Driver not found!")
        return
    
    if vehicle["status"] != "Available":
        print("Vehicle is not available!")
        return
    
    if driver["status"] != "Available":
        print("Driver is not available!")
        return
    # Check license expiry
    expiry_date = datetime.strptime(driver["license_expiry"], "%Y-%m-%d")
    today = datetime.today()

    if expiry_date < today:
       print("Driver license expired! Cannot assign trip.")
       return
    
    if cargo_weight > vehicle["capacity"]:
        print("Error: Cargo exceeds vehicle capacity!")
        return
    
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
def menu():
    while True:
        print("\n--- FleetFlow Menu ---")
        print("1. Add Vehicle")
        print("2. Add Driver")
        print("3. Create Trip")
        print("4. Complete Trip")
        print("5. Add Maintenance")
        print("6. Show Dashboard")
        print("7. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            name = input("Enter vehicle name: ")
            capacity = int(input("Enter capacity: "))
            add_vehicle(name, capacity)
        
        elif choice == "2":
            name = input("Enter driver name: ")
            expiry = input("Enter license expiry date (YYYY-MM-DD): ")
            add_driver(name, expiry)
        
        elif choice == "3":
            vehicle = input("Enter vehicle name: ")
            driver = input("Enter driver name: ")
            cargo = int(input("Enter cargo weight: "))
            create_trip(vehicle, driver, cargo)
        
        elif choice == "4":
            vehicle = input("Enter vehicle name: ")
            complete_trip(vehicle)
        
        elif choice == "5":
            vehicle = input("Enter vehicle name: ")
            issue = input("Enter maintenance issue: ")
            add_maintenance(vehicle, issue)
        
        elif choice == "6":
            show_dashboard()
        
        elif choice == "7":
            print("Exiting FleetFlow...")
            break
        
        else:
            print("Invalid choice!")

# Start the system
menu()