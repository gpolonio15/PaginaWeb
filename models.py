import db
from sqlalchemy import Column, Integer, String, Float
from werkzeug.security import check_password_hash as checkph
from werkzeug.security import generate_password_hash as genph



class Producto(db.Base):
    __tablename__="producto"
    id = Column(Integer, primary_key=True)
    nombreEmpresa= Column(String(200), nullable=False)
    telefono= Column(Integer, nullable=False)
    direccion= Column(String(200), nullable=False)
    cif= Column(String(200), nullable=False)
    precio = Column(Float, nullable=False)
    porcentaje_descuento= Column(Integer, nullable=False)
    color = Column(String(200), nullable=False)
    descripcion= Column(String(200), nullable=False)
    marca= Column(String(200), nullable=False)
    cantidad= Column(Integer, nullable=False)
    referencia= Column(String(200), nullable=False)
    email= Column(String(200), nullable=False)

    def __init__(self,nombreEmpresa,telefono,direccion,cif,precio,porcentaje_descuento,color,descripcion,marca,cantidad,referencia,email):
        self.nombreEmpresa = nombreEmpresa
        self.telefono= telefono
        self.direccion= direccion
        self.cif= cif
        self.precio= precio
        self.porcentaje_descuento= porcentaje_descuento
        self.color= color
        self.descripcion= descripcion
        self.marca= marca
        self.cantidad= cantidad
        self.referencia= referencia
        self.email= email


    def __repr__(self):
        return "Cliente {}:{} {} {} {} {} {} {} {} {} {} {} ({})".format(self.id,self.nombreEmpresa,self.telefono,self.direccion,self.cif, self.precio,self.porcentaje_descuento, self.color,self.descripcion,self.marca,self.referencia,self.email, self.cantidad)

    def __str__(self):
        return "Cliente {}:{} {} {} {} {} {} {} {} {} {} {} ({})".format(self.id,self.nombreEmpresa,self.telefono,self.direccion,self.cif, self.precio,self.porcentaje_descuento, self.color,self.descripcion,self.marca, self.referencia,self.email, self.cantidad)


class User (db.Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String(40), unique=True, nullable=False)
    password = Column(String(40), unique = True, nullable = False)


    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return "Contaseña {} {} {}".format(self.id, self.username, self.password)

    def def_clave(self, password):
        self.password = genph(password)

    def verif_clave(self, password):
        return checkph(self.password, password)


class Ventas(db.Base):
    __tablename__ = "ventas"
    id = Column(Integer, primary_key=True)
    venta= Column(Integer, nullable=False)
    referencia= Column(String(200), nullable=False)
    precio= Column(Float, nullable=False)
    ganancias= Column(Float, nullable=False)

    def __init__(self,venta, referencia, precio,ganancias):
        self.venta = venta
        self.referencia= referencia
        self.precio=precio
        self.ganancias=ganancias
    def __repr__(self):
        return "Ventas {}:{} {} {} {}". format(self.id, self.venta, self.referencia, self.precio, self.ganancias)

class Cliente(db.Base):
    __tablename__ = "cliente"
    id = Column(Integer, primary_key=True)
    nombre= Column(String(200), nullable=False)
    direccion= Column(String(200), nullable=False)
    postal= Column(Integer, nullable=False)
    telefono= Column(Integer, nullable=False)
    mail= Column(String(200), nullable=False)


    def __init__(self, nombre, direccion, postal, telefono, mail):
        self.nombre = nombre
        self.direccion = direccion
        self.postal = postal
        self.telefono = telefono
        self.mail=mail

    def __repr__(self):
        return "Ventas {}:{} {} {} {} {}".format(self.id, self.nombre, self.direccion, self.postal, self.telefono, self.mail)