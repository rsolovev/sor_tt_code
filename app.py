from datetime import datetime

from flask import Flask
import pytz

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    tz = pytz.timezone('Europe/Moscow')
    msc_now = datetime.now(tz)
    return "Current Moscow time is " + str(msc_now.strftime("%b %d %Y %H:%M:%S")) + "\n"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
