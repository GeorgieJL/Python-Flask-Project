from flask import render_template

from application import app


@app.route('/home')
@app.route('/')
def home():
    return render_template('home.html', title='Home')


@app.route('/about')
def about():
    return render_template('About.html', title='About', name='Marge')


@app.route('/city')
def city():
    return render_template('city.html', title='City', city='Springfield')

