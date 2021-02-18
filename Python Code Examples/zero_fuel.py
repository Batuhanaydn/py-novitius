def zero_fuel(distance_to_pump,mgp,fuel_left):
    if (mgp * fuel_left) >= distance_to_pump:
        return True
    return False
print(zero_fuel(100, 50, 1))