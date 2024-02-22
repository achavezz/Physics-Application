from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/linear_motion", methods=["GET", "POST"])
def linear_motion():
    if request.method == "POST":
        return render_template("lm_submit.html")
    return render_template('linear_motion.html')

@app.route('/2d_motion')
def twod_motion():
    return render_template('2d_motion.html')

@app.route('/newtons_laws')
def newtons_laws():
    return render_template('newtons_laws.html')

@app.route('/forces')
def forces():
    return render_template('forces.html')

@app.route('/work_energy')
def work_energy():
    return render_template('work_energy.html')

if __name__ == '__main__':
    app.run(debug=True)