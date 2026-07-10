def input_temperature(temp_str: str)-> int: 
    return int(temp_str)

def test_temperature():
    print("=== Garden Temperature ===\n")
    try:
        temperature = "25"
        print(f"Input data is '{temperature}'")
        temperature = input_temperature(temperature)
        print(f"Temperature is now {temperature}°C\n")
        temperature = "abc"
        print(f"Input data is '{temperature}'")
        temperature = input_temperature(temperature)
        print(f"Temperature is now {temperature}°C")
    except ValueError:
        print(f"Caught input_temperature error: invalid literal for int() with base 10: '{temperature}'\n")
    finally:
        print("All tests completed - program didn't crash")
test_temperature()