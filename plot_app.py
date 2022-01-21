from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/html')
def hello_html():
    return render_template('hello.html')

@app.route('/template')
def template():
    return render_template('template.html', tekst='Dit is nu de tekst')

@app.route('/plot/<int:plot_keuze>')
def plot(plot_keuze):

    data = pd.read_csv('plot_data.csv')

    if plot_keuze == 1:
        plt.figure(figsize=(15, 7))
        plt.bar(data.columns[1:], data.mean())
        plt.ylabel('Hoeveelheid [mg/100g]')
        plt.xlabel('Voedingsstof')
        plt.xticks(rotation=90)
        plt.savefig('static/plot.png')
    elif plot_keuze == 2: 
        plt.figure(figsize=(15, 7))
        plt.hist(data['Calcium (Ca)'], log=True, bins=50)
        plt.title ('Hoeveelheid calcium van verschillende voedingsmiddelen')
        plt.ylabel('Aantal voedingsmiddelen')
        plt.xlabel('Ca (mg/100g)')
    else:
        plt.plot(range(10))

        
    plt.savefig('static/plot.png')
    plt.close()

    return render_template('plot.html')