from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)

app.secret_key = "this is a key to the city"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def survey_info():
    session['username'] = request.form['name']
    session['location'] = request.form['dojoLocation']
    session['language'] = request.form['favLanguage']
    session['comments'] = request.form['comment']
    return redirect('/result')

@app.route('/result')
def display_results():
    return render_template('results.html', name_on_template=session['username'], location_on_template=session['location'], language_on_template=session['language'], comment_on_template=session['comments'])

@app.route('/home')
def home():
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)