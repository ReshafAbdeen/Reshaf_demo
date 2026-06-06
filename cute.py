import urllib.request
import json

def get_weather(city):
    url = f"https://wttr.in/{city}?format=j1"
    
    try:
        print(f"Fetching weather for {city}...")
        request = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        
        with urllib.request.urlopen(request) as response:
            data = json.loads(response.read().decode())
            
            current = data['current_condition'][0]
            temp_c = current['temp_C']
            weather_desc = current['weatherDesc'][0]['value']
            humidity = current['humidity']
            
            print(f"\nWeather in {city.capitalize()}:")
            print(f"Condition: {weather_desc}")
            print(f"Temperature: {temp_c}°C")
            print(f"Humidity: {humidity}%")
            
    except Exception as e:
        print(f"Error fetching weather data: {e}")

if __name__ == "__main__":
    target_city = input("Enter a city name: ").strip()
    if target_city:
        get_weather(target_city)
    else:
        print("City name cannot be empty.")