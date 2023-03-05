from flask import Flask

cars = 'Chevrolet, Renault, Ford, Lada'

app = Flask(__name__)

@app.route('/cars')
def carss():
    global cars
    return cars

if __name__ == "__main__":
    app.run(port=80, debug=True)