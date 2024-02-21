from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/linear_motion')
def linear_motion():
    return render_template('linear_motion.html')

@app.route('/2d_motion')
def linear_motion():
    return render_template('2d_motion.html')

@app.route('/newtons_laws')
def newtons_laws():
    return render_template('newtons_laws')

@app.route('/forces')
def forces():
    return render_template('forces.html')

if __name__ == '__main__':
    app.run(debug=True)