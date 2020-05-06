"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from Assignment5130Gadi import app
from Assignment5130Gadi.Models.LocalDatabaseRoutines import create_LocalDatabaseServiceRoutines
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure


from datetime import datetime
from flask import render_template, redirect, request

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import json 
import requests

import io
import base64

from os import path

from flask   import Flask, render_template, flash, request
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from wtforms import TextField, TextAreaField, SubmitField, SelectField, DateField
from wtforms import ValidationError


from Assignment5130Gadi.Models.QueryFormStructure import LoginFormStructure 
from Assignment5130Gadi.Models.QueryFormStructure import UserRegistrationFormStructure 

from flask_bootstrap import Bootstrap
bootstrap = Bootstrap(app)

from Assignment5130Gadi.Models.Forms import ExpandForm
from Assignment5130Gadi.Models.Forms import CollapseForm
from Assignment5130Gadi.Models.Forms import GamesPoints



db_Functions = create_LocalDatabaseServiceRoutines() 

app.config['SECRET_KEY'] = 'All You Need Is Love Ta ta ta ta ta'

def plot_to_img(fig):
    pngImage = io.BytesIO()
    FigureCanvas(fig).print_png(pngImage)
    pngImageB64String = "data:image/png;base64,"
    pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')
    return pngImageB64String



@app.route('/')
@app.route('/home')
def home():
    return render_template(
        'home.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/datamodel')
def datamodel():
    return render_template(
        'datamodel.html',
        title='Data Model',
        year=datetime.now().year,
    )

@app.route('/register', methods=['GET', 'POST'])
def Register():
    form = UserRegistrationFormStructure(request.form)

    if (request.method == 'POST' and form.validate()):
        if (not db_Functions.IsUserExist(form.username.data)):
            db_Functions.AddNewUser(form)
            db_table = ""

            flash('Thanks for registering new user - '+ form.FirstName.data + " " + form.LastName.data )
        else:
            flash('Error: User with this Username already exist ! - '+ form.username.data)
            form = UserRegistrationFormStructure(request.form)

    return render_template(
        'register.html', 
        form=form, 
        title='Register New User',
        year=datetime.now().year,
        repository_name='Pandas',
        )

@app.route('/login', methods=['GET', 'POST'])
def Login():
    form = LoginFormStructure(request.form)

    if (request.method == 'POST' and form.validate()):
        if (db_Functions.IsLoginGood(form.username.data, form.password.data)):
            flash('Login approved!')
            return redirect('DataQuery')   

        else:
            flash('Error in - Username and/or password')
   
    return render_template(
        'login.html', 
        form=form, 
        title='Login to data analysis',
        year=datetime.now().year,
        repository_name='Pandas',
        )

@app.route('/data/data1' , methods = ['GET' , 'POST'])
def data1():
    """Renders the about page."""
    form1 = ExpandForm()
    form2 = CollapseForm()
    df = pd.read_csv(path.join(path.dirname(__file__), 'static/data/Jordan.csv'))
    raw_data_table = ''

    if request.method == 'POST':
        if request.form['action'] == 'Expand' and form1.validate_on_submit():
            raw_data_table = df.to_html(classes = 'table table-hover')
        if request.form['action'] == 'Collapse' and form2.validate_on_submit():
            raw_data_table = ''

    

    return render_template(
        'data1.html',
        title='Data 1',
        year=datetime.now().year,
        message='My Data 1 page.',
        raw_data_table = raw_data_table,
        form1 = form1,
        form2 = form2
    )


@app.route('/data/data2' , methods = ['GET' , 'POST'])
def data2():
    """Renders the about page."""
    form1 = ExpandForm()
    form2 = CollapseForm()
    df = pd.read_csv(path.join(path.dirname(__file__), 'static/data/LeBron.csv'))
    raw_data_table = ''

    if request.method == 'POST':
        if request.form['action'] == 'Expand' and form1.validate_on_submit():
            raw_data_table = df.to_html(classes = 'table table-hover')
        if request.form['action'] == 'Collapse' and form2.validate_on_submit():
            raw_data_table = ''

    

    return render_template(
        'data2.html',
        title='Data 2',
        year=datetime.now().year,
        message='My Data 2 page.',
        raw_data_table = raw_data_table,
        form1 = form1,
        form2 = form2
    )


