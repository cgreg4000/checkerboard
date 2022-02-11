from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def eight_by_eight():
    return render_template('8_by_8.html')

@app.route('/<int:x>')
def eight_by_x(x):
    return render_template('8_by_x.html', x = x)

@app.route('/<int:x>/<int:y>')
def x_by_y(x, y):
    return render_template('x_by_y.html', x = x, y = y)

if __name__=="__main__":
    app.run(debug=True)