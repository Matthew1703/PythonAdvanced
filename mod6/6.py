from flask import Flask

app = Flask(__name__)

@app.route("/play/")
def play():
    return 'ff'

@app.route("/gg/")
def gg():
    return 'gg'
@app.errorhandler(404)
def handle_exception(e: 404):
    lst = []
    for rule in app.url_map.iter_rules():
        url = "http://localhost:5000" + str(rule.rule)
        lst.append(f"<a href='{url}'>{url}</a>")
    return f"Данная страница не найдена. Вы можете перейти по следующим ссылкам:<br>" \
           f"{'<br>'.join(lst[1:])}", 404

if __name__ == "__main__":
    app.run(debug=True)