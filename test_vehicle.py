from vehicle import vehicle_registration

def test_vehicle_registration():
    expected_output=(
      Vehicle number="1234"
   Vehicle owner name="riya"
    Vehicle type="car"
    Year of manifacture=2023
    )
    assert vehicle_registration("1234","riya","car",2023)==expected_output
