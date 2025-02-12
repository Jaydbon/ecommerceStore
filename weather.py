import requests
from datetime import datetime, timezone

def get_weather_forecast():
    # API KEY
    api_key = "API_KEY"
    city = "Toronto"
    # OpenWeatherMap API endpoint for 5-day weather forecast (every 3 hours)
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&cnt=40&appid={api_key}&units=metric"

    # Make a request to the API
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        days = []
        dates = []
        # Loop through the forecast data for each day
        for day in data["list"]:
            weather = day['weather'][0]["main"]
            date = datetime.fromtimestamp(day["dt"]).strftime('%A')
            temp = int(day["main"]["temp"])
            if date not in dates:
                dates.append(date)
                days.append([temp, weather, date])
        
        return days
    
    else:
        print(f"Failed to fetch weather data: {response.status_code}, {response.text}")


# Call the function to get the weather forecast
# print(get_weather_forecast())



# Day gives
# Temperature FeelsLike MinTemp MaxTemp Pressure SeaLvL GroundLvL Humidity temp_kf