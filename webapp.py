from flask import Flask, render_template
from vsearch import search_for_letter

app=Flask(__name__)

@app.route('/')
def hello() ->str:
    return 'hello world from flask'

@app.route('/search')
def do_search() -> str:
	return str(search_for_letter('life,the universe,and everything','eiru,!'))

@app.route('/entry')
def entry_page() ->'html':
	return render_template('entry.html',the_title='welcome to search_for_letters on the web!')
	
app.run()
