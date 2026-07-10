class TempError(Exception):
    pass

def input_temperature(temp_str: str)-> int: 
    temp = int(temp_str)
    if temp < 0:
        raise TempError(f"Caught input_temperature error: {temp}°C is too cold for plants (min 0°C)")
    elif temp > 40:
        raise TempError(f"Caught input_temperature error: {temp}°C is too hot for plants (max 40°C)")
    else:
        return temp

def test_temperature():
    datos = ["40", "abc", "100", "-50"]
    for dato in datos:
        try:
            temperature = dato
            print(f"Input data is '{temperature}'")
            temperature = input_temperature(temperature)
            print(f"Temperature is now {temperature}°C\n")
        except ValueError:
            print(f"Caught input_temperature error: invalid literal for int() with base 10: '{temperature}'\n")
        except TempError as e:
            print(f"{e}\n")

    print("All tests completed - program didn't crash")


print("=== Garden Temperature ===\n")
test_temperature()