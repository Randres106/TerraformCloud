from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/')
def get_datetime():
    tz = pytz.timezone('UTC')  # Puedes ajustar a tu zona horaria preferida
    now = datetime.now(tz)
    return {"datetime": now.isoformat(), "timezone": str(now.tzinfo)}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
