from vsearch import search4letters
from flask import Flask, render_template,request,escape

app = Flask(__name__)

def log_request(req:'flask_request',res:str) :
    with open('vsearch.log','a') as log :
        #print(str(dir(req)),res,file=log)
        print(req.form,req.user_agent,req.remote_addr,res,file=log,sep='|')

@app.route('/search4',methods = ['POST'])
def search4() -> str:
    """Returns the results of a call to 'search4letters' to the browser."""
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'here are you results'
    results = str(search4letters(phrase,letters))
    log_request(request,results)
    return (render_template('results.html',the_phrase = phrase,the_letters = letters,the_title = title,the_results = results))

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    """Returns the entry page to browser."""
    return render_template('entry.html',
                           the_title='Welcome to search4letters on the web!')

@app.route('/viewlog')
def view_the_log()->str :
    with open('vsearch.log') as log :
        contents = log.read()
    return escape(contents)

@app.route('/bim')
def test() :
    pass
app.run(debug=True)
