from flask import Flask, render_template, request

app = Flask(__name__)

def bmi_cal(weight, height):
    return weight/(height/100)**2
@app.route("/", methods = ['GET', 'POST'])
def index_page():
    result = None
    if request.method == 'POST' and 'weight' in  request.form:
        result = bmi_cal(int(request.form.get('weight')), int(request.form.get('height')))
    return render_template('index.html', result = result)


app.run()