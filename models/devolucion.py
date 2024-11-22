from utils.db import db
from dataclasses import dataclass
from models.producto import Producto
from models.pedido import Pedido

@dataclass
class Devolucion(db.Model):
    __tablename__ = 'devoluciones'
    
    devolucion_id = db.Column(db.Integer, primary_key=True)
    cantidad = db.Column(db.Integer)
    motivo = db.Column(db.String(250))
    fecha_devolucion = db.Column(db.DateTime)
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.producto_id'))
    pedido_id = db.Column(db.Integer, db.ForeignKey('pedidos.pedido_id'))
    
    def __init__ (self,cantidad,motivo,fecha_devolucion,producto_id,pedido_id):
        self.cantidad = cantidad
        self.motivo = motivo
        self.fecha_devolucion = fecha_devolucion
        self.producto_id = producto_id
        self.pedido_id = pedido_id