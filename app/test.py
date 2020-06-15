from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'mysqldb'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_HOST'] = 'db'

mysql = MySQL(app)

@app.route('/',methods=['GET'])
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Student")
    mysql.connection.commit()
    rows=cur.fetchall()
    return render_template('index.html', rows=rows)

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5000, debug = True)
