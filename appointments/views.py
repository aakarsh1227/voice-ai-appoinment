from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import requests
import os

@csrf_exempt
def vapi_webhook(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        
        # Vapi sends a 'tool_call' when it needs to book something
        message = data.get('message', {})
        if message.get('type') == 'tool-call':
            tool_calls = message.get('toolCalls', [])
            
            for call in tool_calls:
                if call['function']['name'] == 'book_appointment':
                    args = call['function']['arguments']
                    
                    # Logic to call Cal.com (Requirement R6)
                    api_key = os.getenv("CAL_API_KEY")
                    payload = {
                        "start": args['datetime'],
                        "eventTypeId": 123456, # Replace with your Cal.com ID
                        "responses": {
                            "name": args['name'],
                            "email": args['email']
                        }
                    }
                    
                    response = requests.post(
                        f"https://api.cal.com/v1/bookings?apiKey={api_key}",
                        json=payload
                    )
                    
                    if response.status_code == 201:
                        return JsonResponse({"result": "Appointment confirmed! Invite sent."})
                    else:
                        return JsonResponse({"result": "Slot unavailable. Ask for another time."}, status=400)

    return JsonResponse({"status": "ok"})