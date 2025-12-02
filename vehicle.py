def vehicleregistration_details(vehicleno,ownername,vechicetype,yearofmanufacture):
    result=(
        f"vehicle No:{no}\n"
        f"owner name:{name}\n"
        f"vehicle type:{type}\n"
        f"year of manufacture:{manufacture}"
    )
    return result
if __name__=="__main__":
    vehicle no="1234"
    ownwe name="riya"
    vehicle type="car"
    year of manufacture=2023
    print(vehicleregistration_details(no,name,type,manufacture))
