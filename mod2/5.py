from flask import Flask

app = Flask(__name__)

@app.route("/max_number/<path:number>")
def max_num(number) -> str:
    lst = number.split('/')
    try:
        lst = [int(x) for x in lst]
        return f"Максимальное число:<i>{max(lst)}</i>"
    except:
        return "Ошибка: передано не числовое значение!"

if __name__ == "__main__":
    app.run(debug=True)
