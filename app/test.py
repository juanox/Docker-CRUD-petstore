from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'mysqldb'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_HOST'] = 'db'

mysql = MySQL(app)


@app.route('/', methods=['GET'])
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM mysqldb.Customer")
    mysql.connection.commit()
    rows = cur.fetchall()
    cur.execute("SELECT * FROM mysqldb.Order")
    mysql.connection.commit()
    rows2 = cur.fetchall()
    cur.execute("SELECT * FROM mysqldb.Pet")
    mysql.connection.commit()
    rows3 = cur.fetchall()
    cur.close()
    return render_template('index.html', rows=rows, rows2=rows2, rows3=rows3)


@app.route('/add', methods=['POST'])
def add():
    idCostumer = request.form['idCostumer']
    idPet = request.form['idPet']
    price = request.form['price']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO mysqldb.Order (idCustomer, idPet, pet_price) VALUES (%s, %s, %s)",
                (idCostumer, idPet, price))
    mysql.connection.commit()
    return redirect(url_for('index'))


@app.route('/modify', methods=['POST'])
def modify():
    idOrder = request.form['id']
    idCustomer = request.form['idCustomer']
    idPet = request.form['idPet']
    price = request.form['price']
    cur = mysql.connection.cursor()
    cur.execute("UPDATE mysqldb.Order SET idCustomer=%s, idPet=%s, pet_price=%s WHERE idOrder=%s", (idCustomer, idPet, price, idOrder))
    mysql.connection.commit()
    return redirect(url_for('index'))


@app.route('/delete/<string:id_order>', methods=['GET'])
def delete(id_order):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM mysqldb.Order WHERE idOrder=%s", (id_order))
    mysql.connection.commit()
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
