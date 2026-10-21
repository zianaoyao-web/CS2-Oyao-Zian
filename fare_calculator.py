# Travel Fare Calculator
FARE_RATE = 14

# Rule 1
name = input("Enter passenger name: ").strip()
while not name:
    print("Passenger name cannot be empty.")
    name = input("Enter passenger name: ").strip()

# Rule 2
while True:
    try:
        distance = float(input("Enter distance (km): "))
        if distance > 0:
            break
        print("Distance must be a number greater than 0.")
    except ValueError:
        print("Enter a valid number for distance.")

# Rule 3
while True:
    try:
        passengers = int(input("Enter number of passengers: "))
        if passengers > 0:
            break
        print("Number of passengers must be a positive whole number greater than 0.")
    except ValueError:
        print("Enter a valid integer for the number of passengers.")

total_fare = distance * FARE_RATE * passengers

print("\nPassenger:", name)
print("Total Fare: PHP", round(total_fare, 2))
