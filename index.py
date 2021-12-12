from flask import Flask, redirect, render_template, send_from_directory
#import render_template
import json
import request
#import redirect
#import send_from_directory
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__, static_url_path='/static', static_folder='templates/static') ##important
app.config['SECRET_KEY'] = 'nrfirfrifj_secret_key'


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/description')
def description():
    return render_template('description.html')

@app.route('/viewthedataset')
def showSignUp():
    return render_template('Table.html')

@app.route('/tops')
def topgenres():
    return render_template('Top20_genres_pie.html')

@app.route('/ab')
def ab():
    return render_template('ab.html')

@app.route('/success')
def Success():
    return render_template('success.html')

@app.route('/base')
def base():
    return render_template('base.html')

if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')