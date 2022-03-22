from flask import Flask, render_template, request
import db
from models import Producto, User, Ventas, Cliente
from werkzeug.security import check_password_hash
import matplotlib.pyplot as plt
import pandas as pd
import sqlite3
import smtplib



app = Flask(__name__)  # En app se encuentra nuestro servidor web de Flask


@app.route('/', methods=['GET'])
def home():
    return render_template("index.html")

@app.route('/cliente', methods=['GET'])
def cliente():
    todos_los_productos = db.session.query(Producto).all()
    return render_template("cliente.html", lista_de_productos=todos_los_productos)

@app.route('/proveedor', methods=['GET'])
def entrar():
    return render_template("proveedor.html")

@app.route('/comprador', methods=['POST'])
def crear():
    try:
        creado= Producto(nombreEmpresa=request.form['nombreEmpresa'],
                     telefono=request.form['telefono'],
                     direccion=request.form['direccion'],
                     cif=request.form['cif'],
                     email= request.form['email'],
                     precio=request.form['precio'],
                     porcentaje_descuento=request.form['descuento'],
                     color=request.form['color'],
                     descripcion=request.form['descripcion'],
                     marca=request.form['marca'],
                     cantidad=request.form['cantidad'],
                     referencia=request.form['referencia'])
        db.session.add(creado)
        db.session.commit()
        return render_template("registrado.html")
    except:
        return render_template("error_proveedor.html")

@app.route('/volver_registro', methods=['GET'])
def volver_registro():
    return render_template("proveedor.html")

@app.route('/volver_index', methods=['GET'])
def volver_index():
    return render_template("index.html")

@app.route('/usuario', methods=['POST'])
def usuario():
    return render_template("password.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    user = db.session.query(User).filter_by(username=request.form['usuario']).first()
    if user and check_password_hash(user.password, request.form['contrasena']):
        todos_los_productos = db.session.query(Producto).all()
        return render_template("administrador.html", lista_de_adm=todos_los_productos)
    else:
        return render_template("Contraseña.html")

@app.route('/volver_login', methods=['GET'])
def volver_login():
    return render_template("password.html")

@app.route('/anadir_producto', methods=['GET'])
def anadir_producto():
    return render_template("anadir_producto.html")

@app.route('/cantidad_sumar', methods=['GET', 'POST'])
def ana():
    cantidad_proveedor= request.form['cantidad_nueva']
    producto_ref = db.session.query(Producto).filter_by(referencia=request.form['referencia_2']).first()
    try:
        if producto_ref.referencia == request.form['referencia_2']:
            producto_ref.cantidad= Producto.cantidad + cantidad_proveedor
            db.session.commit()
            return render_template("producto_ana.html")
        else:
            return("La referencia es incorrecta")
    except:
        return render_template("referencia_incorrecta.html")

@app.route('/referencia_incorrecta', methods=['GET'])
def referencia_incorrecta():
    return render_template("anadir_producto.html")

@app.route('/eliminar', methods=['GET', 'POST'])
def eliminar():
    return render_template("Eliminar_producto.html")

@app.route('/eliminar_producto', methods=['GET', 'POST'])
def eliminar_producto():
    producto_ref = db.session.query(Producto).filter_by(referencia=request.form['referencia_3']).first()
    try:
        if producto_ref.referencia == request.form['referencia_3']:
            db.session.query(Producto).filter_by(referencia=request.form['referencia_3']).delete()
            db.session.commit()
            return render_template("ele_producto.html")
        else:
            return ("La referencia o el cif son incorrectos")
    except:
        return render_template("ref_eliminar.html")

@app.route('/ele',methods=['GET', 'POST'])
def ele():
    return render_template("password.html")

@app.route('/graf', methods=['GET', 'POST'])
def grafica():
    con = sqlite3.connect('database/ProyectoFinal.db')
    cursor = con.cursor()
    df = pd.read_sql_query("SELECT marca,cantidad FROM Producto", con)
    fd = pd.read_sql_query("SELECT referencia,ganancias FROM Ventas", con)
    da = pd.read_sql_query("SELECT venta,referencia FROM Ventas", con)
    cursor.close()
    con.close()
    plt.title("Productos disponibles en la web")
    plt.bar(df.marca, df.cantidad)
    plt.savefig("new_plot.png")
    plt.title("Ganancias")
    plt.bar(fd.referencia, fd.ganancias)
    plt.savefig("ganancia_plot.png")
    plt.title("Ventas de la web")
    plt.bar(da.referencia, da.venta)
    plt.savefig("grafica_ventas.png")
    return render_template("graficos.html", name = 'new_plot.png', name_1='ganancia_plot.png', name_2= 'grafica_ventas.png'  )

@app.route('/grafica', methods=['GET', 'POST'])
def grafico():
    return render_template("graficos.html", name='new_plot.png')


@app.route('/vendido', methods=['GET', 'POST'])
def vender():
    cantidad_venta = request.form['venta']
    pro_ref = db.session.query(Producto).filter_by(referencia=request.form['referencia_4']).first()
    if pro_ref.referencia == request.form['referencia_4'] and pro_ref.cantidad >= int(cantidad_venta):
        pro_ref.cantidad = Producto.cantidad - cantidad_venta
        db.session.commit()
    else:
        return render_template("agotado.html")

    if int(cantidad_venta) >= 0.1*(pro_ref.cantidad):
        message = 'Desde Armario Casual nos gustaria indicarle que el stock de su producto {} se encuentra por debajo del 90%'.format(pro_ref.referencia)
        subject= 'Stock Armario Casual'
        message= 'Subject: {}\n\n {}'.format(subject, message)

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('g32pobag@gmail.com', 'policianacional15')
        server.sendmail('g32pobag@gmail.com',pro_ref.email, message)
        server.quit()

    if pro_ref.cantidad >= int(cantidad_venta):
        precio_descuento= (pro_ref.precio-(pro_ref.precio * (pro_ref.porcentaje_descuento/100)))
        precio_final= precio_descuento * int(cantidad_venta)
        ganancias_empresa= precio_final*0.05
        venta= Ventas(venta= request.form['venta'],
                  referencia= request.form['referencia_4'],
                  precio= precio_final,
                  ganancias= ganancias_empresa)
        db.session.add(venta)
        db.session.commit()
        con = sqlite3.connect('database/ProyectoFinal.db')
        cursor = con.cursor()
        seleccion = pd.read_sql_query('SELECT precio FROM Ventas ORDER BY id DESC LIMIT 1', con)
        selec = pd.read_sql_query('SELECT venta FROM Ventas ORDER BY id DESC LIMIT 1', con)
        cursor.close()
        con.close()
        return render_template("precio.html", lista_de_ventas=seleccion.precio.values[0], list= selec.venta.values[0])
    else:
        return render_template("agotado.html")




@app.route('/clientecompra', methods=['GET', 'POST'])
def cliente_com():
        datos = Cliente(nombre=request.form['nombre'],
                    direccion=request.form['direccion'],
                    postal=request.form['postal'],
                    telefono=request.form['telefono'],
                    mail=request.form['mail'])
        db.session.add(datos)
        db.session.commit()
        return render_template("producto_comprado.html")



@app.route('/beneficio', methods=['GET', 'POST'])
def beneficio():
    todos_las_ventas = db.session.query(Ventas).all()
    return render_template("beneficio.html", lista_de_ventas=todos_las_ventas)



if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine)
    app.run(debug=True)