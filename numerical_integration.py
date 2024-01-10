import math
from flask import Flask
from flask import request
app = Flask('_name_')
def BlackBoxFunction(x):
    f = math.sin(x)
    return f
@app.route('/numericalintegration/<length>/<width>')
def numericalintegration(length, width):
    LENGTH = float(width)
    WIDTH = float(length)
    var = " "
    x = " "
    N = [10, 100, 1000, 10000, 100000, 1000000, 10000000]
    l = len(N)
    for i in range(0, l):
        integral = 0.0
        dx = WIDTH-LENGTH/N[i]
        for j in range(1, N[i]):
            xp = dx*(j+0.5)
            di = BlackBoxFunction(xp)*dx
            integral += di
        print(abs(integral))    
        var += str(integral)+","
        x = var
    return x