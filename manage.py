from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index_football.html')

@app.route('/about')
def aboutPage():
    return render_template('about_us.html')

@app.route('/contact') 
def contactUs():
     return render_template('contact_us.html')  

@app.route('/login') 
def login():
    return render_template('login.html') 

@app.route('/register')
def register():
    return render_template('register.html')     

app.run()