
import requests
from datetime import datetime

API_ID = "14d8b66f"
API_KEY = "b1251eb185011ebd42e2584b625b9acd"
SHEETY_USERNAME = "Ian"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/b734b032125a0156568e9b08b7e6a3fb/workoutTracking/workouts"

workout_details = input("Tell me about your workout: ")

headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY
}

exercise_content = {
    "query": workout_details,
    "gender": "male",
    "weight_kg": 74.0,
    "height_cm": 165.0,
    "age": 20
}

print(workout_details)

today = datetime.now()
curr_date = today.strftime("%d/%m/%Y")
curr_time = today.strftime("%H:%M:%S")

sheety_header = {
    "Authorization": "Basic SWFuOkdvYUtvY2hpMTIz"
}


response = requests.post(url=exercise_endpoint, json=exercise_content, headers=headers)
print(response.json())
n = len(response.json()["exercises"])
for exercise in response.json()["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": curr_date,
            "time": curr_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheety_response = requests.post(url=sheety_endpoint, json=sheet_inputs, headers=sheety_header)
    print(sheety_response.text)