from flask import Flask

app = Flask(__name__)

count = 0
@app.route('/counter')
def counter():
    global count
    count += 1
    return str(count)

if __name__ == "__main__":
    app.run(port=55555, debug=True)