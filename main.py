import requests
import datetime

APP_ID = 'ca5e9125'
APP_KEY = '30d1c5f06b0443a57ecd62ea283562c5'
TOKEN = 'jihjo8ffh98hwuih98hkjnerf83'
nutritionix_post_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
sheety_post_endpoint = 'https://api.sheety.co/c13c53be19243560e8c6686373748f97/workoutTracking/workouts'

user_exercise = input("What exercise did you do today? ")

headers = {
    'x-app-id': APP_ID,
    'x-app-key': APP_KEY
}

post_request = {
 "query": user_exercise,
 "gender": "male",
 "weight_kg": "79",
 "height_cm": "185",
 "age": "30"
}

nutix_response = requests.post(url=nutritionix_post_endpoint, json=post_request, headers=headers)
workout_data = nutix_response.json()

today = datetime.datetime.now()

for exercise in workout_data['exercises']:
    sheety_post_body = {
        'workout':
            {'date': today.strftime('%d/%m/%Y'),
             'time': today.strftime('%H:%M:%S'),
             'exercise': exercise['name'].title(),
             'duration': exercise['duration_min'],
             'calories': exercise['nf_calories']
             }
        }

    sheety_header = {
        'Authorization': 'Bearer jihjo8ffh98hwuih98hkjnerf83'
    }
    sheety_request = requests.post(url=sheety_post_endpoint, json=sheety_post_body, headers=sheety_header)
    print(sheety_request.json())


