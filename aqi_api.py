import requests
API_KEY="ac7beedeef2237b9d57379e02ec4ec8a"

def get_aqi(city):
    geo_url=f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={API_KEY}"
    geo=requests.get(geo_url).json()
    if not geo:
        return{"error":"City not Found"}
    lat=geo[0]["lat"]
    lon=geo[0]["lon"]
    url=f"https://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&aooid={API_KEY}"
    data=requests.get(url).json
    aqi=data["list"][0]["main"]["aqi"]
    level=["GOOD","Fair","Moderate","Poor","Very Poor"]
    return{
        "aqi":aqi,
        "category":level[aqi-1]
    }
