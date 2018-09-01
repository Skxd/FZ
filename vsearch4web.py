from vsearch import search4letters
from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return 'Hello world from Flask!'

@app.route('/search4',methods = ['POST'])
def search4() -> str:
    """Returns the results of a call to 'search4letters' to the browser."""
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'here are you results'
    results = str(search4letters(phrase,letters))
    return (render_template('results.html',the_phrase = phrase,the_letters = letters,the_title = title,the_results = results))

@app.route('/entry')
def entry_page() -> 'html':
    """Returns the entry page to browser."""
    return render_template('entry.html',
                           the_title='Welcome to search4letters on the web!')

app.run(debug=True)
