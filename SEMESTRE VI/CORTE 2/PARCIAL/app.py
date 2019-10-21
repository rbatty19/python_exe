from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/empleados.db'

db = SQLAlchemy(app)


class Empleado(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.String(200))
    tipo = db.Column(db.String(200))
    nombres = db.Column(db.String(200))
    apellidos = db.Column(db.String(200))
    edad = db.Column(db.String(200))
    correo = db.Column(db.String(200))
    profesion = db.Column(db.String(200))
    telefono = db.Column(db.String(200))
    cargo = db.Column(db.String(200))
    salario = db.Column(db.String(200))
    done = db.Column(db.Boolean)

@app.route('/')
def home():
    empleados = Empleado.query.all()
    return render_template('index.html', empleados = empleados)

@app.route('/crear-emp', methods=['POST'])
def create():
    nuevoEmpleado = Empleado(numero=request.form['numero'],
    tipo=request.form['tipo'],
    nombres=request.form['nombres'],
    apellidos=request.form['apellidos'],
    edad=request.form['edad'],
    correo=request.form['correo'],
    profesion=request.form['profesion'],
    telefono=request.form['telefono'],
    cargo=request.form['cargo'],
    salario=request.form['salario'],
    done= False)
    db.session.add(nuevoEmpleado)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/done/<id>')
def done(id):
    empleado = Empleado.query.filter_by(id=int(id)).first()
    empleado.done = not(empleado.done)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/delete/<id>')
def delete(id):
    Empleado.query.filter_by(id=int(id)).delete()
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
