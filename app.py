from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

# โหลด environment variables จาก .env
load_dotenv("/Users/sheribam/Desktop/sol-n_solar_web_project/access_key.env")

app = Flask(__name__)

# ดึง Unsplash API Key จาก .env
UNSPLASH_ACCESS_KEY = os.getenv("UNSPLASH_ACCESS_KEY")
print("UNSPLASH_ACCESS_KEY =", UNSPLASH_ACCESS_KEY)

def get_unsplash_image(city):
    if not UNSPLASH_ACCESS_KEY:
        return "/static/default.jpg"
    
    url = f"https://api.unsplash.com/photos/random?query={city}&orientation=landscape&client_id={UNSPLASH_ACCESS_KEY}"
    try:
        response = requests.get(url, timeout=4)
        data = response.json()
        return data['urls']['regular']
    except:
        return "/static/default.jpg"

@app.route("/", methods=["GET", "POST"])
def index():
    city = ""
    data = {}
    background_image_url = get_unsplash_image("solar")

    if request.method == "POST":
        city = request.form["city"]

        # ปลอมข้อมูลจำลอง:
        data = {
            "city": city,
            "lat": 13.7563,
            "lon": 100.5018,
            "irradiance": 5.6,
            "energy_kwh": 22.4,
            "hours": list(range(6, 19)),
            "values": [0, 1.2, 2.1, 3.5, 4.0, 3.8, 2.2, 1.1, 0.5, 0.2, 0, 0, 0],
            "hourly": [0, 150, 300, 500, 600, 550, 400, 250, 100, 50, 0, 0, 0]
        }

        background_image_url = get_unsplash_image(city)

    return render_template(
        "index.html",
        data=data,
        background_image_url=background_image_url
    )

if __name__ == "__main__":
    app.run(debug=True, port=5002)






