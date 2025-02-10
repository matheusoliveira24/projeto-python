from flask import Flask, render_template

app = Flask(__name__)

@app.route('/a')
def home():
    return render_template('base.html', title='Adicionar Tarefa')