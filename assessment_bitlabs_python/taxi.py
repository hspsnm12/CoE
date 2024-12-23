def fare(distances):
    base_fare = 50
    distance_fare = 10
    total_fare = 0
    trip_fares = []
    for i, distance in enumerate(distances, start=1):
        fare = base_fare + distance * distance_fare
        trip_fares.append(f"Trip {i}: ${fare}")
        total_fare += fare
    trip_fares.append(f"Total Fare: ${total_fare}")
    return trip_fares

trips = [5, 10, 3]
result = fare(trips)

for line in result:
    print(line)
