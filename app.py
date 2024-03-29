import os, json
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/linear_motion", methods=['POST', 'GET'])
def linear_motion():
    if request.method == "POST":
        lookup_value = request.form.get("lookup_value")
        given_value_1 = request.form.get("value_1")
        given_value_2 = request.form.get("value_2")
        given_value_3 = request.form.get("value_3")
        first_input = request.form.get("inputField1")
        second_input = request.form.get("inputField2")
        third_input = request.form.get("inputField3")
        dict = {
            given_value_1 : first_input,
            given_value_2 : second_input,
            given_value_3 : third_input,
        }
        json_dict = json.dumps(dict)
        return render_template('lm_submit.html', lookup_value=lookup_value, dict=json_dict)

    
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