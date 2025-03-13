import json
import requests
import boto3

# Initialize DynamoDB
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table("UserPreferences")

def lambda_handler(event, context):
    # Extract city from request
    city = event.get("queryStringParameters", {}).get("city", "New York")
    user_id = "user123"  # You can modify this to be dynamic
    
    # Store user preference in DynamoDB
    table.put_item(Item={"userId": user_id, "preferredCity": city})
    
    # Fetch weather data from OpenWeather API
    api_key = "<api-key>"
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    response = requests.get(weather_url)
    data = response.json()
    
    # Extract relevant weather details
    weather_info = {
        "location": data["name"],
        "temperature": f"{data['main']['temp']}°C",
        "weather": data["weather"][0]["description"],
        "humidity": f"{data['main']['humidity']}%",
        "wind_speed": f"{data['wind']['speed']} km/h"
    }
    
    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps(weather_info)
    }
