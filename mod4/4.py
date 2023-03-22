from flask import Flask
import sys

app = Flask(__name__)

line = sys.stdin.readline()
args = line.split(' ')
res_line = args[1:]
res_line = ''.join(res_line)

@app.route("/uptime", methods=["GET"])
def upTimee():
    """Передача данных происходит через конвейер pipe в терминале"""
    UPTIME = res_line
    return f"Current uptime is {UPTIME}"

if __name__ == "__main__":
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(port=55555, debug=False)