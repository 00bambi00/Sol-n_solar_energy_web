#fetch_solar_data.py

import requests
from datetime import datetime, timedelta

def get_average_irradiance(lat, lon):
    end_date = datetime.utcnow()
    start_date = end_date - timedelta(days=6)

    url = "https://power.larc.nasa.gov/api/temporal/daily/point"
    params = {
        "start": start_date.strftime("%Y%m%d"),
        "end": end_date.strftime("%Y%m%d"),
        "latitude": lat,
        "longitude": lon,
        "community": "RE",
        "parameters": "ALLSKY_SFC_SW_DWN",
        "format": "JSON"
    }
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        json_data = response.json()
        irr_dict = json_data["properties"]["parameter"]["ALLSKY_SFC_SW_DWN"]
        values = [v for v in irr_dict.values() if v is not None and v >= 0]
        return sum(values) / len(values) if values else None
    except Exception as e:
        print(f"Error fetching irradiance data: {e}")
        return None

def get_hourly_irradiance(lat, lon):
    try:
        url = (
            f"https://api.open-meteo.com/v1/forecast?"
            f"latitude={lat}&longitude={lon}&hourly=shortwave_radiation&timezone=auto"
        )
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        times = data["hourly"]["time"]
        values = data["hourly"]["shortwave_radiation"]

        hourly_data = {
            t.split("T")[1][:5]: v for t, v in zip(times, values)
        }
        return hourly_data
    except Exception as e:
        print(f"Error fetching hourly irradiance: {e}")
        return None




