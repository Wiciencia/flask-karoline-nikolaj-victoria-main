from flask import Flask, render_template, redirect
from app.config import Config
from app.forms import LoginForm
import sqlite3 as lite

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/side2/')
def pizzaer():
    return render_template("side2.html")

@app.route('/login/', methods=['POST', 'GET'])
def login():
    loginform = LoginForm()
    if loginform.validate_on_submit():
        #print(loginform.username.data)
        #print(loginform.password.data)
        con = None
        con = lite.connect("static/db/site.db")
        cur = con.cursor()
        sql = "SELECT name, pw FROM users WHERE (name = '"+loginform.username.data+"') AND (pw = '"+loginform.password.data+"')"
        cur.execute(sql)
        res = cur.fetchall()
        if res:
            return redirect('/')
        con.close()
    return render_template('login.html', loginform=loginform)

if __name__ == '__main__':
    app.debug = True
    #app.run(debug=True) #Kør kun på localhost
    app.run(host='0.0.0.0', port=5005)