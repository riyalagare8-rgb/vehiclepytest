

def vehicle_registration(number, name, vehicle_type, manufacture):
    result = (
        f"Vehicle number:{number}\n"
        f"vehicle owner name:{name}\n"
        f"vehicle type:{vehicle_type}\n"
        f"year of manufacture:{manufacture}"
    )
    return result

if _name_ == "_main_":
    number = "KA31N2881"
    name = "riya"
    vehicle_type = "car"
    manufacture = 2023
    print(vehicle_registration(number, name, vehicle_type,manufacture))
