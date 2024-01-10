from flask import Flask
import math

app = Flask(__name__)

def BlackBoxFunction(x):
    return math.sin(x)

@app.route('/numericalintegration/<length>/<width>')
def numerical_integration(length, width):
    LENGTH = float(length)
    WIDTH = float(width)
    var = ""
    N = [10, 100, 1000, 10000, 100000, 1000000, 10000000]
    for i in N:
        integral = 0.0
        dx = (WIDTH - LENGTH) / i
        for j in range(1, i):
            xp = dx * (j + 0.5)
            integral += BlackBoxFunction(xp) * dx
        var += f"{integral},"
    return var

if __name__ == '__main__':
    app.run(debug=True)
