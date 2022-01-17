def gas_stations(distance, tank_size, stations):
    points = [0]
    for station in stations:
        if station < distance:
            points.append(station)
    points.append(distance)
    distance_remaining = distance
    tank_remaining = tank_size
    gas_stations_shortest_list = []
    index = 0
    while index < len(points) - 1:
        distance_to_next_point = points[index + 1] - points[index]
        if distance_to_next_point >= tank_size:
            return []
        if distance_to_next_point < tank_remaining:
            tank_remaining -= distance_to_next_point
            distance_remaining -= distance_to_next_point
        else:
            gas_stations_shortest_list.append(points[index])
            tank_remaining = tank_size
            index -= 1
        index += 1
    return gas_stations_shortest_list


print(gas_stations(320, 90, [50, 80, 140, 180, 220, 290]))
print(gas_stations(390, 80, [70, 90, 140, 210, 240, 280, 350]))
print(gas_stations(100, 50, [10, 20, 30, 40, 50, 60, 70, 80, 90, 150]))
print(gas_stations(100, 50, [10, 90]))
