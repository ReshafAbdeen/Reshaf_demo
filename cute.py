import requests

city = "London"
url = f"https://wttr.in/{city}?format=j1"
response = requests.get(url).json()

current = response["current_condition"][0]
temp = current["temp_C"]
weather_desc = current["weatherDesc"][0]["value"]

print(f"--- Weather in {city} ---")
print(f"Temperature: {temp}°C | Condition: {weather_desc}")