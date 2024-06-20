#importing modules
from flask import Flask, render_template, request, session, redirect
import pickle
import numpy as np
from flask_session import Session
import seaborn as sns
import matplotlib.pyplot as plt
model = pickle.load(open('stress.pkl', 'rb'))
app = Flask(__name__)
#dictionary to hold the registrant name and password
REGISTRANTS = {'Lokesh':'lokesh','Sanish':'sanish','Teja':'teja','Anush':'anush'}
#configure session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
@app.route("/")
def index():
    return render_template("index.html", name=session.get("name"))
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session["name"] = request.form.get("name")
        session["password"] = request.form.get("password")
        if (session["name"] in REGISTRANTS.keys() and session["password"] == REGISTRANTS[session["name"]]):
            return render_template('home.html')
        else:
            return render_template('incorrect.html')
    return render_template("login.html")
@app.route("/reg",methods=["POST","GET"])
def register():
    if request.method == "POST":
        name=request.form.get("name")
        password=request.form.get("password")
        REGISTRANTS[name]=password
        return render_template("index.html")
    return render_template("register.html")   
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")
#user gives inputs to this page
@app.route('/home')
def man():
    return render_template('home.html')
#user inputs are processed for prediction
@app.route('/predict', methods=['POST'])
def home():  
    data1 = request.form['a']
    data2 = request.form['b']
    data3 = request.form['c']
    data4 = request.form['d']
    data5 = request.form['e']
    data6 = request.form['f']
    data7 = request.form['g']
    data8 = request.form['h']
    if not data1 or not data2 or not data3 or not data4 or not data5 or not data6 or not data7 or not data8 :
        redirect('/home')
    arr = np.array([[data1, data2, data3, data4, data5, data6, data7, data8]])
    
    pred = model.predict(arr)
    return render_template('prediction.html', data=pred)
@app.route('/graphs')
def graph():
    return render_template("graphs.html")
@app.route('/charts')
def chart():
    return render_template("pie.html")
@app.route('/hist')
def hist():
    return render_template("hist.html")
@app.route('/heat')
def heat():
    return render_template("heat.html")
@app.route('/box')
def box():
    return render_template("box.html")
@app.route('/map')
def map():
    return render_template("map.html")
@app.route('/scatter')
def compare():
    return render_template("scatter.html")
if __name__ == "__main__":
    app.run(debug=True)
