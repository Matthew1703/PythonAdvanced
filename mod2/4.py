from flask import Flask
from datetime import datetime

app = Flask(__name__)

weekday = datetime.today().weekday()
days = ('понедельника', 'вторника', 'среды', 'четверга', 'пятницы', 'субботы', 'воскресенья')
@app.route("/hello-world/<name>")
def hello(name) -> str:
    if weekday == 0 or weekday == 1 or weekday == 3 or weekday == 6:
        return f"Привет, {name}! Хорошего {days[weekday]}"
    else:
        return f"Привет, {name}! Хорошей {days[weekday]}"

if __name__ == "__main__":
    app.run(debug=True)
