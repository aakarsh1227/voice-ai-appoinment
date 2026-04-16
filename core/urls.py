from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
import os

# Define the HTML directly in the view to test if it's a path issue
def home(request):
    html_content = """
    <!DOCTYPE html>
    <html>
    <head><title>Voice Clinic</title></head>
    <body style="display:flex; justify-content:center; align-items:center; height:100vh; font-family:sans-serif;">
        <div style="text-align:center;">
            <h1>Clinic Voice Assistant</h1>
            <button id="callBtn" style="padding:20px; font-size:20px; background:#1a73e8; color:white; border:none; border-radius:10px; cursor:pointer;">
                Start Voice Booking
            </button>
        </div>
        <script src="https://cdn.jsdelivr.net/gh/vapi-ai/web-sdk@latest/dist/vapi-sdk.js"></script>
        <script>
            const vapi = new Vapi('608a8199-5983-4b0d-bea7-5d86465baab3');
            document.getElementById('callBtn').onclick = () => {
                vapi.start('6b5356e0-d38c-4c85-b7b9-d224f8c760cc');
                document.getElementById('callBtn').innerText = "Connecting...";
            };
        </script>
    </body>
    </html>
    """
    return HttpResponse(html_content)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    # Add your webhook path here too
]