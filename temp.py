import requests

def temperature_detector():
    api_key = "315a6e08d1ac589ddb566d0cbb06589d"
    city = "welkite"

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    data = response.json()

    # Check if request was successful
    if response.status_code != 200:
        print("Error from API:", data.get("message", "Unknown error"))
        return

    temperature = data["main"]["temp"]

    print(f"Current Temperature in {city}: {temperature}°C")

    if temperature < 0:
        print("❄️ FREEZING! Wear heavy winter clothes!")
    elif temperature < 10:
        print("🧥 COLD! Wear a jacket!")
    elif temperature < 20:
        print("😊 COOL! Perfect for a light sweater!")
    elif temperature < 30:
        print("🌤 WARM! Nice weather!")
    elif temperature < 35:
        print("☀️ HOT! Stay hydrated!")
    else:
        print("🔥 VERY HOT! Stay indoors with AC!")

temperature_detector()