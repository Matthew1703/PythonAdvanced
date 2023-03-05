from flask import Flask
import datetime

app = Flask(__name__)

@app.route('/get_time/now')
def get_time():
    return f"Точное время: {datetime.datetime.now()}"

if __name__ == "__main__":
    app.run(port=5555, debug=True)