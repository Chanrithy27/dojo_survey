from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)

app.secret_key = "this is a key to the city"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/survey', methods=['POST'])
def survey_info():
    session['username'] = request.form['name']
    session['location'] = request.form['dojoLocation']
    session[''] = request.form['']
    session[''] = request.form['']
    return redirect('/results')

@app.route('/results')
def display_results():
    return render_template('results.html')

if __name__ == "__main__":
    app.run(debug=True)