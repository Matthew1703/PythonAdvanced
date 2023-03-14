from flask import Flask

app = Flask(__name__)

storage = {}

@app.route("/add/<date>/<int:number>")
def addDay(date, number) -> str:
    day = date[6:8]
    month = date[4:6]
    year = date[:4]
    return f"{day}"


# @app.route("/calculate/<int:year>")
# def calcul() -> str:
#     pass
#
# @app.route("/calculate/<int:year>/<int:month>")
# def calcul() -> str:
#     pass

if __name__ == "__main__":
    app.run(debug=True)
