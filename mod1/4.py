from flask import Flask
import datetime

app = Flask(__name__)

@app.route('/get_time/now')
def get_time():
    time = datetime.datetime.now()
    return f"Точное время: {time}"

if __name__ == "__main__":
    app.run(port=5555, debug=True)