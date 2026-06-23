import requests

def get_weather(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        name        = data["name"]
        temp        = data["main"]["temp"]
        condition   = data["weather"][0]["description"].title()
        humidity    = data["main"]["humidity"]
        wind_speed  = data["wind"]["speed"] * 3.6  # convert m/s to km/h

        print("\n-----------------------------")
        print(f"  Weather in {name}")
        print("-----------------------------")
        print(f"  Temperature : {temp:.1f}°C")
        print(f"  Condition   : {condition}")
        print(f"  Humidity    : {humidity}%")
        print(f"  Wind Speed  : {wind_speed:.1f} km/h")
        print("-----------------------------\n")
    else:
        print(f"\n❌ City not found. Please check the spelling and try again.\n")

def main():
    print("=== Weather Dashboard CLI ===")
    api_key = "af019697e6c29609cb015abc99b0317a"   

    while True:
        city = input("Enter city (or 'quit' to exit): ").strip()
        if city.lower() == "quit":
            print("Goodbye!")
            break
        elif city == "":
            print("Please enter a city name.")
        else:
            get_weather(city, api_key)

if __name__ == "__main__":
    main()