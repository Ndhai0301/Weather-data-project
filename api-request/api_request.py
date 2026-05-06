import requests
url = '09ac46a08e452dcdbc800ba18ebc0461'
api_url = f"https://api.weatherstack.com/current?access_key={url}&query=New York"

def fetch_data():
    print("Fetching weather data from Weatherstack API...")
    try:
    
        response = requests.get(api_url)
        response.raise_for_status()
        print("API response received successfully")
        print(response.json())
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error eccourred: {e}")
        raise

def mock_fetch_data():
    return {'request': {'type': 'City', 'query': 'New York, United States of America', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'New York', 'country': 'United States of America', 'region': 'New York', 'lat': '40.714', 'lon': '-74.006', 'timezone_id': 'America/New_York', 'localtime': '2026-05-03 09:50', 'localtime_epoch': 1777801800, 'utc_offset': '-4.0'}, 'current': {'observation_time': '01:50 PM', 'temperature': 8, 'weather_code': 116, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0002_sunny_intervals.png'], 'weather_descriptions': ['Partly cloudy'], 'astro': {'sunrise': '05:52 AM', 'sunset': '07:55 PM', 'moonrise': '10:22 PM', 'moonset': '06:28 AM', 'moon_phase': 'Waning Gibbous', 'moon_illumination': 98}, 'air_quality': {'co': '156.85', 'no2': '4.75', 'o3': '94', 'so2': '2.55', 'pm2_5': '7.05', 'pm10': '8.05', 'us-epa-index': '1', 'gb-defra-index': '1'}, 'wind_speed': 23, 'wind_degree': 315, 'wind_dir': 'NW', 'pressure': 1013, 'precip': 0, 'humidity': 49, 'cloudcover': 75, 'feelslike': 4, 'uv_index': 2, 'visibility': 16, 'is_day': 'yes'}}

    