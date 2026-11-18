from tools import get_current_weather

result = get_current_weather.invoke({"location": "New York"})

print(result)