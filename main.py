from flask import Flask, render_template, url_for, request, flash, redirect, session
# from flask_mysqldb import MySQL
import mysql.connector

app = Flask(__name__)
app.secret_key = 'pjrgwrhogvnoi37292t97t-+*gg@#TY8ppP2PP@DFH#$^&26XZ'

# app.config['MYSQL_HOST'] = "localhost"
# app.config['MYSQL_USER'] = "root"
# app.config['MYSQL_PASSWORD'] = 'philip'
# app.config['MYSQL_DB'] = "flask"

# mysql = MySQL(app)
mydb = mysql.connector.connect(
    host="localhost",
    port=3307,
    user="root",
    password="philip",
    database="flask"
    
)

cursor = mydb.cursor()
@app.route("/")
def index():
    # session['isthereuser'] = ''
    if 'isthereuser' in session:
        if session['isthereuser'] != '':
            user = session['isthereuser']
            # cursor = mysql.connection.cursor()
            cursor.execute(
                f"SELECT THEY FROM flask.msseges where THEY='{user}'")
            data = cursor.fetchall()
            if len(data) > 0:
                cursor.execute(
                    f"SELECT ME FROM flask.msseges where THEY='{user}'")
                data = cursor.fetchall()
                mevar = data
                cursor.execute(
                    f"SELECT MSSEGE FROM flask.msseges where THEY='{user}'")
                data = cursor.fetchall()
                # cursor.close()
                mssegevar = data
                return render_template('tousers.html', usert=user, they=mevar, mssege=mssegevar, num=len(mevar)-1)
            else:
                return render_template('tousers.html', usert=user, they='', mssege='', num=0)
        else:
            return render_template('index.html')
    else:
        return render_template('index.html')


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == 'POST':
        username = request.form['textbox']
        password = request.form['password']
        
        # cursor = mysql.connection.cursor()
        cursor.execute(
            f"SELECT USERNAME FROM flask.users where USERNAME='{username}'")
        data = cursor.fetchall()
        print(data)
        if len(data) > 0:
            cursor.execute(
                f"SELECT PASSWORD FROM flask.users where USERNAME='{username}'")
            data1 = cursor.fetchall()
            print(data1[0][0])
            print(password)
            print(int(data1[0][0]) == int(password))
            # cursor.close()
            if int(data1[0][0]) == int(password):
                print(True)
                # flash("You are connected", category="s")
                # return render_template('index.html')
                # print(url_for('index'))
                session['isthereuser'] = username
                return redirect('/')
            else:
                print(False)
                flash("error", category="e")
        else:
            flash("error", category="e")

    return render_template('second.html')


@app.route("/signup", methods=["POST", "GET"])
def singup():
    if request.method == 'POST':
        name = request.form['name']
        username = request.form['textbox']
        password = request.form['password']

        # cursor = mysql.connection.cursor()
        cursor.execute(
            f"SELECT USERNAME FROM flask.users where USERNAME='{username}'")
        data = cursor.fetchall()
        if len(data) > 0:
            flash("This username is taken, please change the username",
                  category='error')
        else:
            cursor.execute(
                f"INSERT INTO USERS(NAME, USERNAME, PASSWORD) VALUES('{name}','{username}','{password}')")
            mydb.commit()
            cursor.close()
            mydb.close()
            # cursor.close()

    return render_template('third.html')


@app.route("/leave", methods=["POST", "GET"])
def leave():
    if 'isthereuser' in session:
        session['isthereuser'] = ''
    return redirect(url_for('index'))


@app.route("/send", methods=["POST", "GET"])
def send():
    print('hi')
    if request.method == 'POST':

        they = request.form['addressee']
        messege = request.form['message']

        # cursor = mysql.connection.cursor()
        cursor.execute(
            f"SELECT USERNAME FROM flask.users where USERNAME='{they}'")
        data = cursor.fetchall()
        if len(data) > 0:
            cursor.execute(
                f"INSERT INTO msseges(me, they, mssege) VALUES('{session['isthereuser']}','{they}','{messege}')")
            mydb.commit()
            cursor.close()
            mydb.close()
            # cursor.close()
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
