import pytest

from utilities.rest_utils import get_weather_details


@pytest.mark.priority(1)
def test_validate_weather_id_500_and_description():
    response = get_weather_details()

    expected_details = {
        "id": "500",
        "description": "light rain"
    }

    weather_id = response["list"][92]["weather"][0]["id"]
    weather_description = response["list"][92]["weather"][0]["description"]

    assert str(weather_id) == expected_details["id"]
    print(f"Weather Id: {weather_id}")
    assert weather_description == expected_details["description"]
    print(f"Weather Description: {weather_description}")


@pytest.mark.priority(2)
def test_validate_weather_id_800_and_description():
    response = get_weather_details()

    expected_details = {
        "id": "800",
        "description": "clear sky"
    }

    weather_id = response["list"][4]["weather"][0]["id"]
    weather_description = response["list"][4]["weather"][0]["description"]

    assert str(weather_id) == expected_details["id"]
    print(f"Weather Id: {weather_id}")
    assert weather_description == expected_details["description"]
    print(f"Weather Description: {weather_description}")


@pytest.mark.priority(3)
def test_forecast_in_hourly_interval():
    response = get_weather_details()

    timestamps = [item["dt"] for item in response["list"]]
    print(timestamps)

    expected_timestamp = timestamps[0]
    for timestamp in timestamps:
        assert expected_timestamp == timestamp
        expected_timestamp += 3600


@pytest.mark.priority(4)
def test_response_contains_4_days_of_data():
    response = get_weather_details()

    number_of_data_points = len(response["list"])
    assert number_of_data_points == 4 * 24  # Assuming hourly data
    print(f"Number of Data Points: {number_of_data_points}")


@pytest.mark.priority(5)
def test_temperature_range():
    response = get_weather_details()

    temperatures = [item["main"]["temp"] for item in response["list"]]
    temp_min = [item["main"]["temp_min"] for item in response["list"]]
    temp_max = [item["main"]["temp_max"] for item in response["list"]]

    for temp, min_temp, max_temp in zip(temperatures, temp_min, temp_max):
        assert min_temp <= temp <= max_temp

        print(f"Temp: {temp}")
        print(f"Min Temp: {min_temp}")
        print(f"Max Temp: {max_temp}")

        assert min_temp <= max_temp
