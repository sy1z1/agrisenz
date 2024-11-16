from celery import shared_task
import requests
from .models import NPKSensor

@shared_task
def fetch_and_store_sensor_data():
    try:
        urls = {
            "NITROGEN": "https://sgp1.blynk.cloud/external/api/get?token=KAg_k8iVJioh6oIh16TUvoZsVjcyVpRG&v6",
            "PHOSPHORUS": "https://sgp1.blynk.cloud/external/api/get?token=KAg_k8iVJioh6oIh16TUvoZsVjcyVpRG&v7",
            "POTASSIUM": "https://sgp1.blynk.cloud/external/api/get?token=KAg_k8iVJioh6oIh16TUvoZsVjcyVpRG&v8",
        }

        nitrogen = float(requests.get(urls["NITROGEN"]).text)
        phosphorus = float(requests.get(urls["PHOSPHORUS"]).text)
        potassium = float(requests.get(urls["POTASSIUM"]).text)

        # Save data to database
        NPKSensor.objects.create(nitrogen=nitrogen, phosphorus=phosphorus, potassium=potassium)

    except Exception as e:
        print(f"Error fetching or storing data: {e}")
