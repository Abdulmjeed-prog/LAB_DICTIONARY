weather = {
    "Riyadh": {
        "2026-02-24": {"temperature": 18.5, "humidity": 40, "condition": "sunny"},
        "2026-02-25": {"temperature": 20.0, "humidity": 35, "condition": "cloudy"}
    },
    "Jeddah": {
        "2026-02-24": {"temperature": 25.2, "humidity": 75, "condition": "rainy"}
    }
}

def add_weather(weather):
    city = input("City: ")
    date = input("Date (YYYY-MM-DD): ")
    temp = float(input("Temp: "))
    hum = int(input("Humidity: "))
    cond = input("Condition: ")
    
    if city not in weather:
        weather[city] = {}
    weather[city][date] = {"temperature": temp, "humidity": hum, "condition": cond}
    print("Added!")

def query_city(weather):
    city = input("Enter city name: ").title()
    
    if city not in weather:
        print("No data for this city.")
        return
    
    print(f"\nWeather for {city}:")
    for date, data in weather[city].items():
        print(f"  {date}: {data['temperature']}°C, {data['humidity']}%, {data['condition']}")

def update_weather(weather, city, date, new_data):
    """Update specific weather data for a city/date."""
    if city in weather and date in weather[city]:
        weather[city][date].update(new_data)
        print(f"Updated {city} on {date}: {new_data}")
    else:
        print(f"City '{city}' or date '{date}' not found.")

def delete_weather(weather, city, date):
    if city in weather and date in weather[city]:
        del weather[city][date]
        print(f"✅ Deleted {city} on {date}")
        if not weather[city]:  # Clean empty city
            del weather[city]
    else:
        print(f"City '{city}' or date '{date}' not found.")


pick = None

while pick != 5:
    print("1- add new City")
    print("2- check city weather by city name") 
    print("3- Update")
    print("4- Deleate")
    print("5- Exit")
    pick = int(input("Select one of the options: "))
    
    if pick == 1:
        add_weather(weather)
    elif pick == 2:
        query_city(weather)
    elif pick == 3:
        city = input("City: ").strip()
        date = input("Date (YYYY-MM-DD): ").strip()
        temp = int(input("New temp: "))
        hum = int(input("New humidity: "))
        new_data = {"temperature": temp, "humidity": hum}  
        update_weather(weather, city, date, new_data)   
    elif pick == 4:
        city = input("City: ").strip().title()
        date = input("Date (YYYY-MM-DD): ").strip()
        delete_weather(weather, city, date)
    else:
        print("invalid")

print(weather)
