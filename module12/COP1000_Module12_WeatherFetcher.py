# v6
"""
Module 12
Project: Weather Forecast Fetcher
Program: COP1000_Module12_WeatherFetcher.py
Author: Richard Anderson
"""
import requests
# from pprint import pprint

# requests time out after this number of seconds
TIMEOUT = 15

def input_str(message: str):
  while True:
    in_str = input(message).strip()
    if in_str == "":
      print("String must not be empty.")
    else:
      return in_str

# makes api request
def safe_get(url, params, timeout=TIMEOUT):
  try:
    response = requests.get(url, params=params, timeout=timeout)
  except requests.exceptions.RequestException as error:
    print(f"Error: RequestException: {str(error)}")
    return {"status": {"network_ok": False,
                       "network_false_reason": "request_exception",
                       "request_error": error}}
  if response.status_code != 200:
    print("Status code not 200.")
    return {"status": {"network_ok": False,
                       "network_false_reason": "status_code",
                       "status_code": response.status_code}}
  else:
    return {"status": {"network_ok": True},
            "response": response}

# makes api request
def get_location(city_name: str):
  url = "https://geocoding-api.open-meteo.com/v1/search"
  params = {
    "name": city_name,
    "count": 1,
    "language": "en",
    "format": "json"
  }
  result = safe_get(url, params)
  if result["status"]["network_ok"] == False:
    # print("Error in getting location.")
    return result
  response = result["response"]
  data = response.json()
  try:
    location = data["results"][0]
  except KeyError:
    print("No location results for that city.")
    return {"status": {"network_ok": True,
                       "results_nonempty": False}}
  return {"status": {"network_ok": True,
                     "results_nonempty": True},
          "location": location}

# makes api request
def get_weather(location: dict):
  latitude = location["latitude"]
  longitude = location["longitude"]
  url = "https://api.open-meteo.com/v1/forecast"
  params = {
    "latitude": latitude,
    "longitude": longitude,
    "current": "temperature_2m,wind_speed_10m",
    "temperature_unit": "fahrenheit",
    "wind_speed_unit": "mph"
  }
  result = safe_get(url, params)
  if result["status"]["network_ok"] == False:
    # print("Error in getting weather.")
    return result
  response = result["response"]
  data = response.json()
  weather = data
  return {"status": {"network_ok": True},
          "weather": weather}

def get_location_str(location: dict):
  delim = ", "
  location_str = ""
  try:
    location_str += f"{location["name"]}"
  except KeyError:
    print("No city name data.")
  if location_str != "":
    location_str += delim
  try:
    location_str += f"{location["admin1"]}"
  except:
    print("No state data.")
  return location_str

def get_weather_str(weather: dict):
  delim = "\n"
  temp_key = "temperature_2m"
  wind_speed_key = "wind_speed_10m"
  weather_str = ""
  try:
    weather_str += f"Temperature {weather["current"][temp_key]} {weather["current_units"][temp_key]}"
  except KeyError:
    print("No temperature data.")
  if weather_str != "":
    weather_str += delim
  try:
    weather_str += f"Wind Speed {weather["current"][wind_speed_key]} {weather["current_units"][wind_speed_key]}"
  except KeyError:
    print("No wind speed data.")
  return weather_str

def y_n_choice(message: str):
    choice = input(f"{message}? [y/n]: ").strip()
    if choice.casefold() == "y":
      return True
    else:
      return False

# makes api request
def api_ui(api_func, data_key, error_msg_in):
  result = api_func()
  return_dict = {}
  try:
    return_dict[data_key] = result[data_key]
  except KeyError:
    print(error_msg_in)
    error_msg_out = "Error Type: "
    if result["status"]["network_ok"] == False:
      error_msg_out += "network related"
      error_msg_out += "\nNetwork Error Type: "
      if result["status"]["network_false_reason"] == "status_code":
        error_msg_out += "status code: "
        error_msg_out += str(result["status"]["status_code"])
      elif result["status"]["network_false_reason"] == "request_exception":
        error_msg_out += "request exception: "
        error_msg_out += str(result["status"]["request_error"])
    else:
      error_msg_out += "Unknown"
    return_dict["ui_error"] = error_msg_out
  finally:
    return_dict["status"] = result["status"]
    return return_dict

# makes api request
def api_ui_loop(api_func, data_key, error_msg_in):
  while True:
    result = api_ui(api_func, data_key, error_msg_in)
    if "ui_error" in result:
      if "results_nonempty" in result["status"]:
        if result["status"]["results_nonempty"] == False:
          result["ui_error"] = "Error Type: search results empty"
          print(result["ui_error"])
          return result
      print(result["ui_error"])
      if y_n_choice("try again") == False:
        return result
    else:
      return result

def main():
  print("Weather Forecast Fetcher\n")

  city = input_str("Enter a city: ")

  location_result = api_ui_loop(lambda: get_location(city), "location",
                                    "Error in getting location.")
  if "ui_error" in location_result:
    return
  else:
    location = location_result["location"]

  print(f"\nWeather for {get_location_str(location)}")

  weather_result = api_ui_loop(lambda: get_weather(location), "weather",
                                   "Error in getting weather.")
  if "ui_error" in weather_result:
    return
  else:
    weather = weather_result["weather"]

  print(f"\n{get_weather_str(weather)}")

def main_loop():
  while True:
    main()
    print("")
    if y_n_choice("run again") == False:
      return
    print("")

main_loop()