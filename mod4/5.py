import subprocess, shlex
from flask import Flask, request

app = Flask(__name__)

@app.route("/ps/", methods=["GET"])
def pss():
    args: list[str] = request.args.getlist('arg')
    user_cmd = ''.join(args)
    clean_user_cmd = shlex.quote(user_cmd)
    result = str(subprocess.check_output(["ps", clean_user_cmd]))
    return f"<pre>Your result</pre>\n{result}"

if __name__ == "__main__":
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)