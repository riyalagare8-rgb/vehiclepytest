from vehicle import vehicle_registration

def test_vehicle_registration():
    expected_output = (
        "Vehicle number:KA31N2881\n"
        "vehicle owner name:riya\n"
        "vehicle type:car\n"
        "year of manufacture:2023"
    )

    assert vehicle_registration("KA31N2881", "riya", "car", 2023) == expected_output
