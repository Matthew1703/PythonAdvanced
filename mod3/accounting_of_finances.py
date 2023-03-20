from flask import Flask

app = Flask(__name__)

storage = {2023: {2: {1: 1000, 2: 800, 5: 500, 11: 200, 13: 100}, 3: {1: 100, 7: 300, 22: 1100}}}

@app.route("/add/<date>/<int:number>")
def addDay(date: str, number: int) -> str:
    day = int(date[6:8])
    month = int(date[4:6])
    year = int(date[:4])
    global storage
    storage.setdefault(year, {}).setdefault(month, {}).setdefault(day, 0)
    storage[year][month][day] += number
    return f"Дата: {year}-{month}-{day} <br>Траты: {str(storage[year][month][day])}"

@app.route("/calculate/<int:year>")
def calculYear(year: int) -> str:
    global storage
    summ = 0
    for value in storage[year].values():
        summ += sum(value.values())
    return f"Траты за год({year}): {str(summ)}"

@app.route("/calculate/<int:year>/<int:month>")
def calculMonth(year: int, month: int) -> str:
    global storage
    return f"Траты за месяц({year}-{month}): {str(sum(storage[year][month].values()))}"

if __name__ == "__main__":
    app.run(debug=True)
