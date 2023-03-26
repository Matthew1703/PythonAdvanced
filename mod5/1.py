import os, signal
import subprocess

from flask import Flask

app = Flask(__name__)

port = 5000
def lsof(port:int):
    try:
        app.run(port=port, debug=True)
    except:
        res = subprocess.run(["lsof", "-i", ":" + str(port)], capture_output=True, encoding='utf-8')
        lst_pid = set()
        for irow_with_pid in res.stdout.split("\n")[1:]:
            if irow_with_pid:
                lst_pid.add(irow_with_pid.split()[1])
        for i_pid in lst_pid:
            os.kill(int(i_pid), signal.SIGKILL)
        subprocess.run(["lsof", "-i", ":" + str(port)], capture_output=True, encoding='utf-8')

@app.route('/hello_world')
def hello():
    return 'Привет, мир!'

if __name__ == "__main__":
    lsof(port)
    app.run(port=port, debug=True)