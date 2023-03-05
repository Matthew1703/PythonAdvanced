from flask import Flask

app = Flask(__name__)

@app.route('/hello_world')
def hello():
    return 'Привет, мир!'

if __name__ == "__main__":
    app.run(port=55555, debug=True)