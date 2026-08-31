import time
import requests


class WeatherTracker:

    def __init__(self, api_key="demo"):
        self.api_key = api_key
        self.history = []

    def fetch_weather(self, city):
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units=metric"
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                data = response.json()
                result = {
                    "city": city,
                    "temp": data["main"]["temp"],
                    "weather": data["weather"][0]["description"],
                    "timestamp": time.strftime("%H:%M:%S"),
                }
                self.history.append(result)
                return result
            return {"error": f"City not found (Status {response.status_code})"}
        except requests.RequestException as e:
            return {"error": str(e)}

    def show_history(self):
        print("\n--- Search History ---")
        for item in self.history:
            print(
                f"[{item['timestamp']}] {item['city']}: {item['temp']}°C, {item['weather']}"
            )


tracker = WeatherTracker()
print(tracker.fetch_weather("London"))
print(tracker.fetch_weather("Tokyo"))
tracker.show_history()