from flask import Flask
import datetime

app = Flask(__name__)

@app.route('/get_time/future')
def get_time():
    return f"Точное время через час будет {datetime.datetime.now() + datetime.timedelta(hours=1)}"

if __name__ == "__main__":
    app.run(port=5555, debug=True)