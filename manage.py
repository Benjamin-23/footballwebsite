from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index_football.html')

@app.route('/about')
def aboutPage():
    return render_template('about_us.html')

app.run()