@app.route('/data/data3' , methods = ['GET' , 'POST'])
def data3():
    """Renders the about page."""
    form1 = ExpandForm()
    form2 = CollapseForm()
    df = pd.read_csv(path.join(path.dirname(__file__), 'static/data/Kobe.csv'))
    raw_data_table = ''

    if request.method == 'POST':
        if request.form['action'] == 'Expand' and form1.validate_on_submit():
            raw_data_table = df.to_html(classes = 'table table-hover')
        if request.form['action'] == 'Collapse' and form2.validate_on_submit():
            raw_data_table = ''

    

    return render_template(
        'data3.html',
        title='Data 3',
        year=datetime.now().year,
        message='My Data 3 page.',
        raw_data_table = raw_data_table,
        form1 = form1,
        form2 = form2
    )

@app.route('/DataQuery' , methods = ['GET' , 'POST'])
def DataQuery():

    print("Data Query")

    form1 = GamesPoints()
    chart = '/static/imgs/img.jpg'
    message = ''

   
    Jordan = pd.read_csv(path.join(path.dirname(__file__), 'static/Data/Jordan.csv'))
    Kobe = pd.read_csv(path.join(path.dirname(__file__), 'static/Data/Kobe.csv'))
    LeBron = pd.read_csv(path.join(path.dirname(__file__), 'static/Data/LeBron.csv'))


    if request.method == 'POST':
        points = form1.points.data
        
        Games_with_points = Jordan[(Jordan['PTS'] >= points)].drop(['AST', 'TRB', 'MP', 'FG%', '3P%', 'FT%', 'STL', 'BLK', 'TOV', 'PF', 'G', 'Date', 'Tm', 'X', 'Opp', 'Result', 'GS', 'FG', 'FGA', '3P', '3PA', 'FT', 'FTA', 'ORB', 'DRB', 'GmSc', 'Player', 'RSorPO'], 1)
        Jordan_Qualified_games = Games_with_points['PTS'].size
        Jordan_Total = int(len(Jordan.index))
    
        Games_with_points = Kobe[(Kobe['PTS'] >= points)].drop(['AST', 'TRB', 'MP', 'FG%', '3P%', 'FT%', 'STL', 'BLK', 'TOV', 'PF', 'G', 'Date', 'Tm', 'X', 'Opp', 'Result', 'GS', 'FG', 'FGA', '3P', '3PA', 'FT', 'FTA', 'ORB', 'DRB', 'GmSc', 'Player', 'RSorPO'], 1)
        Kobe_Qualified_games = Games_with_points['PTS'].size
        Kobe_Total = int(len(Kobe.index))
    

        Games_with_points = LeBron[(LeBron['PTS'] >= points)].drop(['AST', 'TRB', 'MP', 'FG%', '3P%', 'FT%', 'STL', 'BLK', 'TOV', 'PF', 'G', 'Date', 'Tm', 'X', 'Opp', 'Result', 'GS', 'FG', 'FGA', '3P', '3PA', 'FT', 'FTA', 'ORB', 'DRB', 'GmSc', 'Player', 'RSorPO'], 1)
        LeBron_Qualified_games = Games_with_points['PTS'].size
        LeBron_Total = int(len(LeBron.index))
    
        qualified = [Jordan_Qualified_games, Kobe_Qualified_games, LeBron_Qualified_games]
        total = [Jordan_Total, Kobe_Total, LeBron_Total]
        index = ['Michael Jordan', 'Kobe Bryant', 'LeBron James']
        df = pd.DataFrame({'Qualified Games': qualified,
                            'Total Games': total}, index=index)
        ax = df.plot.bar(rot=0)
        fig = plt.figure()
        ax = fig.add_subplot(111)
        fig.subplots_adjust(bottom=0.4)
        df.plot(ax = ax , kind = 'bar', figsize = (24, 8) , fontsize = 22 , grid = True)
        chart = plot_to_img(fig)

        message = 'Michael Jordan had ' + str(Jordan_Qualified_games) + " " +  str(points) + ' point games, Kobe Bryant had ' + str(Kobe_Qualified_games) + " " + str(points) + ' point games and LeBron James had ' + str(LeBron_Qualified_games) + " " + str(points) + ' point games.'

    
    return render_template(
        'DataQuery.html',
        form1 = form1,
        chart = chart,
        message = message
    )


