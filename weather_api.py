import requests

def get_coordinates(city_name):

    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {
        "name":city_name,
        "language":"ru",
        "format":"json"
    }
    try:

        response_geocoding = requests.get(url, params=params, timeout=5)
        result_data = response_geocoding.json()

        if "results" in result_data and len(result_data["results"]) > 0:
            city_data = result_data["results"][0]

            filtered_data = {
                "name":city_data.get("name"),
                "admin1":city_data.get("admin1"),
                "country_code": city_data.get("country_code"),
                "latitude":city_data.get("latitude"),
                "longitude":city_data.get("longitude")
            }

            return filtered_data

        else:
            print("City not found during geocoding")
            return None

    except requests.exceptions.RequestException:
        print("Error")
        return  None


print(get_coordinates("Краснояк"))





