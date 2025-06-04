# fetch_hourly_solar.py

import requests
from datetime import datetime

def get_hourly_irradiance(lat, lon):
    today = datetime.utcnow().strftime("%Y%m%d")
    url = (
        f"https://power.larc.nasa.gov/api/temporal/hourly/point"
        f"?parameters=ALLSKY_SFC_SW_DWN"
        f"&community=RE"
        f"&latitude={lat}&longitude={lon}"
        f"&format=JSON"
        f"&start={today}&end={today}"
    )
    try:
        res = requests.get(url)
        res.raise_for_status()
        data = res.json()
        irradiance = data["properties"]["parameter"]["ALLSKY_SFC_SW_DWN"]
        hourly_data = {
            f"{k.split(':')[1]}:00": v
            for k, v in irradiance.items()
            if v is not None
        }
        return hourly_data
    except Exception as e:
        print("Error fetching hourly:", e)
        return None

