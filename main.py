from flask import Flask, render_template, redirect, url_for, session, request
from flask_mysqldb import MySQL
import MySQLdb
import bcrypt
from flask_cors import CORS #comment this on deployment
import json

app = Flask(__name__, static_url_path='', static_folder='frontend/build')
CORS(app)
app.secret_key = "321"
app.config["MYSQL_HOST"] = "0.0.0.0"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_USER"] = "monty"
app.config["MYSQL_PASSWORD"] = "123"
app.config["MYSQL_DB"] = "testdb"

db = MySQL(app)

@app.route('/react', methods=["GET"])
def react():
    print("react...?!")
    return {
      'resultStatus': 'SUCCESS',
      'message': "Hello Api Handler"
      }


@app.route('/')
def index():
    return redirect(url_for('login'))

# @app.route('/login', methods=["GET", "POST"])
# def login():
#     if request.method == "POST":
#         if "username" in request.form and "password" in request.form:
#             username = request.form["username"]
#             password = request.form["password"]
#             cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
#             cursor.execute('SELECT * from login WHERE username="{}"'.format(username))
#             info = cursor.fetchone()
#             if info:
#                 matched = bcrypt.checkpw(password.encode('utf8'), info["password"].encode('utf8'))
#                 if info["username"] == username and matched:
#                     session['login_success'] = True
#                     return redirect(url_for("profile"))
#
#             return redirect(url_for("login"))
#     # return redirect(url_for('login'))
#     return render_template("login.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        try:
            creds = json.loads(request.data.decode('utf8'))
        except ValueError:
            return {
                'resultStatus': 'FAILED',
                'message': "Decondinf JSON has fled"
            }
        # need to send it in request form!!! because request data is just bytes
        if "username" in creds and "password" in creds:
            print("2")
            username = creds["username"]
            password = creds["password"]
            cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * from login WHERE username="{}"'.format(username))
            info = cursor.fetchone()
            if info:
                matched = bcrypt.checkpw(password.encode('utf8'), info["password"].encode('utf8'))
                if info["username"] == username and matched:
                    session['login_success'] = True
                    print("success!")
                    return {
                        'resultStatus': 'SUCCESS',
                        'message': "verified user"
                    }
            print("credentials are wrong!")
            return {
                'resultStatus': 'FAILED',
                'message': "FAILED"
            }
    # return redirect(url_for('login'))
    return {
        'resultStatus': 'FAILED',
        'message': "GOT A 'GET' REQUEST"
    }


@app.route('/logout')
def logout():
    session.pop("login_success", None)
    return redirect(url_for("login"))

@app.route('/register', methods = ["GET", "POST"])
def register():
    if request.method == "POST":
        if "username" in request.form and "password" in request.form:
            username = request.form["username"]
            hashed_pass = bcrypt.hashpw(request.form["password"].encode('utf8'), bcrypt.gensalt(10))
            password = hashed_pass
            cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute("INSERT INTO login (username, password) VALUES(%s, %s)", (username, password))
            db.connection.commit()
            return redirect(url_for("index"))

    return render_template("register.html")

@app.route('/profile')
def profile():
    if session and session['login_success']:
        return render_template("profile.html")
    else:
        return redirect(url_for("index"))


if __name__ == '__main__':
    app.run(debug=False)
