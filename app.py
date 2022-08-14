from flask import Flask, render_template, request
from flask_mysqldb import MySQL
app=Flask(__name__)
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'mypassword'
app.config['MYSQL_DB'] = 'agenda'
mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        nombre = request.form['nombre']
        direccion = request.form['direccion']
        telefono = request.form['telefono']
        local = request.form['local']
        destino = request.form['destino']
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO contactos (nombre,direccion,telefono,local,destino) VALUES(%s,%s,%s,%s,%s,)'),
        (nombre,direccion,telefono,local,destino)
        mysql.connection.commit()
        return 'recivido'
@app.route('/edit')
def editar_contaco():
    return 'editar contactos'

@app.route('/delete')
def delete_contactos():
    return 'eliminar contactos'

if __name__ == '__main__':
    app.run(port = 3000, debug=True)



