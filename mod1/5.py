from flask import Flask
import datetime

app = Flask(__name__)

@app.route('/get_time/future')
def get_time():
    time_after_hour = datetime.datetime.now() + datetime.timedelta(hours=1)
    return f"Точное время через час будет {time_after_hour}"

if __name__ == "__main__":
    app.run(debug=True)