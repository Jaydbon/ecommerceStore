import requests
from datetime import datetime, timezone

def get_weather_forecast(city, api_key):
    # OpenWeatherMap API endpoint for 5-day weather forecast (every 3 hours)
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&cnt=5&appid={api_key}&units=metric"

    # Make a request to the API
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(f"5-Day Weather Forecast for {city.capitalize()}:\n")

        # Loop through the forecast data for each day
        for day in data["list"]:
            # Extract timestamp and convert to readable date
            timestamp = day["dt"]
            date = datetime.fromtimestamp(timestamp, timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
            temp = day["main"]["temp"]
            weather = day["weather"][0]["description"]
            
            print(f"{date}: {temp}°C, {weather.capitalize()}")
    else:
        print(f"Failed to fetch weather data: {response.status_code}, {response.text}")

# Replace with your OpenWeatherMap API key
API_KEY = "839f5f168106cb210a47885408533897"

# Replace with the city of your choice
city = "London"

# Call the function to get the weather forecast
get_weather_forecast(city, API_KEY)