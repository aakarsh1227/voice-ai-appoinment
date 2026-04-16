import requests
import os

CAL_API_KEY = os.getenv("CAL_API_KEY")

def check_availability(date):
    # Call Cal.com API to see if slots exist
    response = requests.get(f"https://api.cal.com/v1/slots?apiKey={CAL_API_KEY}&dateFrom={date}")
    return response.json()

def create_booking(name, email, start_time, event_type_id):
    # Finalize the booking
    data = {
        "responses": {"name": name, "email": email},
        "start": start_time,
        "eventTypeId": event_type_id
    }
    response = requests.post(f"https://api.cal.com/v1/bookings?apiKey={CAL_API_KEY}", json=data)
    return response.json()