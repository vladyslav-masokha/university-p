import requests
import pandas as pd
from sklearn.linear_model import LogisticRegression

def get_location_key(api_key, city):
    base_url = 'http://dataservice.accuweather.com/locations/v1/cities/search'
    params = {'apikey': api_key, 'q': city}
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data:
            return data[0]['Key']
        else:
            return None
    else:
        return None

def get_weather(api_key, location_key, days=5):
    base_url = f"http://dataservice.accuweather.com/forecasts/v1/daily/{days}day/{location_key}"
    params = {'apikey': api_key}
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

api_key = 'A6mcAHymBugcNaznLG6h3SAnG93pOyJg'
city = 'Kyiv'

location_key = get_location_key(api_key, city)
if location_key:
    print('Location key:', location_key)
else:
    print('Помилка при отримані location key.')

weather_data = get_weather(api_key, location_key, days=5)
if weather_data:
    # print('Weather data:', weather_data)
    print('Дані завантажено успішно.')
else:
    print('Помилка при отримані даних.')

df = pd.DataFrame(weather_data['DailyForecasts'])

df['temperature'] = [25] * len(df)
df['humidity'] = [60] * len(df)
df['wind_speed'] = [15] * len(df)

df['target_weather'] = ['Sunny', 'Rain', 'Cloudy', 'Mostly cloudy', 'Mostly cloudy']

model = LogisticRegression()
model.fit(df[['temperature', 'humidity', 'wind_speed']], df['target_weather'])

predicted_weather = model.predict([[25, 60, 15]])
print('Прогнозована погода на наступний день:', predicted_weather[0])
