import requests

# Function to fetch weather data
def get_weather(city):
    api_key = "your_api_key_here"  # Replace with your OpenWeatherMap API key
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}
    
    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        
        if response.status_code == 200:
            weather = data["weather"][0]["description"].capitalize()
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            
            print(f"Weather in {city}: {weather}")
            print(f"Temperature: {temp}°C")
            print(f"Humidity: {humidity}%")
        else:
            print(f"Error: {data['message'].capitalize()}")
    except requests.exceptions.RequestException as e:
        print("Error fetching data. Please check your internet connection.")

# Main program
if __name__ == "__main__":
    print("Welcome to the Weather App!")
    city = input("Enter the city name: ").strip()
    if city:
        get_weather(city)
    else:
        print("City name cannot be empty.")
