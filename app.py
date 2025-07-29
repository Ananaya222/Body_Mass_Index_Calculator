# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('one.html')

@app.route('/index')
def index():
    return render_template('index1.html')

@app.route('/diabetics')
def diabetics():
    return render_template('diabetics.html')

@app.route('/obesity')
def obesity():
    return render_template('obesity.html')

@app.route('/hearthealth')
def hearthealth():
    return render_template('hearthealth.html')

@app.route('/vitamins')
def vitamins():
    return render_template('vitamins.html')

@app.route('/weightloss')
def weightloss():
    return render_template('weightloss.html')

@app.route('/medication')
def medication():
    return render_template('medication.html')

@app.route('/healthnews')
def healthnews():
    return render_template('healthnews.html')

@app.route('/fitness')
def fitness():
    return render_template('fitness.html')

@app.route('/nutrition')
def nutrition():
    return render_template('nutrition.html')

@app.route('/mentalhealth')
def mentalhealth():
    return render_template('mentalhealth.html')

if __name__ == '__main__':
    app.run(debug=True)
