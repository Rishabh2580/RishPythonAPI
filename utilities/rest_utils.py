import requests


def get_weather_details():
    base_url = "https://samples.openweathermap.org"
    endpoint = "/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"

    response = requests.get(f"{base_url}{endpoint}", verify=False)

    assert response.status_code == 200

    return response.json()
